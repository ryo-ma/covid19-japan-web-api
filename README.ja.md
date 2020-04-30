![logo](https://github.com/ryo-ma/covid19-japan-web-api/blob/master/.github/logo_img.png)

# COVID-19 Japan Web API
![UpdateData](https://github.com/ryo-ma/covid19-japan-web-api/workflows/UpdateData/badge.svg)
[![LICENSE](https://img.shields.io/github/license/ryo-ma/covid19-japan-web-api?color=blue)](./LICENSE)
[![Tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fryo-ma%2Fcovid19-japan-web-api)](https://twitter.com/intent/tweet?text=日本のコロナウイルス(COVID-19)情報を取得できるWebAPI&url=https%3A%2F%2Fgithub.com%2Fryo-ma%2Fcovid19-japan-web-api)

**言語**

[英語🇺🇸](./README.md) | 日本語🇯🇵



<!-- 🦠 Web API to get COVID-19(coronavirus) information of each prefecture in Japan -->
🦠 日本の都道府県ごとのCOVID-19（コロナウイルス）情報を取得するためのWeb API

<!-- I created this API to help disseminate about the Japanese COVID-19 information. I am updating this API from time to time, so if you have an API you want to add, please let me know! -->
このAPIは、COVID-19に関する日本国内情報を広めるためのものです。このAPIは随時更新していますので、追加したいAPIがありましたらお知らせください。


<!-- # Table of Contents -->
# 目次

- [主な機能](#features)
- [このAPIを使用するプロジェクト](#project-using-this-api)
- [使い方](#usage)
- [Contribution Guide](#contribution-guide)
- [データソースについて](#data-sources)
- [ライセンス](#license)

# Features

* 🔁 2時間ごとにデータを更新する
* 🚀 REST APIを提供
* 🇯🇵 日本の各都道府県の情報を取得
* ☕️ シンプルなデータと使いやすさ
* 📈 今後30日間の予測


<!-- # Project using this API -->
# このAPIを使用したプロジェクト

<!-- If your project is not listed here, let us know! -->
もしプロジェクトがここにリストされていない場合は、お知らせください。

* **https://github.com/yakuri/covid19**
* **https://github.com/yuto51942/COVID-19-notice**
* **https://github.com/postmanlabs/covid-19-apis**
* **https://github.com/InumberX/covid-19**
* **https://github.com/miya/covid19-jp-linebot**

<!-- # Usage -->
#  使い方

<!-- You can see the documentation of this API and/or import it as a Postman collection [using this link](https://documenter.getpostman.com/view/9215231/SzYaWe6h?version=latest). -->

このAPIのドキュメントを表示したり、[こちらのリンク](https://documenter.getpostman.com/view/9215231/SzYaWe6h?version=latest) からPostmanコレクションとしてインポートしたりできます。

* [Prefectures](#prefectures)
* [Total](#total)
* [Total History](#total-history)
* [Total Prediction](#total-prediction)
* [Positives](#positives)
* [Positives Statistics](#positives-statistics)

---

<!-- ## Prefectures -->
## 都道府県ごとのデータ(Prefectures)

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/prefectures](https://covid19-japan-web-api.now.sh/api/v1/prefectures)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    "id": 1,
    "name_ja": "北海道",
    "name_en": "Hokkaido",
    "lat": 43.46722222,
    "lng": 142.8277778,
    "last_updated": {
      "cases_date": 20200422,
      "deaths_date": 20200422,
      "pcr_date": 2020420
    },
    "cases": 468,
    "deaths": 23,
    "pcr": 4399
  },
  {
    "id": 2,
    "name_ja": "青森",
    "name_en": "Aomori",
    "lat": 40.78027778,
    "lng": 140.83194440000003,
    "last_updated": {
      "cases_date": 20200422,
      "deaths_date": 20200422,
      "pcr_date": 2020420
    },
    "cases": 22,
    "deaths": 0,
    "pcr": 521
  },
...
```

</details>

---

<!-- ## Total -->
## 全国の合計(Total)

<!-- This API includes FLIGHT data and SHIPMENT data. -->
このAPIには、FLIGHTデータとSHIPMENTデータを含んでいます。

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/total](https://covid19-japan-web-api.now.sh/api/v1/total)

<details>
<summary><b>Response</b></summary>

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

</details>

---

<!-- ## Total History -->
## 全国の合計の履歴(Total History)

<!-- This API includes FLIGHT data and SHIPMENT data. -->
このAPIには、FLIGHTデータとSHIPMENTデータを含んでいます。

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/total?history=true](https://covid19-japan-web-api.now.sh/api/v1/total?history=true)

<details>
<summary><b>Response</b></summary>

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

</details>

---

<!-- ## Total Prediction -->
## 今後の予測(Total Prediction)

Predict  for the next 30 days about the positive total and the death total.
機械学習に基づき、感染者および死亡者について次の30日間を予測します。

<!-- This API includes the FLIGHT data and the SHIPMENT data. -->
このAPIには、FLIGHTデータとSHIPMENTデータを含んでいます。

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/total?predict=true](https://covid19-japan-web-api.now.sh/api/v1/total?predict=true)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    "date": 20200413,
    "positive": 6960.103502394343,
    "death": 102.8839324261669
  },
  {
    "date": 20200414,
    "positive": 7652.287257933034,
    "death": 107.84568822992809
  },
  {
    "date": 20200415,
    "positive": 8413.308833378682,
    "death": 113.04673329952118
  },
  {
    "date": 20200416,
    "positive": 9250.01416438296,
    "death": 118.49860777416443
  },
  {
    "date": 20200417,
    "positive": 10169.930016336322,
    "death": 124.21340833627379
  },
  {
    "date": 20200418,
    "positive": 11181.33169302858,
    "death": 130.2038150517223
  },
  {
    "date": 20200419,
    "positive": 12293.317478949984,
    "death": 136.4831195045177
  },
  {
    "date": 20200420,
    "positive": 13515.89048489476,
    "death": 143.06525428832322
  },
...
```

</details>

---

<!-- ## Positives -->
## 感染者データ(Positives)

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/positives?prefecture=東京都](https://covid19-japan-web-api.now.sh/api/v1/positives?prefecture=東京都)

<!-- **Query parameter** -->
**クエリパラメーター**

<!-- * **required**: prefecture=(jp_name) : Filter by prefecture using jp_name -->
* **必須パラメーター**：citizen =(jp_name): jp_nameを使用して都道府県でフィルター

<details>
<summary><b>Response</b></summary>

```json
[
  {
    "code": "",
    "announcement_date": "2020-01-24",
    "src": "https://www.metro.tokyo.lg.jp/tosei/hodohappyo/press/2020/01/24/20.html",
    "prefecture": "東京都",
    "residence_prefecture": "国外（武漢市）",
    "age": "40代",
    "gender": "男性",
    "attribute": "",
    "prefecture_number": "東京都1",
    "travel_or_contact": "渡航歴",
    "detail": "中国（武漢）",
    "id": "ID130001",
    "diagnosis_date": "",
    "onset": "2020/01/14",
    "symptom": "1",
    "death_or_discharge_date": "",
    "comment": "",
    "outcome": "1",
    "outcome_src": "https://i.imgur.com/P185t7C.jpg"
  },
  {
    "code": "",
    "announcement_date": "2020-01-25",
    "src": "https://www.metro.tokyo.lg.jp/tosei/hodohappyo/press/2020/01/27/24.html",
    "prefecture": "東京都",
    "residence_prefecture": "国外（武漢市）",
    "age": "30代",
    "gender": "女性",
    "attribute": "",
    "prefecture_number": "東京都2",
    "travel_or_contact": "渡航歴",
    "detail": "中国（武漢）",
    "id": "ID130002",
    "diagnosis_date": "",
    "onset": "2020/01/21",
    "symptom": "1",
    "death_or_discharge_date": "",
    "comment": "",
    "outcome": "1",
    "outcome_src": "https://i.imgur.com/P185t7C.jpg"
  },
...
```

</details>

---

<!-- ## Positives Statistics -->
## 感染者の統計データ
<!-- This is a statistic of the **positives API** and does not include data that is not publicly available. -->
これは**Positives API**の統計であり、公開されていないデータは含まれません。

**Endpoint**: [https://covid19-japan-web-api.now.sh/api/v1/statistics](https://covid19-japan-web-api.now.sh/api/v1/statistics)

<details>
<summary><b>Response</b></summary>

```json
[
  {
    "name_ja": "北海道",
    "name_en": "Hokkaido",
    "total_count": 239,
    "male": {
      "count": 137,
      "generations_count": {
        "00s": 6,
        "10s": 1,
        "20s": 5,
        "30s": 8,
        "40s": 19,
        "50s": 35,
        "60s": 27,
        "70s": 19,
        "80s": 14,
        "90s": 2,
        "100s": 0,
        "unknown": 1
      }
    },
    "female": {
      "count": 100,
      "generations_count": {
        "00s": 1,
        "10s": 1,
        "20s": 14,
        "30s": 10,
        "40s": 12,
        "50s": 17,
        "60s": 15,
        "70s": 16,
        "80s": 8,
        "90s": 4,
        "100s": 0,
        "unknown": 2
      }
    },
    "unkown_gender": {
      "count": 2,
      "generations_count": {
        "00s": 0,
        "10s": 0,
        "20s": 0,
        "30s": 0,
        "40s": 0,
        "50s": 0,
        "60s": 0,
        "70s": 0,
        "80s": 0,
        "90s": 0,
        "100s": 0,
        "unknown": 2
      }
    }
  },
...
```

</details>

---

# Contribution Guide
<!-- * Please use **flake8** as Lint -->
* Lintとして**flake8**を使用してください
<!-- * Please don't add **/data** directory to your commit -->
* **/data**ディレクトリをコミットに追加しないでください
<!-- * Please PullRequest to master because gitflow is not currently used -->
* gitflowは現在使用されていないため、masterにPullRequestしてください

## Contributers
<a href="https://github.com/ryo-ma/covid19-japan-web-api/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=ryo-ma/covid19-japan-web-api" />
</a>

Made with [contributors-img](https://contributors-img.web.app).

# データソースについて
<!-- This data was collected by volunteers and may be incorrect. Please refer to the reports of public organizations correctly. -->
このデータはボランティアによって収集されたものであり、正確でない可能性があります。正しいデータを得るには公的機関からのレポートを参照してください。

* [swsoyee/2019-ncov-japan](https://github.com/swsoyee/2019-ncov-japan)

# LICENSE
[MIT LICENSE](./LICENSE)
