import pandas as pd
import json

POSITIVE_DETAIL_DATA_PATH = 'data/2019-ncov-japan/Data/positiveDetail.csv'
OUTPUT_JSON_PATH= 'data/created_json/positive_detail.json'


def create_json_file():
    prefectures = []
    header = ('date', 'prefecture', 'residence_prefecture',
              'age', 'gender', 'attribute', 'prefecture_number',
              'travel_or_contact', 'detail', 'src', 'onset', 'symptom',
              'death_or_discharge_date', 'comment1', 'outcome', 'outcome_src', 'comment2')
    positive_detail_df = pd.read_csv(POSITIVE_DETAIL_DATA_PATH, index_col=0, names=header,  encoding='utf-8')

    with open(OUTPUT_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(positive_detail_df.drop(positive_detail_df.index[0]).to_dict(orient='records'), f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    create_json_file()
