#!/usr/bin/env bash

docker build -t pymsx_demo_script:latest .
docker run --name=pymsx_demo_script pymsx_demo_script:latest