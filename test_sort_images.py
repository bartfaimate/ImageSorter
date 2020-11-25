import unittest
from pathlib import Path, PosixPath
from tempfile import TemporaryDirectory

from sort_images import ImageSorter

TEST_DIR = Path(__file__).parent.joinpath("test_images")

class TestSortImages(unittest.TestCase):
    
    def test_get_files(self):
        image_sorter = ImageSorter(TEST_DIR)
        files = image_sorter.get_files(TEST_DIR.joinpath("jpeg"))
        raw_files = image_sorter.get_files(TEST_DIR.joinpath("raw"))

        self.assertTrue(len(files) == 70)
        self.assertTrue(len(raw_files) == 70)

        self.assertTrue(list(raw_files)[0][0:3] == "DSC")
        self.assertFalse("RAW" in list(raw_files)[0])


    def test_copy(self):
        """
        copy xxxx xxxx xxxx contaning files to [dest] from [source] and create [dest] with parents
        files can have suffixes as well and can be given with full name 
        """
        pass

    def test_move(self):
        """
        copy xxxx xxxx xxxx contaning files to [dest] from [source] and create [dest] with parents
        xxxx can ends with .jpg or .png or any suffix

        """
        pass

    def test_delete(self):
        """
        delete xxxx xxxx xxxx contaning files from [source] 
        if xxxx is folder than delete it
        """
        pass

    

if __name__ == "__main__":
    unittest.main()