FROM python:3.8

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN pip install --upgrade numpy

CMD [ "bash", "run.sh" ]