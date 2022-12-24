FROM python:3
WORKDIR /telegram_bot
COPY requirements.txt /telegram_bot
RUN python3 -m pip install -r requirements.txt
COPY . /telegram_bot
EXPOSE 8888
CMD ["python", "bot.py"]