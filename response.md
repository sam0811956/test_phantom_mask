# Introduction
使用語言: Python
框架: Django

## 專案流程
* 依照 raw data 撰寫 model.py
* 解析 raw data, 修改 migrations.py
* migrate raw data
* 撰寫 API 在 views.py, 撰寫 ulrs.py
* 撰寫 測試程式
* 佈署到 heroku
* 建立 Docker

## Required
### API Document
  https://sam0811956.docs.apiary.io/#reference/0/api-collection/list-all-pharmacies-that-are-open-at-a-certain-time

### Import Data Commands
  `python makemigrations`
  `python migrate`

## Bonus
### Test Coverage Report
  check report 
![image](https://user-images.githubusercontent.com/32931993/133278739-73d64a96-29f0-428e-ba6d-cf6b927cc798.png)

### Dockerized
  check my dockerfile !
https://github.com/sam0811956/test_phantom_mask/blob/main/Dockerfile
### Demo Site Url
  demo site is ready on https://phantom-mask-api.herokuapp.com/
