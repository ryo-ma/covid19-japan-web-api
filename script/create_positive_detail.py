import pandas as pd
import json
import textwrap

POSITIVE_DETAIL_DATA_PATH = 'data/2019-ncov-japan/50_Data/positiveDetail.csv'
OUTPUT_JSON_PATH = 'data/created_json/positive_detail.json'
OUTPUT_JSON_PATH_FORMAT = 'data/created_json/positive_detail_by_prefecture/{0}.json'
PREFECTURES = textwrap.dedent('''\
北海道,青森県,岩手県,宮城県,秋田県,山形県,福島県,茨城県,栃木県,群馬県,埼玉県,千葉県,東京都,神奈川県,新潟県,富山県,\
石川県,福井県,山梨県,長野県,岐阜県,静岡県,愛知県,三重県,滋賀県,京都府,大阪府,兵庫県,奈良県,和歌山県,鳥取県,島根県,\
岡山県,広島県,山口県,徳島県,香川県,愛媛県,高知県,福岡県,佐賀県,長崎県,熊本県,大分県,宮崎県,鹿児島県,沖縄県\
''').split(',')


def create_json_file():
    header = ('code', 'announcement_date', 'src', 'prefecture', 'residence_prefecture',
              'age', 'gender', 'attribute', 'prefecture_number',
              'travel_or_contact', 'detail', 'id', 'diagnosis_date', 'onset', 'symptom',
              'death_or_discharge_date', 'comment', 'outcome', 'outcome_src')
    positive_detail_df = pd.read_csv(POSITIVE_DETAIL_DATA_PATH, names=header,  encoding='utf-8')

    # by prefecture
    groupby_prefecture = positive_detail_df.groupby('prefecture')
    for prefecture in PREFECTURES:
        json_path = OUTPUT_JSON_PATH_FORMAT.format(prefecture)
        df_by_prefecture = (groupby_prefecture.get_group(prefecture)
                            if prefecture in groupby_prefecture.groups else None)
        output_positive_detail(json_path, df_by_prefecture)

    # all
    output_positive_detail(OUTPUT_JSON_PATH, positive_detail_df)


def output_positive_detail(json_path, positive_detail_df):
    with open(json_path, 'w', encoding='utf-8') as f:
        json_data = ([] if positive_detail_df is None
                     else positive_detail_df.drop(positive_detail_df.index[0]).fillna('').to_dict(orient='records'))
        json.dump(json_data, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_json_file()
