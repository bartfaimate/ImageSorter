#!/usr/bin/env python3
import unittest
import sys
from pathlib import Path

sys.path.append(Path(__file__).parents[1].joinpath('lib'))

for path in sys.path:
    print(path)
from tempfile import TemporaryDirectory, TemporaryFile
from unittest.main import main

from lib.darktable import Darktable


class TestDarktable(unittest.TestCase):

    pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
    