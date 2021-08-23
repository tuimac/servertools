FROM alpine:latest

WORKDIR /root

expose 80
expose 8000

ADD requirements.txt /root/requirements.txt
ADD nginx.conf /etc/nginx/nginx.conf
ADD entrypoint.sh /root/entrypoint.sh

RUN apk update && \
    apk upgrade && \
    apk add --no-cache bash git python3 python3-dev py3-pip nodejs npm nginx cargo rust gcc openssl-dev build-base libffi-dev redis && \
    pip3 install -r requirements.txt && \
    git clone https://github.com/tuimac/servertools && \
    cd /root/servertools/src/frontend && \
    npm install bootstrap react-bootstrap react-router-dom && \
    npm run-script build && \
    mkdir /upload

ENTRYPOINT ["/root/entrypoint.sh"]
