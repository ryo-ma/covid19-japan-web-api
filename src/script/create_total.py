import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import json
import datetime
from ..const import (SUMMARY_DATA_PATH, TODAY_TOTAL_JSON_PATH,
                     HISTORY_TOTAL_JSON_PATH, PREDICTION_TOTAL_JSON_PATH)

# Incubation period + Onset period
DAY_RANGE = 28
PREDICTION_DAYS = 30


def create_total_dict(df, date):
    """
    Create a dict. total_dict.

    Args:
        df: (todo): write your description
        date: (todo): write your description
    """
    if len(df.loc[date].shape) > 1:
        summary = df.loc[date].sum().fillna(0)
    else:
        summary = df.loc[date].fillna(0)

    total = {
        'date': int(date),
        'pcr': int(summary['検査人数']),
        'hospitalize': int(summary['入院中']),
        'positive': int(summary['陽性者']),
        'severe': int(summary['重症者']),
        'discharge': int(summary['退院者']),
        'death': int(summary['死亡者']),
        'symptom_confirming': int(summary['確認中']),
    }
    return total


def create_json_file():
    """
    Creates a summary file.

    Args:
    """
    summary_df = pd.read_csv(SUMMARY_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    today = summary_df.index.max()
    output_total(TODAY_TOTAL_JSON_PATH, create_total_dict(summary_df, today))

    history_total_list = []
    for date in summary_df.index.drop_duplicates().values:
        history_total_list.append(create_total_dict(summary_df, date))
    output_total(HISTORY_TOTAL_JSON_PATH, history_total_list)

    positive_param, _ = predict([x['positive'] for x in history_total_list])
    death_param, _ = predict([x['death'] for x in history_total_list])
    predicted_totals = []
    parsed_date = datetime.date(int(str(today)[:4]), int(str(today)[4:6]), int(str(today)[6:8]))
    for i, x in enumerate(range(DAY_RANGE + 1, DAY_RANGE + PREDICTION_DAYS), 1):
        date = parsed_date + datetime.timedelta(days=i)
        positive_prediction = nonlinear_func(x, positive_param[0], positive_param[1])
        death_prediction = nonlinear_func(x, death_param[0], death_param[1])
        predicted_totals.append({
            'date': int(date.strftime("%Y%m%d")),
            'positive': positive_prediction,
            'death': death_prediction,
        })
    output_total(PREDICTION_TOTAL_JSON_PATH, predicted_totals)


def output_total(json_path, data_dict):
    """
    Outputs the_path to file.

    Args:
        json_path: (str): write your description
        data_dict: (dict): write your description
    """
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=2, ensure_ascii=False)


def predict(array_data):
    """
    Predict the best fit.

    Args:
        array_data: (array): write your description
    """
    array_x = range(1, DAY_RANGE + 1)
    array_y = array_data[len(array_data) - DAY_RANGE: len(array_data)]
    return curve_fit(nonlinear_func, array_x, array_y)


def nonlinear_func(x, a, b):
    """
    Nonlinear function.

    Args:
        x: (todo): write your description
        a: (todo): write your description
        b: (todo): write your description
    """
    return b * np.exp(a*x)
