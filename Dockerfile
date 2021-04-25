FROM python:3.6

ADD entrypoint.sh /entrypoint.sh

RUN pip install apache-airflow==2.0.2

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"] "requirements.txt" "dags" "var.json"
