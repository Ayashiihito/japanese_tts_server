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
        software-properties-common \
        sox \
        subversion \
        unzip \
        wget \
        zip \
        zlib1g-dev \
        python2.7 \
        python3.7 \
        python3-pip \
        python3-setuptools \
        python3-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3.7 -m pip install -U pip setuptools wheel

COPY ./requirements.txt ./requirements.txt

RUN  python3.7 -m pip install -r ./requirements.txt

COPY . .

CMD flask run
