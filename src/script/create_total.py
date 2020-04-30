import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import json
import datetime
from ..const import (DOMESTIC_DAILY_REPORT_DATA_PATH, TODAY_TOTAL_JSON_PATH, DEATHS_DATA_PATH,
                     HISTORY_TOTAL_JSON_PATH, PREDICTION_TOTAL_JSON_PATH)

# Incubation period + Onset period
DAY_RANGE = 28
PREDICTION_DAYS = 30


def create_json_file():
    total_df = pd.read_csv(DOMESTIC_DAILY_REPORT_DATA_PATH, na_values='0', encoding='utf-8')
    death_df = pd.read_csv(DEATHS_DATA_PATH, index_col=0, na_values='0', encoding='utf-8')
    today_total = total_df.iloc[-1].fillna(0).astype(int).to_dict()
    history_total_df = total_df.fillna(0).astype(int)

    # Replace the death to a death.csv data
    today_death_total = death_df.fillna(0).sum(numeric_only=True).sum().astype(int)
    today_total['death'] = int(today_death_total)
    for i, row in history_total_df.iterrows():
        date = row['date']
        death_count = death_df.fillna(0).sum(axis=1)[0:death_df.index.get_loc(date)].sum().astype(int)
        history_total_df.loc[i, 'death'] = death_count

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

    output_total(TODAY_TOTAL_JSON_PATH, today_total)
    output_total(HISTORY_TOTAL_JSON_PATH, history_total_df.to_dict(orient='records'))
    output_total(PREDICTION_TOTAL_JSON_PATH, predicted_totals)


def output_total(json_path, data_dict):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data_dict, f, indent=2, ensure_ascii=False)


def predict(array_data):
    array_x = range(1, DAY_RANGE + 1)
    array_y = array_data[len(array_data) - DAY_RANGE: len(array_data)]
    return curve_fit(nonlinear_func, array_x, array_y)


def nonlinear_func(x, a, b):
    return b * np.exp(a*x)
