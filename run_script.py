from project.src.script import create_prefectures
from project.src.script import create_total
from project.src.script import create_statistics_positives


if __name__ == '__main__':
    create_prefectures.create_json_file()
    create_total.create_json_file()
    create_statistics_positives.create_json_file()
