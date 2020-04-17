import pandas as pd
import json

POSITIVE_DETAIL_DATA_PATH = 'data/2019-ncov-japan/50_Data/positiveDetail.csv'
PREFECTURE_DATA_PATH = 'data/created_json/prefectures.json'
OUTPUT_JSON_PATH = 'data/created_json/statistics_positive_detail.json'

GENERATIONS = ('00代', '10代', '20代', '30代', '40代', '50代', '60代', '70代', '80代', '90代', '100代', '不明')


def create_json_file():
    positive_detail_df = pd.read_csv(POSITIVE_DETAIL_DATA_PATH, encoding='utf-8')
    analytics = []
    with open(PREFECTURE_DATA_PATH, 'r', encoding='utf-8') as f:
        prefectures = json.load(f)
    for prefecture in prefectures:
        name = prefecture['name_ja']
        filtered_positive_df_by_prefecture = positive_detail_df.query(f'都道府県.str.startswith("{name}")',
                                                                      engine='python')
        filtered_positve_df_by_male = filtered_positive_df_by_prefecture.query('性別=="男性"')
        filtered_positve_df_by_female = filtered_positive_df_by_prefecture.query('性別=="女性"')
        filtered_positve_df_by_unknown_gender = filtered_positive_df_by_prefecture.query('性別!="男性"')\
            .query('性別!="女性"')
        male_count = len(filtered_positve_df_by_male)
        female_count = len(filtered_positve_df_by_female)
        unkonw_gender_count = len(filtered_positve_df_by_unknown_gender)

        prefecture = {
            'name_ja': name,
            'name_en': prefecture['name_en'],
            'total_count': len(filtered_positive_df_by_prefecture),
            'male': {
                'count': male_count,
                'generations_count': get_generations_count(filtered_positve_df_by_male),
            },
            'female': {
                'count': female_count,
                'generations_count': get_generations_count(filtered_positve_df_by_female),
            },
            'unkown_gender': {
                'count': unkonw_gender_count,
                'generations_count': get_generations_count(filtered_positve_df_by_unknown_gender),
            }
        }
        analytics.append(prefecture)

    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(analytics,
                  f,
                  indent=2,
                  ensure_ascii=False)


def get_generations_count(df):
    generations_count = {}
    for generation_str in GENERATIONS:
        label = generation_str.replace('代', 's').replace('不明', 'unknown')
        generations_count[label] = len(df.query(f'年齢=="{generation_str}"'))
    return generations_count


if __name__ == '__main__':
    create_json_file()
