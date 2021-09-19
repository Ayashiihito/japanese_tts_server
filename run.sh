#!/bin/bash

docker stop tts || true
docker rm tts || true

docker build . --tag tts:latest
docker run \
  --name tts \
  -dit \
  -p 5000:5000 \
  -v ${pwd}/models:/models \
  tts
