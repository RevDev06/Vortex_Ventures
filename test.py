import unittest
from PyQt6.QtWidgets import QApplication
from barra_carga import Window

app = QApplication([])


class TestWindow(unittest.TestCase):
    def setUp(self):
        self.window = Window()

    def test_init(self):
        self.assertEqual(self.window.prog_bar.value(), -1)
        self.assertEqual(self.window.timer.interval(), 500)

    def test_auto_increment(self):
        initial_value = self.window.prog_bar.value()
        self.window.auto_increment()
        self.assertEqual(self.window.prog_bar.value(), initial_value + 1)


if __name__ == '__main__':
    unittest.main()
