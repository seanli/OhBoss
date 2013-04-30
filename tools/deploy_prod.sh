#!/bin/bash

git push git@heroku.com:ohboss.git
heroku run python manage.py migrate --app ohboss
heroku run python manage.py collectstatic --noinput --app ohboss
