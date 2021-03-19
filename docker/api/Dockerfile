FROM  python:3.10-rc-alpine3.13
WORKDIR /ep7-app
# gcc ,openssl をインストールしなければ、python のセットアップ時にエラーを起こしてしまう。
RUN apk add build-base libffi-dev
COPY ./requirement.txt .
RUN pip install --upgrade setuptools && pip install -r requirement.txt
CMD ["uvicorn", "run:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]