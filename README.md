![logo](https://user-images.githubusercontent.com/6661165/78037051-fc6cac80-73a5-11ea-91fe-10509d2b03ed.png)

# COVID-19 Japan Web API
![UpdateData](https://github.com/ryo-ma/covid19-japan-web-api/workflows/UpdateData/badge.svg)

🦠 Web API to get COVID-19(coronavirus) information of each prefecture in Japan

# Features

* 🔁 Update data every 2 hours
* 🚀 Provide REST API
* 🇯🇵 Get info of each prefecture in Japan

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
  "symtomConfirming": 133,
  "hospitalize": 1187,
  "mild": 659,
  "severe": 59,
  "confirming": 323,
  "waiting": 13,
  "discharge": 408,
  "death": 52
}
```
