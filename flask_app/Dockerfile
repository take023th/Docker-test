# ubuntuのインストール
#FROM ubuntu:bionic

#RUN apt update -y && apt install -y python3-pip python-dev

# Flaskのインストール
#COPY ./requirements.txt requirements.txt 

#RUN pip3 install -r requirements.txt 

#COPY . .

# 実行するファイル
#ENTRYPOINT ["python3"]

# ENTRYPOINTに対する引数
#CMD ["app.py"]

# ubuntuのインストール
FROM ubuntu:bionic

RUN apt update -y && apt install -y python3-pip python-dev

# 作業ディレクトリの指定
WORKDIR /app

# Flaskのインストール
COPY ./requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# アプリケーションのコピー
COPY . .

# ポートの公開
# EXPOSE 5000

# ENTRYPOINTに対する引数
ENTRYPOINT ["python3", "app.py"] 
# "--host=0.0.0.0", "--port=5000"]

