Provisioning a new site
=======================

## Required packages:
* nginx
* python 3
* git
* pip
* virtualenv

sudo apt-get install nginx git python3 python3-pip
sudo pip3 install virtualenv

## nginx virtual host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:

Assume we have a user account at /home/username

/home/username
	˪sites
		˪Sitename
			˫database
			˫source
			˫static
			˪virtual env
