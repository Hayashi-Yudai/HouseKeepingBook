# House Keeping Book

## Requirement

- Python 3.7
- Django 3.0.7

## Features

シンプルデザインの家計簿アプリ
![ScreenShot](https://github.com/Hayashi-Yudai/HouseKeepingBook/blob/images/main-view.png)

## Usage

### Dependency

リポジトリに `requirements.txt` と `Pipfile` の両方を置いてあります。Pipenv を使って仮想環境を
構築する場合には、

```bash
$ pipenv install
```

を実行すれば必要なライブラリが入った仮想環境が作成されます。

### Setup

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

## News

- (2020/03/08) Django のバージョンを 3.0.4 にアップグレードしました
- (2020/09/09) Django のバージョンを 3.0.7 にアップグレードしました
