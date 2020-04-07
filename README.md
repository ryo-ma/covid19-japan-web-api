![logo](https://user-images.githubusercontent.com/6661165/78037051-fc6cac80-73a5-11ea-91fe-10509d2b03ed.png)

# COVID-19 Japan Web API
![UpdateData](https://github.com/ryo-ma/covid19-japan-web-api/workflows/UpdateData/badge.svg)

🦠 Web API to get COVID-19(coronavirus) information of each prefecture in Japan

# Features

* 🔁 Update data every 2 hours
* 🚀 Provide REST API
* 🇯🇵 Get info of each prefecture in Japan


# Project using this API

if your project is not listed here, let us know!


# Usage

## Prefectures

**Endpont**: [https://covid19-japan-web-api.now.sh/api/v1/prefectures](https://covid19-japan-web-api.now.sh/api/v1/prefectures)
```bash
$ curl https://covid19-japan-web-api.now.sh/api/v1/prefectures
```

**Response:**
```json
[
  {
    "id": 1,
    "name_ja": "北海道",
    "name_en": "Hokkaido",
    "lat": 43.46722222,
    "lng": 142.8277778,
    "cases": 176,
    "deaths": 7
  },
  {
    "id": 2,
    "name_ja": "青森",
    "name_en": "Aomori",
    "lat": 40.78027778,
    "lng": 140.83194440000003,
    "cases": 8,
    "deaths": 0
  },
...
```

## Total

**Endpont**: [https://covid19-japan-web-api.now.sh/api/v1/total](https://covid19-japan-web-api.now.sh/api/v1/total)
```bash
$ curl https://covid19-japan-web-api.now.sh/api/v1/total
```

**Response:**
```json
{
  "date": 20200329,
  "pcr": 26401,
  "positive": 1647,
  "symptom": 1352,
  "symptomless": 162,
  "symptomConfirming": 133,
  "hospitalize": 1187,
  "mild": 659,
  "severe": 59,
  "confirming": 323,
  "waiting": 13,
  "discharge": 408,
  "death": 52
}
```

## Positives

**Endpont**: [https://covid19-japan-web-api.now.sh/api/v1/positives](https://covid19-japan-web-api.now.sh/api/v1/positives)
```bash
$ curl https://covid19-japan-web-api.now.sh/api/v1/positives
```

**Response:**
```json
[
  {
    "id": "ID01001",
    "announcement_date": "2020/01/28",
    "diagnosis_date": "",
    "prefecture": "北海道",
    "residence_prefecture": "国外（武漢市）",
    "age": "40代",
    "gender": "女性",
    "attribute": "来日観光客",
    "prefecture_number": "北海道1",
    "travel_or_contact": "渡航歴",
    "detail": "中国（武漢）",
    "cluster": "",
    "src": "https://www.mhlw.go.jp/stf/newpage_09158.html",
    "onset": "2020/01/26",
    "symptom": "1",
    "death_or_discharge_date": "",
    "comment1": "",
    "outcome": "",
    "outcome_src": "",
    "comment2": ""
  },
  {
    "id": "ID01002",
    "announcement_date": "2020/02/14",
    "diagnosis_date": "",
    "prefecture": "北海道",
    "residence_prefecture": "札幌市",
    "age": "50代",
    "gender": "男性",
    "attribute": "来日観光客",
    "prefecture_number": "北海道2",
    "travel_or_contact": "",
    "detail": "",
    "cluster": "",
    "src": "http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm",
    "onset": "2020/01/31",
    "symptom": "1",
    "death_or_discharge_date": "",
    "comment1": "",
    "outcome": "",
    "outcome_src": "",
    "comment2": ""
  },
...
```

# Data Sources

* [swsoyee/2019-ncov-japan](https://github.com/swsoyee/2019-ncov-japan)
