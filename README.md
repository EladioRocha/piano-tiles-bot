# Piano Tiles Screen Bot

A Python desktop automation experiment that samples four screen coordinates and clicks when a pixel's **red channel is below 20**. It uses PyAutoGUI for screen access and clicks, and `keyboard` for the stop key.

## Setup

Use Python 3 on a local desktop with screen and keyboard access. Install the two runtime dependencies in your Python environment:

```sh
python -m pip install pyautogui keyboard
```

## Configure and run

Position the game, then identify the horizontal center of each of its four columns and a shared vertical sampling position. Replace the example coordinates with values for your own screen:

```sh
python piano-tiles.py --columns 100 200 300 400 --y 475
```

| Argument | Meaning |
| --- | --- |
| `--columns X1 X2 X3 X4` | Required: exactly four non-negative horizontal coordinates. |
| `--y Y` | Shared vertical coordinate; defaults to `475`. |

The script starts sampling immediately and sends real mouse clicks. Hold `s` to exit the loop. Screen coordinates must be within the current screen bounds. Recalibrate after moving the game or changing display scaling.

## How it works

The loop checks the stop key, then samples each column at the configured row. The threshold tests only the red channel, so a low-red colored pixel may also trigger a click. There is no image recognition, game-window detection, or automatic calibration.

## Tests

```sh
python -m unittest discover -p test_piano_tiles.py
```

The four tests use screen and keyboard doubles to check the fourth column, stopping, screen bounds, and incomplete arguments. They do not capture the desktop or click.

## Files and limitations

- [piano-tiles.py](piano-tiles.py): argument parsing and the automation loop.
- [test_piano_tiles.py](test_piano_tiles.py): isolated regression tests.

The loop has no explicit delay or click debouncing. Performance and input permissions depend on the operating system. Desktop gameplay was not exercised during this documentation update.
