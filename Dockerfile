FROM python:3.6

ENV TigaEnv production

ADD . /code

WORKDIR /code

RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade -q pip 
RUN pip3 install -q --no-python-version-warning --disable-pip-version-check -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

CMD ["waitress-serve", "--threads", "4", "--port", "8080", "--call", "factory:create_app"]

EXPOSE 8080
