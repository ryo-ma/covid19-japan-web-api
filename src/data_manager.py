import json
from .const import (PREFECTURES_JSON_PATH, PREDICTION_TOTAL_JSON_PATH,
                    HISTORY_TOTAL_JSON_PATH, TODAY_TOTAL_JSON_PATH,
                    STATISTICS_JSON_PATH)


class DataManager:
    def __init__(self):
        with open(PREFECTURES_JSON_PATH) as f:
            self.prefectures_json = f.read()
        with open(HISTORY_TOTAL_JSON_PATH) as f:
            self.history_total_json = f.read()
        with open(TODAY_TOTAL_JSON_PATH) as f:
            self.today_total_json = f.read()
        with open(PREDICTION_TOTAL_JSON_PATH) as f:
            self.prediction_total_json = f.read()
        with open(STATISTICS_JSON_PATH) as f:
            self.statistics_json = f.read()

    def get_positive_detail_json(self, prefecture):
        json_dict = [x for x in json.loads(self.positive_detail_json) if x['prefecture'] == prefecture]
        return json.dumps(json_dict, indent=2, ensure_ascii=False)
