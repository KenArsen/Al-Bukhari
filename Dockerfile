FROM public.ecr.aws/docker/library/python:3.11
#FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    ENV_FILE=.env

WORKDIR /albukhari

RUN pip install --upgrade pip && \
    apt-get update

COPY requirements/base.txt /albukhari/
RUN pip install -r /albukhari/base.txt

COPY . .

EXPOSE 8000
RUN if [ ! -d "static" ]; then mkdir "static"; fi

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Очищаем кэш pip и временные файлы
RUN pip cache purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/*

CMD ["./entrypoint.sh"]
