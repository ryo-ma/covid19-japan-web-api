import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import json
import datetime


DOMESTIC_DAILY_REPORT = 'data/2019-ncov-japan/50_Data/domesticDailyReport.csv'
TODAY_OUTPUT_JSON_PATH = 'data/created_json/today_total.json'
HISTORY_OUTPUT_JSON_PATH = 'data/created_json/history_total.json'
PREDICTION_OUTPUT_JSON_PATH = 'data/created_json/prediction_total.json'
# Incubation period + Onset period
DAY_RANGE = 28
PREDICTION_DAYS = 30


def create_json_file():
    total_df = pd.read_csv(DOMESTIC_DAILY_REPORT, na_values='0', encoding='utf-8')
    today_total = total_df.iloc[-1].fillna(0).astype(int).to_dict()
    history_total_df = total_df.fillna(0).astype(int)

    positive_param, _ = predict(history_total_df['positive'].array)
    death_param, _ = predict(history_total_df['death'].array)
    predicted_totals = []
    latest_date = str(history_total_df['date'].max())
    parsed_date = datetime.date(int(latest_date[:4]), int(latest_date[4:6]), int(latest_date[6:8]))
    for i, x in enumerate(range(DAY_RANGE + 1, DAY_RANGE + PREDICTION_DAYS), 1):
        date = parsed_date + datetime.timedelta(days=i)
        positive_prediction = nonlinear_func(x, positive_param[0], positive_param[1])
        death_prediction = nonlinear_func(x, death_param[0], death_param[1])
        predicted_totals.append({
            'date': int(date.strftime("%Y%m%d")),
            'positive': positive_prediction,
            'death': death_prediction,
        })

    output_total(TODAY_OUTPUT_JSON_PATH, today_total)
    output_total(HISTORY_OUTPUT_JSON_PATH, history_total_df.to_dict(orient='records'))
    output_total(PREDICTION_OUTPUT_JSON_PATH, predicted_totals)


def output_total(json_path, data_dict):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=2, ensure_ascii=False)


def predict(array_data):
    array_x = range(1, DAY_RANGE + 1)
    array_y = array_data[len(array_data) - DAY_RANGE: len(array_data)]
    return curve_fit(nonlinear_func, array_x, array_y)


def nonlinear_func(x, a, b):
    return b * np.exp(a*x)


if __name__ == '__main__':
    create_json_file()
