import pandas as pd
import json

DOMESTIC_DAILY_REPORT = 'data/2019-ncov-japan/Data/domesticDailyReport.csv'
OUTPUT_JSON_PATH= 'data/created_json/today_total.json'


def create_json_file():
    today_total_df = pd.read_csv(DOMESTIC_DAILY_REPORT, na_values='0', encoding='utf-8')
    today_total = today_total_df.iloc[-1].fillna(0).astype(int).to_dict()

    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(today_total, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_json_file()
