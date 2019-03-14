FROM ubuntu:18.04

ENV host:logger:consoleLoggingMode=always

RUN apt-get update && apt-get install -y python-dev 
RUN pip install --upgrade pip && \
    pip install --upgrade virtualenv && \
    pip install --upgrade setuptools
RUN pip install git+https://github.com/Supervisor/supervisor

ADD requirements.txt /

RUN pip install -r requirements.txt

ADD ./app.py /funcroot

RUN virtualenv --system-site-packages /env

RUN mkdir -p /var/log/supervisor
ADD ./supervisord.conf /etc/supervisord.conf

COPY start.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/start.sh

EXPOSE 8080

CMD ["supervisord"]
