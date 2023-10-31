# syntax=docker/dockerfile:1
FROM ubuntu:22.04
# 必要なパッケージのインストールとPythonのセットアップ
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --upgrade pip
WORKDIR /app
# 環境変数を設定してPythonの出力を直接コンソールに出す
ENV PYTHONUNBUFFERED=1
# requirements.txtを/appディレクトリにコピー
# COPY app/requirements.txt /app/
COPY . .
# 依存関係のインストール
RUN pip3 install -r app/requirements.txt
ENV PATH=$PATH:/root/.local/bin
# コンテナ起動時にuvicornを使用してFastAPIアプリケーションを起動
CMD ["uvicorn", "app.server.main:app", "--host", "0.0.0.0", "--port", "3000"]
EXPOSE 3000
