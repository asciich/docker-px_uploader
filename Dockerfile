FROM alpine:3.7

MAINTAINER Reto Hasler <reto.hasler@asciich.ch>

RUN apk upgrade --no-cache && \
    apk update && \
    apk add --no-cache \
        git \
        python3 \
        py3-pip

RUN pip3 install --upgrade pip && \
    pip3 install --upgrade \
        pyserial

RUN cd / && \
    git clone https://github.com/ArduPilot/PX4Firmware.git

RUN cp -v /PX4Firmware/Tools/px_uploader.py /usr/bin/px_uploader && \
    chmod +x+x+x /usr/bin/px_uploader
