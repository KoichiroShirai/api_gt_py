FROM python:3.9.0-slim
USER root
SHELL ["/bin/bash", "-c"]
WORKDIR /root/dev
COPY requirements.txt /root/dev
RUN apt-get update \
    && apt-get -y install locales \
    && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 \
    && pip install --upgrade pip \
    && pip install --upgrade setuptools \
    && pip install -r requirements.txt
ENV LANG ja_JP.UTF-8 \
    LANGUAGE ja_JP.UTF-8 \
    LC_ALL ja_JP.UTF-8 \
    TZ JST-9 \
    term xterm \
    DEBCONF_NOWARNINGS yes
