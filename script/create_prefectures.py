import pandas as pd
import json

CASES_DATA_PATH = 'data/2019-ncov-japan/Data/byDate.csv'
DEATHS_DATA_PATH = 'data/2019-ncov-japan/Data/death.csv'
OUTPUT_JSON_PATH= 'data/created_json/prefectures.json'


def create_json_file():
    prefectures = []
    cases_df = pd.read_csv(CASES_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    deaths_df = pd.read_csv(DEATHS_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    cases_df_sum = cases_df.sum().astype('int32')
    deaths_df_sum = deaths_df.sum().astype('int32')
    for prefecture in cases_df.columns:
        prefectures.append({'name': prefecture,
                            'cases': int(cases_df_sum[prefecture]),
                            'deaths': int(deaths_df_sum[prefecture])})

    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(prefectures, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_json_file()
