# 上手くできなかったのでwebから検索（https://gray-code.com/blog/flask-on-docker/)
# FROM python:alpine

# WORKDIR /app

# COPY . /app

# RUN pip install Flask

# CMD ["python", "index.py"]

# 以下ははじめてのDockerfile(https://qiita.com/suzu12/items/c4bc47c0df6ec9b9290b)

# 最新ubuntuをベースとする
FROM ubuntu:latest

# /var/www/htmlで命令を実行していく
WORKDIR /var/www/html

# echoの内容をsample.txtに格納
RUN echo 'sampleです！' > sample.txt

# ホストのテキストファイルをコンテナにコピー
COPY copy.txt copy.txt

# ubuntuのコマンドを指定（bashだが明示的に記述）
CMD [" /bin/bash"]
