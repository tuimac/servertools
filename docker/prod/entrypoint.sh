#!/bin/bash

cd /root
redis-server &

python3 /root/servertools/src/backend/manage.py runserver 0.0.0.0:8000 &

/usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf
