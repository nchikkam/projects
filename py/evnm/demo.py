from lib.fss import FSS
from lib.fss import logger
import unittest

class FSSTest(unittest.TestCase):

    def test_directory_creation_and_deletion(self):
        fss = FSS("id", "token")

        directory = "temp"
        current_dir = "."
        fss.create_directory(current_dir, directory)
        self.assertTrue(fss.directory_exists(directory))

        current_dir = "."
        fss.remove_directory(current_dir, directory)
        self.assertFalse(fss.directory_exists(directory))

    def test_file_creation_and_deletion_in_a_directory(self):
        fss = FSS('', '')

        test = "test"
        current_dir = "."
        fss.create_directory(current_dir, test)
        file_name = "dummy.txt"
        dst = "dst_" + file_name
        fss.create_file(test, file_name, dst)

        self.assertTrue(fss.file_exists(test, dst))

        fss.remove_file(test, dst)
        self.assertFalse(fss.file_exists(test, dst))
        current_dir = "."
        fss.remove_directory(current_dir, test)


    def test_overriding_a_file_in_a_directory(self):
        fss = FSS('', '')

        test = "test"
        current_dir = "."
        fss.create_directory(current_dir, test)
        file_name = "dummy.txt"
        dst = "dst_" + file_name
        fss.create_file(test, file_name, dst)

        self.assertTrue(fss.file_exists(test, dst))

        #overwrite
        file_name = "overwrite.txt"
        fss.create_file(test, file_name, dst)

        self.assertTrue(fss.file_exists(test, dst))

        fss.remove_file(test, dst)
        self.assertFalse(fss.file_exists(test, dst))

        current_dir = "."
        fss.remove_directory(current_dir, test)

    def test_reading_file(self):
        fss = FSS('', '')
        current_dir = "."
        dummy_dir = 'dummy'
        fss.create_directory(current_dir, dummy_dir)
        fss.create_file(dummy_dir, "dummy.txt", "toread.txt")

        handle = fss.get_file_handle(dummy_dir, "toread.txt")
        logger.info(handle.readlines())

        fss.close_file_handle(handle)
        fss.remove_file(dummy_dir, "toread.txt")
        current_dir = "."
        fss.remove_directory(current_dir, dummy_dir)

    def test_reading_non_existing_file(self):
        fss = FSS('', '')
        handle = fss.get_file_handle(".", "nonexisting.txt")
        self.assertEqual(handle, None)

    def test_directory_files(self):
        fss = FSS('','')

        current_dir = "."
        dummy_dir = 'dummy'
        fss.create_directory(current_dir, dummy_dir)
        fss.create_file(dummy_dir, "dummy.txt", "toread.txt")

        actual = fss.get_directory_contents(dummy_dir)

        self.assertTrue(actual[0].name in ["toread.txt"])

        fss.remove_file(dummy_dir, "toread.txt")
        current_dir = "."

        fss.remove_directory(current_dir, dummy_dir)
        actual = fss.get_directory_contents(dummy_dir)
        self.assertEqual(
            [],
            actual
        )

    def test_get_directories(self):
        fss = FSS('', '')

        directory = "."
        dummy_dir = 'dummy'
        fss.create_directory(directory, dummy_dir)
        fss.create_file(dummy_dir, "dummy.txt", "toread.txt")


        actual = fss.get_directories(dummy_dir)
        self.assertEqual(
            ['dummy'],
            actual
        )

        import os
        new_dir = os.path.join(directory, dummy_dir)

        dirs = ["1", "2", "3"]
        for d in dirs:
            fss.create_directory(new_dir, d)

        actual = fss.get_directories(dummy_dir)
        self.assertEqual(
            ['dummy', ['1'], ['2'], ['3']],
            actual
        )


        fss.remove_file(dummy_dir, "toread.txt")
        current_dir = os.path.join(".", dummy_dir)
        for d in dirs:
            fss.remove_directory(current_dir, d)

        actual = fss.get_directory_contents(dummy_dir)
        self.assertEqual(
            [],
            actual
        )

        current_dir = "."
        fss.remove_directory(current_dir, dummy_dir)

    def test_directory_size(self):
        fss = FSS('', '')

        test = "test"
        current_dir = "."
        fss.create_directory(current_dir, test)
        file_name = "dummy.txt"
        dst = "dst_" + file_name
        fss.create_file(test, file_name, dst)

        before = fss.get_directory_size(test)
        fss.remove_file(test, dst)

        after = fss.get_directory_size(test)
        logger.info(after)

        current_dir = "."
        fss.remove_directory(current_dir, test)

        logger.info(before)
        logger.info(after)
        self.assertTrue(before > after)

if __name__ == "__main__":
    unittest.main()