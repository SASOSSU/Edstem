FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /emp
COPY requirements.txt /emp/
RUN pip install -r requirements.txt
COPY . /emp/