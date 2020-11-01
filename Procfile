web: gunicorn --pythonpath packages/ml_api --access-logfile - --error-logfile - run:application

heroku buildpacks:add heroku-community/awscli
heroku config:add ${AWS_ACCESS_KEY_ID}
heroku config:add ${AWS_SECRET_ACCESS_KEY}
heroku config:add ${AWS_DEFAULT_REGION}

aws codeartifact login --tool pip --domain packages --repository classification-model-package
pip install -r packages/ml_api/requirementsaws.txt