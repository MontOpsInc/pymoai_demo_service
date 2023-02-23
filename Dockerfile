FROM        python:3.9-slim-buster
ENV         PYTHONUNBUFFERED=1
ENV         PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

WORKDIR     /app

RUN         DEBIAN_FRONTEND=noninteractive apt-get update -y && \
            apt-get install -y gcc pkg-config libssl-dev
RUN         DEBIAN_FRONTEND=noninteractive \
            apt-get install -y \
            bmon dumb-init nano iotop \
            curl libpam-systemd python3-dev \
            snmpd sudo rsync \
            tcpdump lsb-release \
            apt-transport-https ca-certificates \
            software-properties-common libpython3-dev && \
            apt-get autoremove -y && apt-get clean && \
            rm -rf /usr/local/src/*

COPY        requirements.txt requirements.txt
RUN         pip install --upgrade pip && pip install -r requirements.txt

COPY        . .

EXPOSE      5000

ENTRYPOINT  ["dumb-init", "--"]
CMD         ["python", "/app/run_service/run_service.py"]