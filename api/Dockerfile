FROM       python:3

WORKDIR    /app
COPY       requirements.txt /app/
RUN        pip install -r requirements.txt

COPY       api.py /app/
RUN        chmod a+x api.py

ENTRYPOINT ["python", "./api.py"]