import pandas as pd
import json

DOMESTIC_DAILY_REPORT = 'data/2019-ncov-japan/Data/domesticDailyReport.csv'
TODAY_OUTPUT_JSON_PATH = 'data/created_json/today_total.json'
HISTORY_OUTPUT_JSON_PATH = 'data/created_json/history_total.json'


def create_json_file():
    total_df = pd.read_csv(DOMESTIC_DAILY_REPORT, na_values='0', encoding='utf-8')
    today_total = total_df.iloc[-1].fillna(0).astype(int).to_dict()
    history_total = total_df.fillna(0).astype(int).to_dict(orient='records')
    output_total(TODAY_OUTPUT_JSON_PATH, today_total)
    output_total(HISTORY_OUTPUT_JSON_PATH, history_total)


def output_total(json_path, data_dict):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_json_file()
