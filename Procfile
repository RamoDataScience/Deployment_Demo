web: gunicorn --pythonpath packages/ml_api --access-logfile - --error-logfile - run:application

aws codeartifact login --tool pip --domain packages --repository classification-model-package
pip install -r packages/ml_api/requirementsaws.txt