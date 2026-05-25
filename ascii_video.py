import cv2
import shutil
import sys
import numpy as np

# Better ASCII gradient
ASCII_CHARS = np.array(list(" .,:;irsXA253hMHGS#9B&@"))

# Get terminal size once
term_width, term_height = shutil.get_terminal_size()

# Reduce slightly for stability
WIDTH = max(40, term_width)
HEIGHT = max(20, term_height - 2)

# ANSI reset
RESET = "\033[0m"

# RGB -> ANSI
def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

# Convert frame to ASCII
def frame_to_ascii(frame):

    # Resize frame correctly
    resized = cv2.resize(
        frame,
        (WIDTH, HEIGHT),
        interpolation=cv2.INTER_AREA
    )

    # Split channels
    b = resized[:, :, 0]
    g = resized[:, :, 1]
    r = resized[:, :, 2]

    # Faster grayscale conversion
    gray = (0.299 * r + 0.587 * g + 0.114 * b).astype(np.uint8)

    # Map brightness to ASCII
    indices = (gray / 255 * (len(ASCII_CHARS) - 1)).astype(np.int32)

    chars = ASCII_CHARS[indices]

    lines = []

    # Build frame efficiently
    for y in range(chars.shape[0]):

        line = []

        for x in range(chars.shape[1]):

            line.append(
                f"{rgb_to_ansi(r[y,x], g[y,x], b[y,x])}{chars[y,x]}"
            )

        lines.append("".join(line))

    return "\n".join(lines)

# Webcam
cap = cv2.VideoCapture(0)

# Lower camera resolution for performance
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

if not cap.isOpened():
    print("Cannot access webcam")
    exit()

# Clear screen once
sys.stdout.write("\033[2J")

try:

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Mirror effect
        frame = cv2.flip(frame, 1)

        # Generate ASCII frame
        ascii_frame = frame_to_ascii(frame)

        # Move cursor to top
        sys.stdout.write("\033[H")

        # Print frame
        sys.stdout.write(ascii_frame)

        # Reset colors
        sys.stdout.write(RESET)

        # Flush instantly
        sys.stdout.flush()

        # Quit with q
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    pass

finally:

    cap.release()
    cv2.destroyAllWindows()

    print(RESET)