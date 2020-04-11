![logo](https://user-images.githubusercontent.com/6661165/78037051-fc6cac80-73a5-11ea-91fe-10509d2b03ed.png)

# COVID-19 Japan Web API
![UpdateData](https://github.com/ryo-ma/covid19-japan-web-api/workflows/UpdateData/badge.svg)

🦠 Web API to get COVID-19(coronavirus) information of each prefecture in Japan

I created this API to help disseminate information about the Japanese COVID-19. I am updating this API from time to time, so if you have an API you want to add, please let me know!


## Table of Contents

- [Features](#features)
- [Project using this API](#project-using-this-api)
- [Usage](#usage)
- [Contribution Guide](#contribution-guide)
- [Data Sources](#data-sources)

# Features

* 🔁 Update data every 2 hours
* 🚀 Provide REST API
* 🇯🇵 Get info of each prefecture in Japan
* ☕️ Simple to use


# Project using this API

if your project is not listed here, let us know!

* **https://github.com/yakuri/covid19**
* **https://github.com/yuto51942/COVID-19-notice**
* **https://github.com/postmanlabs/covid-19-apis**
* **https://github.com/InumberX/covid-19**
* **https://github.com/miya/covid19-jp-linebot**

# Usage

You can see the documentation of this API and/or import it as a Postman collection [using this link](https://documenter.getpostman.com/view/9215231/SzYaWe6h?version=latest).

* [Prefectures](#prefectures)
* [Total](#total)
* [Total History](#total-history)
* [Positives](#positives)


## Prefectures

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/prefectures](https://covid19-japan-web-api.now.sh/api/v1/prefectures)
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

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/total](https://covid19-japan-web-api.now.sh/api/v1/total)
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

## Total History

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/total?history=true](https://covid19-japan-web-api.now.sh/api/v1/total?history=true)
```bash
$ curl https://covid19-japan-web-api.now.sh/api/v1/total?history=true
```

**Response:**
```json
[
  {
    "date": 20200206,
    "pcr": 132,
    "positive": 16,
    "symptom": 16,
    "symptomless": 0,
    "symptomConfirming": 0,
    "hospitalize": 9,
    "mild": 0,
    "severe": 0,
    "confirming": 3,
    "waiting": 0,
    "discharge": 4,
    "death": 0
  },
  {
    "date": 20200207,
    "pcr": 151,
    "positive": 16,
    "symptom": 16,
    "symptomless": 0,
    "symptomConfirming": 0,
    "hospitalize": 12,
    "mild": 0,
    "severe": 0,
    "confirming": 0,
    "waiting": 0,
    "discharge": 4,
    "death": 0
  },
...
```

## Positives

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/positives](https://covid19-japan-web-api.now.sh/api/v1/positives)
```bash
$ curl https://covid19-japan-web-api.now.sh/api/v1/positives
```

**Response:**
```json
[
  {
    "code": "",
    "announcement_date": "2020/01/28",
    "src": "https://www.mhlw.go.jp/stf/newpage_09158.html",
    "prefecture": "北海道",
    "residence_prefecture": "国外（武漢市）",
    "age": "40代",
    "gender": "女性",
    "attribute": "来日観光客",
    "prefecture_number": "北海道1",
    "travel_or_contact": "渡航歴",
    "detail": "中国（武漢）",
    "id": "ID010001",
    "diagnosis_date": "2020/01/28",
    "onset": "2020/01/26",
    "symptom": "1",
    "death_or_discharge_date": "",
    "comment1": "",
    "outcome": "",
    "outcome_src": "",
    "comment2": "",
    "estimated_infection_date": "2020/01/16"
  },
  {
    "code": "",
    "announcement_date": "2020/02/14",
    "src": "http://www.pref.hokkaido.lg.jp/hf/kth/kak/hasseijoukyou.htm",
    "prefecture": "北海道",
    "residence_prefecture": "札幌市",
    "age": "50代",
    "gender": "男性",
    "attribute": "来日観光客",
    "prefecture_number": "北海道2",
    "travel_or_contact": "",
    "detail": "",
    "id": "ID010002",
    "diagnosis_date": "2020/02/14",
    "onset": "2020/01/31",
    "symptom": "1",
    "death_or_discharge_date": "",
    "comment1": "",
    "outcome": "",
    "outcome_src": "",
    "comment2": "",
    "estimated_infection_date": "2020/01/24"
  },
...
```

# Contribution Guide
* Please use **flake8** as Lint
* Please don't add **/data** directory to your commit
* Please PullRequest to master because gitflow is not currently used

# Data Sources
This data was collected by volunteers and may be incorrect. Please refer to the reports of public organizations correctly.

* [swsoyee/2019-ncov-japan](https://github.com/swsoyee/2019-ncov-japan)

# LICENSE
[MIT LICENSE](./LICENSE)
