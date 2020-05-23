import textwrap
import os

# Output json path
PREFECTURES_JSON_PATH = './data/created_json/prefectures.json'
TODAY_TOTAL_JSON_PATH = './data/created_json/today_total.json'
HISTORY_TOTAL_JSON_PATH = './data/created_json/history_total.json'
PREDICTION_TOTAL_JSON_PATH = './data/created_json/prediction_total.json'
POSITIVE_DETAIL_JSON_PATH = './data/created_json/positive_detail.json'
STATISTICS_JSON_PATH = './data/created_json/statistics_positive_detail.json'
POSITIVE_DEITAL_PREFECTURE_JSON_PATH_FORMAT = 'data/created_json/positive_detail_by_prefecture/{0}.json'

# Source data path
SOURCE_DATA_BASE_PATH = 'data/2019-ncov-japan/50_Data/'
POSITIVE_DETAIL_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'positiveDetail.csv')
DOMESTIC_DAILY_REPORT_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'domesticDailyReport.csv')
PREFECTURES_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'prefectures.csv')
CASES_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'byDate.csv')
DEATHS_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'death.csv')
PCR_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'provincePCR.csv')
SUMMARY_DATA_PATH = os.path.join(SOURCE_DATA_BASE_PATH, 'MHLW/summary.csv')

PREFECTURES = textwrap.dedent('''\
北海道,青森県,岩手県,宮城県,秋田県,山形県,福島県,茨城県,栃木県,群馬県,埼玉県,千葉県,東京都,神奈川県,新潟県,富山県,\
石川県,福井県,山梨県,長野県,岐阜県,静岡県,愛知県,三重県,滋賀県,京都府,大阪府,兵庫県,奈良県,和歌山県,鳥取県,島根県,\
岡山県,広島県,山口県,徳島県,香川県,愛媛県,高知県,福岡県,佐賀県,長崎県,熊本県,大分県,宮崎県,鹿児島県,沖縄県\
''').split(',')
