FROM python:3.9
ADD bert_server.py .
ADD model.tflite .
RUN apt update -y && apt upgrade -y && \
    apt-get install -y wget build-essential checkinstall libusb-1.0-0-dev libncursesw5-dev  libssl-dev  libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev && \
    cd /usr/src && \
    wget https://www.python.org/ftp/python/3.9.20/Python-3.9.20.tgz  && \
    tar xzf Python-3.9.20.tgz && \
    cd Python-3.9.20 && \
    ./configure --enable-optimizations && \
    make install && \
    python3.9 -m pip install tflite-support
EXPOSE 8501

CMD ["python3.9", "bert_server.py"]
