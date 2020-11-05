import pandas as pd
import json
from ..const import (PREFECTURES_JSON_PATH, SUMMARY_DATA_PATH, PREFECTURES_DATA_PATH)


def get_pcr_df_by_prefecture(prefecture, df):
    """
    Get pcr pre - pcr pre - pcr.

    Args:
        prefecture: (str): write your description
        df: (todo): write your description
    """
    for i in range(1, len(df.filter(like=prefecture, axis=0))):
        prefecture_pcr_df = df.filter(like=prefecture, axis=0)[-i:][:1]
        if not prefecture_pcr_df['検査数'].isna().bool():
            return prefecture_pcr_df


def create_json_file():
    """
    Create a summary file.

    Args:
    """
    prefectures = []
    prefectures_df = pd.read_csv(PREFECTURES_DATA_PATH, index_col=1, na_values='0', encoding='utf-8')
    prefectures_df['name-en'] = prefectures_df['name-en'].replace(' Prefecture', '', regex=True)
    summary_df = pd.read_csv(SUMMARY_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    today = summary_df.index.max()
    for prefecture in prefectures_df.index:
        last_updated = {
            'cases_date': int(today),
            'deaths_date': int(today),
            'pcr_date': int(today),
            'hospitalize_date': int(today),
            'severe_date': int(today),
            'discharge_date': int(today),
            'symptom_confirming_date': int(today),
        }
        summary = summary_df.loc[today].fillna(0).query(f'都道府県名=="{prefecture}"')
        prefecture_df = prefectures_df.loc[prefecture]
        prefectures.append({'id': int(prefecture_df['id']),
                            'name_ja': prefecture,
                            'name_en': prefecture_df['name-en'],
                            'lat': float(prefecture_df['lat']),
                            'lng': float(prefecture_df['lng']),
                            'population': int(prefecture_df['pop']),
                            'last_updated': last_updated,
                            'cases': int(summary['陽性者']),
                            'deaths': int(summary['死亡者']),
                            'pcr': int(summary['検査人数']),
                            'hospitalize': int(summary['入院中']),
                            'severe': int(summary['重症者']),
                            'discharge': int(summary['退院者']),
                            'symptom_confirming': int(summary['確認中']),
                            })

    with open(PREFECTURES_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(prefectures, f, indent=2, ensure_ascii=False)
