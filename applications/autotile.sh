#!/bin/bash
# Desc: Auto-tiling by simulating keyboard shortcuts.
# Auth: Nicklas Vraa

# Full tiling.
max() {
    xdotool key "super+m" && sleep 0.05
}

# Half tiling.
left() {
    xdotool key "super+Left" && sleep 0.05
}
right() {
    xdotool key "super+Right" && sleep 0.05
}
up() {
    xdotool key "super+Up" && sleep 0.05
}
down() {
    xdotool key "super+Down" && sleep 0.05
}

# Quarter tiling.
left_up() {
    xdotool key "super+Left+Up" && sleep 0.05
}
left_down() {
    xdotool key "super+Left+Down" && sleep 0.05
}
right_up() {
    xdotool key "super+Right+Up" && sleep 0.05
}
right_down() {
    xdotool key "super+Right+Down" && sleep 0.05
}

# Array of open windows.
prev_windows=()
windows=()

# Update array of id's of all currently open application windows.
get_windows() {
    windows=($(wmctrl -l | awk '{print $1}' | tail -n +2))
}

# Set a given window to be active.
focus() {
    wmctrl -ia ${windows[$(($1 - 1))]}
    sleep 0.01
}

open() {
    if (($1 == 1)); then
        max
    elif (($1 == 2)); then
        right
        focus 1 && left
        focus 2
    elif (($1 == 3)); then
        right_down
        focus 2 && right_up
        focus 3
    elif (($1 == 4)); then
        left_down
        focus 1 && left_up
        focus 4
    fi
}

close() {
    if (($2 == 4)); then
        if (($1 == 4)); then
            focus 1 && down
        elif (($1 == 3)); then
            focus 3 && right && right
            focus 1 && down
        elif (($1 == 2)); then
            focus 2 && up && up
            focus 3 && right && right
            focus 1 && down
        elif (($1 == 1)); then
            focus 1 && left && left && down
            focus 2 && up && up
            focus 3 && right && right
        fi
        focus 3
    elif (($2 == 3)); then
        if (($1 == 3)); then
            focus 2 && down
        elif (($1 == 2)); then
            focus 2 && up
        elif (($1 == 1)); then
            focus 1 && left && left && down
            focus 2 && up
        fi
        focus 2
    elif (($2 == 2)); then
        max
    fi
}

# Main function.
auto_tile() {

    # Register initial state.
    get_windows
    prev_windows=("${windows[@]}")
    m=${#prev_windows[@]} # Previous window count.

    # Tiling loop (events).
    while true; do

        # Register current windows.
        get_windows
        n=${#windows[@]}

        # Get the difference between previous and current windows.
        diff=$(echo ${windows[@]} ${prev_windows[@]} | tr ' ' '\n' | sort | uniq -u)
        changed=($(echo ${diff[@]}))

        # If windows were opened.
        if ((n > m)); then
            echo "Window ${changed[@]: -1} was opened and given the number $n."
            open $n

        # If windows were closed.
        elif ((n < m)); then

            # Determine what numbers the closed windows were assigned.
            for i in "${!prev_windows[@]}"; do
                for j in "${!changed[@]}"; do
                    if [[ "${prev_windows[$i]}" -eq "${changed[$j]}" ]]; then
                        num=$(($i+1))
                        echo "Window ${changed[$j]} was closed and it was number $num."
                        close $num $m
                    fi
                done
            done
        fi

        # Tick rate.
        sleep 0.05

        # Set current windows as previous windows for next iteration.
        prev_windows=("${windows[@]}")
        m=$n
    done
}

auto_tile
