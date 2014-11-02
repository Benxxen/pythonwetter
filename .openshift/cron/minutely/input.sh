#!/bin/sh

if [ `date +%H:%M` == "05:00" ]
then
    python ~/app-root/repo/manage.py shell < ~/app-root/repo/inputdb.py
fi