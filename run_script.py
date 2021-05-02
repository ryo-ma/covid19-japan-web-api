from src.script import create_prefectures
from src.script import create_total
from src.script import create_statistics_positives


if __name__ == '__main__':
    create_prefectures.create_json_file()
    create_total.create_json_file()
    create_statistics_positives.create_json_file()
