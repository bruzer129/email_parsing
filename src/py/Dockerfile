FROM ubuntu:bionic

WORKDIR /root/email_app
COPY req.txt /tmp/
COPY app_email.py .
COPY email.html .

RUN apt-get update &&  apt-get install -y \
    --no-install-recommends \
    vim \
    curl \
    tcpdump \
    python3.7 \
    python3-pip \
    python3-setuptools \
    python3-distutils \
    python3-wheel \
    && mkdir -p /root/email_app \
    && /usr/bin/python3.7 -m pip install --upgrade -r /tmp/req.txt \
    && if [ ! -e /usr/bin/python ]; then ln -s /usr/bin/python3.7 /usr/bin/python; fi \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV FLASK_APP=/root/email_app/app_email.py
ENV PATH $PATH:/usr/local/bin:/root/email_app:.

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
#CMD ["/bin/bash"]
