FROM python:3.12-slim
ADD <DAY>/main.py /src/main.py
WORKDIR /src
CMD ["python", "./main.py"]