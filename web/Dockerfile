# Pythonは公式イメージ
FROM python:3.5.2

# オリジナルはJoshua Conner氏
# MAINTAINER Joshua Conner <joshua.conner@gmail.com>
MAINTAINER Ryosuke Kamei <sr2smail@gmail.com>

# ユーザ作成
RUN groupadd web
RUN useradd -d /home/bottle -m bottle

# bottleを使ったサーバ起動ファイルをコピー
# ADD server.py /home/bottle/server.py

# bottleをインストール
RUN pip install bottle

# ポートはserver.pyと合わせて8080にし、サーバ起動ファイルを新しく作成した"bottle"ユーザで起動
EXPOSE 8080
ENTRYPOINT ["/usr/local/bin/python", "/code/server.py"]
USER bottle
