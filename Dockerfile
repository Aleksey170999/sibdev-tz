FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /sibdev
COPY requirements.txt /sibdev/
RUN pip install -r requirements.txt
COPY . /sibdev/

RUN chmod +x /sibdev/entrypoint.sh
ENTRYPOINT ["/sibdev/entrypoint.sh"]