#!/bin/sh

if [ `date +%H:%M` == "14:13" ]
then
    bash python ~/app-root/repo/manage.py shell < ~/app-root/repo/inputdb.py
fi