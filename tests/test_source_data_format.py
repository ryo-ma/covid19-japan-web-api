import unittest
import os


class SourceDataFormatTest(unittest.TestCase):

    def test_by_date_csv(self):
        """
        : return : py : meth :.

        Args:
            self: (todo): write your description
        """
        self.assert_by_header_line('byDate.csv')

    def test_death_csv(self):
        """
        Test if the user - defined in the test.

        Args:
            self: (todo): write your description
        """
        self.assert_by_header_line('death.csv')

    def test_domestic_daily_report_csv(self):
        """
        Test for every test report.

        Args:
            self: (todo): write your description
        """
        self.assert_by_header_line('domesticDailyReport.csv')

    def test_positive_detail_csv(self):
        """
        Test if there is_positive.

        Args:
            self: (todo): write your description
        """
        self.assert_by_header_line('positiveDetail.csv')

    def test_prefectures_csv(self):
        """
        Determine all csv.

        Args:
            self: (todo): write your description
        """
        self.assert_by_header_line('prefectures.csv')

    def assert_by_header_line(self, filename):
        """
        Asserts that a header is in header.

        Args:
            self: (todo): write your description
            filename: (str): write your description
        """
        EXPECTED_BASE_PATH = 'tests/expected-data-format/'
        SOURCE_DATA_BASE_PATH = 'data/2019-ncov-japan/50_Data/'
        expected = self.get_header_line(os.path.join(EXPECTED_BASE_PATH, filename))
        actual = self.get_header_line(os.path.join(SOURCE_DATA_BASE_PATH, filename))
        self.assertEqual(expected, actual)

    def get_header_line(self, path):
        """
        Reads the header.

        Args:
            self: (todo): write your description
            path: (str): write your description
        """
        with open(path, encoding='utf-8') as f:
            return f.readline().strip()


if __name__ == '__main__':
    unittest.main()
