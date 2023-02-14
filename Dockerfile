FROM python:3.10.6-slim-buster

WORKDIR app/

COPY . app/

RUN cd app/ && pip install -r requirements.txt

CMD ["python", "app/vk_bot/bot.py"]