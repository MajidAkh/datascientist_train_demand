FROM python:3.7.9


ENV WORK_DIR=/opt/datascientist
RUN mkdir ${WORK_DIR}

WORKDIR ${WORK_DIR}

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt 

ENTRYPOINT ["./pipeline/main.py"]
