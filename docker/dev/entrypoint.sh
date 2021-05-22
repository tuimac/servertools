#!/bin/bash

python3 /root/servertools/src/backend/manage.py runserver 0.0.0.0:8000 &

cd /root/servertools/src/frontend
npm start &

/usr/sbin/nginx -g 'daemon off;' -c /etc/nginx/nginx.conf
