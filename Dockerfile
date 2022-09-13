FROM continuumio/miniconda3

COPY entrypoint.sh /entrypoint.sh
COPY *.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
