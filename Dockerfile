FROM python:3.9.18

WORKDIR /TableroProyecto

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./ ./

EXPOSE 9000

CMD ["python", "app.py"]