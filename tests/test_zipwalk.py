from unittest import TestCase

from zipwalk import zipwalk


ZIPFILE = 'tests/1.zip'


class TestZipWalk(TestCase):
    def test_zipwalk(self):
        """ Iterates over the zipfile """
        walker = zipwalk(ZIPFILE)

        # first level
        root, zips, files = next(walker)
        self.assertEqual(root.filename, 'tests/1.zip')
        self.assertListEqual(zips, ['2.zip'])
        self.assertListEqual(files, ['1a.txt', '1b.txt', '1c.txt', 'dir/d1.txt'])

        # second level
        root, zips, files = next(walker)
        self.assertEqual(root.filename, '2.zip')
        self.assertListEqual(zips, list())
        self.assertListEqual(files, ['2a.txt', '2b.txt', '2c.txt'])

    def test_total_files(self):
        """ Counts files """
        allfiles = set()

        for _, _, files in zipwalk(ZIPFILE):
            allfiles |= set(files)
        
        self.assertEqual(len(allfiles), 7)
