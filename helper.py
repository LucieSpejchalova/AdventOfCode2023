"""Helper class for AoC 2023"""

import os
import __main__ as main


class InputLoader:
    """Load the input file for corresponding day."""
    def __init__(self):
        self.input_file = self._get_input_file()

    @staticmethod
    def _get_input_file():
        path = os.path.abspath(main.__file__)
        file_name = path.replace(".py", "_input.txt")
        return file_name

    def load_input_file(self):
        with open(self._get_input_file(), encoding="utf-8", mode="r") as data_file:
            return data_file.readlines()
