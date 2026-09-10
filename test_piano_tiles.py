import contextlib
import importlib.util
import io
from pathlib import Path
import unittest
from unittest.mock import Mock

spec = importlib.util.spec_from_file_location('piano_tiles', Path(__file__).with_name('piano-tiles.py'))
bot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bot)


class PianoTilesTests(unittest.TestCase):
    def test_requires_four_columns_before_loading_desktop_libraries(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                bot.parse_args(['--columns', '10', '20', '30'])

    def test_fourth_column_is_processed_and_bright_tiles_are_ignored(self):
        screen = Mock()
        screen.size.return_value = (1000, 800)
        screen.pixel.side_effect = [(0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 0)]
        keyboard = Mock()
        keyboard.is_pressed.side_effect = [False, True]
        bot.run([10, 20, 30, 40], 475, screen, keyboard)
        self.assertEqual([call.args for call in screen.click.call_args_list], [(10, 475), (40, 475)])

    def test_out_of_screen_coordinates_do_not_click(self):
        screen = Mock()
        screen.size.return_value = (100, 100)
        with self.assertRaises(ValueError):
            bot.run([10, 20, 30, 100], 50, screen, Mock())
        screen.click.assert_not_called()

    def test_stop_key_prevents_any_click(self):
        screen = Mock()
        screen.size.return_value = (100, 100)
        keyboard = Mock()
        keyboard.is_pressed.return_value = True
        bot.run([10, 20, 30, 40], 50, screen, keyboard)
        screen.pixel.assert_not_called()


if __name__ == '__main__':
    unittest.main()
