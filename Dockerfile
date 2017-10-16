# gunicorn-flask

FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive
ENV FLASK_CONFIG production

# Setup flask application
RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY requirements.txt /deploy/app

RUN sed -i "s/http:\/\/archive.ubuntu/http:\/\/mirrors.163/g" /etc/apt/sources.list
RUN apt-get update \
        && apt-get install -y python python-dev build-essential libssl-dev libffi-dev python-pip gunicorn \
        && pip install -U pip -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com \
        && pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com cryptography \
        && pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r /deploy/app/requirements.txt

WORKDIR /deploy/app
EXPOSE 5000
# Start gunicorn
CMD ["/usr/bin/gunicorn", "--config", "/deploy/gunicorn_config.py", "run:app"]
