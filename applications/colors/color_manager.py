from typing import List, Set
import os, re, shutil

def monotone_set(src:str, dest:str, hue:float, sat:float = 0.5) -> None:
    """Recursively copies and converts a folder (src) of svg icons into a
    monochrome set (dest), given a hue and saturation (defaults to 0.5)."""

    if not 0 <= hue <= 1:
        raise ValueError("Hue must be between 0 and 1.")
    if not 0 <= sat <= 1:
        raise ValueError("Saturation must be between 0 and 1.")

    #shutil.copytree(src, dest, symlinks=False)
    copy_file_structure(src, dest)
    paths = get_paths(dest, ".svg")

    for path in paths:
        with open(path, 'r') as file:
            svg = file.read()
        colors = get_fill_colors(svg)

        if sat == 0:
            svg, _ = to_grayscale(svg, colors) # Faster, no color conversion.
        else:
            svg, _ = to_monotone(svg, colors, hue, sat)

        with open(path, 'w') as file:
            file.write(svg)

def copy_file_structure(src:str, dest:str):
    """Copies a directory tree, but changes symbolic links to point
    to files within the destination folder instead of the source.
    Assumes that no link points to files outside the source folder."""

    shutil.copytree(src, dest, symlinks=True)

    for root, dirs, files in os.walk(dest):
        for file in files:
            file_path = os.path.join(root, file)

            if os.path.islink(file_path):
                link_target = os.readlink(file_path)

                if not os.path.isabs(link_target): # Skip.
                    continue

                # Make link relative and update.
                link_base = os.path.dirname(file_path)
                relative_target = os.path.relpath(link_target, link_base)
                print("link_target: " + link_target)
                print("link_base: " + link_base)
                print("rel_target: " + relative_target)
                print()
                os.remove(file_path)

                # Replace root source folder with root destination folder.
                relative_target = relative_target.replace(src, dest, 1)
                os.symlink(relative_target, file_path)

def get_fill_colors(svg:str) -> Set[str]:
    """Return a list of all unique fill colors within a given string
    representing an svg-file."""

    colors = set()
    matches = re.findall(r"#[A-Fa-f0-9]{6}", svg)

    for match in matches:
        colors.add(match)

    return colors

def get_paths(folder:str, ext:str) -> List[str]:
    """Return path of every file with the given extension within a folder
    and its subfolders, excluding symbolic links."""

    paths = []

    for item in os.listdir(folder):
        item_path = os.path.join(folder, item)

        if os.path.islink(item_path): # Link.
            continue

        if os.path.isfile(item_path): # File.
            if item.lower().endswith(ext):
                paths.append(item_path)

        elif os.path.isdir(item_path): # Folder.
            subfolder_svg_paths = get_paths(item_path, ext)
            paths.extend(subfolder_svg_paths)

    return paths

def hex_color_to_grayscale(hex:str) -> str:
    """Convert a hexadecimal color to a hexadecimal grayscale equivalent."""

    hex = hex.lstrip('#')
    r,g,b = int(hex[0:2],16), int(hex[2:4],16), int(hex[4:6],16)
    gs = int(0.21*r + 0.72*g + 0.07*b)
    hex_gs = '#' + format(gs, '02x')*3

    return hex_gs

def to_grayscale(svg:str, colors:Set[str]) -> str:
    """Replace every instance of colors within the given list with their
    grayscale equivalent in the given string representing an svg-file."""

    gray_svg = svg
    graytones = set()

    for color in colors:
        graytone = hex_color_to_grayscale(color)
        graytones.add(graytone)
        gray_svg = re.sub(color, graytone, gray_svg)

    return gray_svg, graytones

def hex_to_rgb(hex):
    """Hexadecimal to RGB base 16."""

    hex = hex.lstrip('#')
    r = int(hex[0:2], 16)
    g = int(hex[2:4], 16)
    b = int(hex[4:6], 16)
    return r, g, b

def rgb_to_hsl(rgb):
    """RGB to HSL color-space."""

    r, g, b = rgb
    r /= 255.0; g /= 255.0; b /= 255.0
    max_val = max(r, g, b); min_val = min(r, g, b)
    h = s = l = (max_val + min_val) / 2.0

    if max_val == min_val:
        h = s = 0
    else:
        d = max_val - min_val
        s = d / (2.0 - max_val - min_val)

        if max_val == r:
            h = (g - b) / d + (6.0 if g < b else 0.0)
        elif max_val == g:
            h = (b - r) / d + 2.0
        else:
            h = (r - g) / d + 4.0
        h /= 6.0

    return h, s, l

def hue_to_rgb(p, q, t):
    """Hue to RGB values. Used only by hsl_to_rgb."""

    if t < 0: t += 1
    if t > 1: t -= 1
    if t < 1 / 6: return p + (q - p) * 6 * t
    if t < 1 / 2: return q
    if t < 2 / 3: return p + (q - p) * (2 / 3 - t) * 6

    return p

def hsl_to_rgb(hsl):
    """HSL to RGB color-space."""

    h, s, l = hsl

    if s == 0:
        r = g = b = l
    else:
        if l < 0.5: q = l * (1 + s)
        else: q = l + s - l * s
        p = 2 * l - q
        r = hue_to_rgb(p, q, h + 1 / 3)
        g = hue_to_rgb(p, q, h)
        b = hue_to_rgb(p, q, h - 1 / 3)

    r = int(round(r * 255))
    g = int(round(g * 255))
    b = int(round(b * 255))
    return r, g, b

def rgb_to_hex(rgb):
    """RGB base 16 to hexadecimal."""

    r, g, b = rgb
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def to_monotone(svg:str, colors:Set[str], hue:float, sat:float) -> str:
    """Replace every instance of color within the given list with their
    monotone equivalent in the given string representing an svg-file,
    determined by the given hue and saturation."""

    monotone_svg = svg
    monotones = set()

    for color in colors:
        graytone = hex_color_to_grayscale(color)
        _, _, l = rgb_to_hsl(hex_to_rgb(graytone))
        monotone = rgb_to_hex(hsl_to_rgb((hue, sat, l)))
        monotones.add(monotone)
        monotone_svg = re.sub(color, monotone, monotone_svg)

    return monotone_svg, monotones
