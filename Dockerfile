FROM python:3.8

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade numpy

COPY . .

CMD [ "bash", "run.sh" ]