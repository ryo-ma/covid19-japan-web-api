import unittest
import os


class SourceDataFormatTest(unittest.TestCase):

    def test_by_date_csv(self):
        self.assert_by_header_line('byDate.csv')

    def test_death_csv(self):
        self.assert_by_header_line('death.csv')

    def test_domestic_daily_report_csv(self):
        self.assert_by_header_line('domesticDailyReport.csv')

    def test_positive_detail_csv(self):
        self.assert_by_header_line('positiveDetail.csv')

    def test_prefectures_csv(self):
        self.assert_by_header_line('prefectures.csv')

    def assert_by_header_line(self, filename):
        EXPECTED_BASE_PATH = 'tests/expected-data-format/'
        SOURCE_DATA_BASE_PATH = 'data/2019-ncov-japan/Data/'
        expected = self.get_header_line(os.path.join(EXPECTED_BASE_PATH, filename))
        actual = self.get_header_line(os.path.join(SOURCE_DATA_BASE_PATH, filename))
        self.assertEqual(expected, actual)

    def get_header_line(self, path):
        with open(path, encoding='utf-8') as f:
            return f.readline().strip()


if __name__ == '__main__':
    unittest.main()
