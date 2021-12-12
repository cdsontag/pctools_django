# pctools_django
This repo is a demo of PCTOOLS using Django

## Goals
- emulate:  https://www.stsci.edu/public/propinfo.html  and  https://www.stsci.edu/cgi-bin/get-proposal-info?id=525&observatory=HST (&pi=1)
- not yet shooting for:  https://www.stsci.edu/hst/observing/program-information
- need to handle (and/or edit):  https://www.stsci.edu/modules/stsci-www-components/javascript/pinfo.js

## To Do
- “Find PI” vs Find PI and CoI” buttons
- put propinfo code into grit
- wrap propinfo pages within js wrapper (&pi=1)
- connect propinfo app to real DB
- discuss where/when to “hand off” project

## To reproduce on dlmarvin
```
cd /data1
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh  # next time get the py3.8 specific ver

export install_tp_dir=/data1/miniconda3
sh Miniconda3-latest-Linux-x86_64.sh -b -p $install_tp_dir
source /data1/miniconda3/bin/activate
conda install python=3.8
conda create --name webapp_env python=3.8.8

source /data1/miniconda3/bin/activate webapp_env  # with each session

conda install django=3.2    #  currently gives 3.2.5 but latest is 3.2.8

# Start by going through the https://docs.djangoproject.com/en/3.2/intro/tutorial01/
# NOTE: in django, a "project" can contain multiple "apps"
# the project I called “pctools”
# the app I called:  “propinfo”  (loosely based on their “polls” app; everywhere you see “polls”, I use “propinfo”)

cd /data1
django-admin startproject pctools
mv pctools pctools-demo-top
cd /data1/pctools-demo-top
python manage.py startapp propinfo
# add some models
# make and then run the migrations
# add some page templates (the basic HTML stuff)
# change forms from using GET to use POST (unlocks better security features in Django and may even be more secure)

#
source /data1/miniconda3/bin/activate webapp_env
cd /data1/pctools-demo-top
python manage.py runserver 0:8000
```
