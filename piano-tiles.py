"""Click dark piano tiles at four explicitly configured screen coordinates."""

import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--columns', type=int, nargs=4, required=True,
        metavar=('X1', 'X2', 'X3', 'X4'),
        help='Screen x coordinates for the four game columns',
    )
    parser.add_argument('--y', type=int, default=475, help='Screen y coordinate')
    args = parser.parse_args(argv)
    if args.y < 0 or any(x < 0 for x in args.columns):
        parser.error('Screen coordinates must be non-negative')
    return args


def run(columns, y, screen, keyboard):
    width, height = screen.size()
    if y >= height or any(x >= width for x in columns):
        raise ValueError('Coordinates must be inside the current screen')
    while not keyboard.is_pressed('s'):
        for x in columns:
            if screen.pixel(x, y)[0] < 20:
                screen.click(x, y)


def main():
    args = parse_args()
    import pyautogui
    import keyboard

    run(args.columns, args.y, pyautogui, keyboard)


if __name__ == '__main__':
    main()

