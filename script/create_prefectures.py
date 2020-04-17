import pandas as pd
import json

PREFECTURES_DATA_PATH = 'data/2019-ncov-japan/50_Data/prefectures.csv'
CASES_DATA_PATH = 'data/2019-ncov-japan/50_Data/byDate.csv'
DEATHS_DATA_PATH = 'data/2019-ncov-japan/50_Data/death.csv'
OUTPUT_JSON_PATH = 'data/created_json/prefectures.json'


def create_json_file():
    prefectures = []
    prefectures_df = pd.read_csv(PREFECTURES_DATA_PATH, index_col=1, na_values='0', encoding='utf-8')
    prefectures_df['name-en'] = prefectures_df['name-en'].replace(' Prefecture', '', regex=True)
    cases_df = pd.read_csv(CASES_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    deaths_df = pd.read_csv(DEATHS_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    cases_df_sum = cases_df.sum().astype('int32')
    deaths_df_sum = deaths_df.sum().astype('int32')
    for prefecture in cases_df.columns:
        if prefecture in prefectures_df.index:
            prefecture_df = prefectures_df.loc[prefecture]
            prefectures.append({'id': int(prefecture_df['id']),
                                'name_ja': prefecture,
                                'name_en': prefecture_df['name-en'],
                                'lat': float(prefecture_df['lat']),
                                'lng': float(prefecture_df['lng']),
                                'cases': int(cases_df_sum[prefecture]),
                                'deaths': int(deaths_df_sum[prefecture])})

    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(prefectures, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_json_file()
