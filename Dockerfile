FROM python:3.6

ADD requirements.txt /tmp/requirements.txt
#TODO: Validate this shouldn't be run through setup.py instead
RUN pip install -r /tmp/requirements.txt

ADD . /app

WORKDIR /app

EXPOSE 5000

CMD [ "/usr/local/bin/connexion", "run", "api.yaml", "-v" ]
