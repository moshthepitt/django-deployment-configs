#!/bin/bash

cd /srv/cert/EXAMPLE.COM
. /opt/simp_le/venv/bin/activate
simp_le \
  -d EXAMPLE.COM:/var/www/static/EXAMPLE.COM/documentroot \
  -d www.EXAMPLE.COM:/var/www/static/EXAMPLE.COM/documentroot \
  -f account_key.json -f key.pem -f cert.pem -f fullchain.pem \
  --email kelvin@jayanoris.com \
  && service nginx reload

# set up cron job:
# 43 1 * * * /srv/bin/cert-renew.sh || true
