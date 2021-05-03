import pandas as pd
import json
import os
from ..const import (PREFECTURES, POSITIVE_DETAIL_JSON_PATH,
                     POSITIVE_DETAIL_DATA_PATH, POSITIVE_DEITAL_PREFECTURE_JSON_PATH_FORMAT)


def create_json_file():
    header = ('code', 'announcement_date', 'src', 'prefecture', 'residence_prefecture',
              'age', 'gender', 'attribute', 'prefecture_number',
              'travel_or_contact', 'detail', 'id', 'diagnosis_date', 'onset', 'symptom',
              'death_or_discharge_date', 'comment', 'outcome', 'outcome_src')
    positive_detail_df = pd.read_csv(POSITIVE_DETAIL_DATA_PATH, names=header,  encoding='utf-8')

    # by prefecture
    groupby_prefecture = positive_detail_df.groupby('prefecture')
    for prefecture in PREFECTURES:
        json_path = os.path.join('project', POSITIVE_DEITAL_PREFECTURE_JSON_PATH_FORMAT.format(prefecture))
        df_by_prefecture = (groupby_prefecture.get_group(prefecture)
                            if prefecture in groupby_prefecture.groups else None)
        output_positive_detail(json_path, df_by_prefecture)

    # all
    output_positive_detail(os.path.join('project', POSITIVE_DETAIL_JSON_PATH), positive_detail_df)


def output_positive_detail(json_path, positive_detail_df):
    with open(json_path, 'w', encoding='utf-8') as f:
        json_data = ([] if positive_detail_df is None
                     else positive_detail_df.drop(positive_detail_df.index[0]).fillna('').to_dict(orient='records'))
        json.dump(json_data, f, indent=2, ensure_ascii=False)
