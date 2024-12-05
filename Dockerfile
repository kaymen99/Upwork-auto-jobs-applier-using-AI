FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install-deps
RUN playwright install firefox

COPY . .

CMD [ "python", "./main.py" ]

