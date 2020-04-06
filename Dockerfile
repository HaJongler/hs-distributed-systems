FROM       python:3

WORKDIR    /app
COPY       homework.py /app/
RUN        chmod a+x homework.py

ENTRYPOINT ["python", "./homework.py"]