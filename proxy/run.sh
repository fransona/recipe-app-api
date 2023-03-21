#!/bin/sh
set -e

# Substituting the ngnix default configurations with the one we created
# the EVN variables will be replaced with the nginx server env variables' values
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

# Will start the ngnix run foreground
nginx -g 'daemon off;'
