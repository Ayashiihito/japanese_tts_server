FROM ubuntu:18.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive \
    apt-get -y install --no-install-recommends \ 
        automake \
        autoconf \
        apt-utils \
        bc \
        build-essential \
        ca-certificates \
        cmake \
        curl \
        flac \
        ffmpeg \
        gawk \
        gfortran \
        git \
        libboost-all-dev \
        libtool \
        libbz2-dev \
        liblzma-dev \
        libsndfile1-dev \
        patch \
        python3 \
        software-properties-common \
        sox \
        subversion \
        unzip \
        wget \
        zip \
        zlib1g-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV DEBIAN_FRONTEND=noninteractive 

RUN add-apt-repository universe
RUN apt-get update -y

RUN apt-get -y install python-pip
RUN curl https://bootstrap.pypa.io/pip/3.6/get-pip.py | python3

RUN apt-get -y install locales locales-all

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

COPY ./requirements.txt ./requirements.txt
RUN  pip install -r ./requirements.txt
RUN pip install pyopenjtalk

COPY . .

CMD flask run --host=0.0.0.0
