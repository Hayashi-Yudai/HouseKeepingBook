# House Keeping Book

## Requirement

- Python 3.7.2
- Django 2.1.2

## Features

シンプルデザインの家計簿アプリ

## Usage

最初にデータベースを作成します。コマンドラインから次のコードを実行します。

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

アプリケーションを動作させるには、

```bash
$ python manage.py runserver
```

を実行して、http://127.0.0.1:8000/ にアクセスします。
