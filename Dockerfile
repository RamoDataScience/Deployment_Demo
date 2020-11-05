FROM python:3.8.3

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/ml_api

ARG CODEARTIFACT_AUTH_TOKEN
ENV FLASK_APP run.py

# Install requirements, including from AWS CodeArtifact
ADD ./packages/ml_api /opt/ml_api/
RUN pip install --upgrade pip
RUN pip install -r /opt/ml_api/requirements.txt
RUN pip install awscli
RUN pip config set global.index-url https://aws:$CODEARTIFACT_AUTH_TOKEN@packages-156062350977.d.codeartifact.us-east-1.amazonaws.com/pypi/classification-model-package/simple/
RUN pip install -r /opt/ml_api/requirementsaws.txt
RUN chmod +x /opt/ml_api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 5000

CMD ["bash", "./run.sh"]