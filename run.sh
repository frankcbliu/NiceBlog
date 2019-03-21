#!/bin/sh
killall -9 uwsgi
uwsgi --ini uwsgi.ini
service nginx reload