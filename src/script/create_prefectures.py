import pandas as pd
import json
from ..const import (PREFECTURES_JSON_PATH, PREFECTURES_DATA_PATH,
                     CASES_DATA_PATH, DEATHS_DATA_PATH, PCR_DATA_PATH)


def get_pcr_df_by_prefecture(prefecture, df):
    for i in range(1, len(df.filter(like=prefecture, axis=0))):
        prefecture_pcr_df = df.filter(like=prefecture, axis=0)[-i:][:1]
        if not prefecture_pcr_df['検査数'].isna().bool():
            return prefecture_pcr_df


def create_json_file():
    prefectures = []
    prefectures_df = pd.read_csv(PREFECTURES_DATA_PATH, index_col=1, na_values='0', encoding='utf-8')
    prefectures_df['name-en'] = prefectures_df['name-en'].replace(' Prefecture', '', regex=True)
    cases_df = pd.read_csv(CASES_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    deaths_df = pd.read_csv(DEATHS_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    pcr_df = pd.read_csv(PCR_DATA_PATH, index_col=0, encoding='utf-8')
    cases_df_sum = cases_df.sum().astype('int32')
    deaths_df_sum = deaths_df.sum().astype('int32')
    last_updated = {
        'cases_date': int(cases_df.index[-1]),
        'deaths_date': int(deaths_df.index[-1]),
    }
    for prefecture in cases_df.columns:
        if prefecture in prefectures_df.index:
            prefecture_pcr_df = get_pcr_df_by_prefecture(prefecture, pcr_df)
            pcr = prefecture_pcr_df['検査数'].astype('int32')
            last_updated['pcr_date'] = int(prefecture_pcr_df['日付'].values[0].replace('/', ''))
            prefecture_df = prefectures_df.loc[prefecture]
            prefectures.append({'id': int(prefecture_df['id']),
                                'name_ja': prefecture,
                                'name_en': prefecture_df['name-en'],
                                'lat': float(prefecture_df['lat']),
                                'lng': float(prefecture_df['lng']),
                                'last_updated': last_updated,
                                'cases': int(cases_df_sum[prefecture]),
                                'deaths': int(deaths_df_sum[prefecture]),
                                'pcr': int(pcr)})

    with open(PREFECTURES_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(prefectures, f, indent=2, ensure_ascii=False)
