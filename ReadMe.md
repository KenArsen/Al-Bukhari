
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Python 3.10.8](https://img.shields.io/badge/python-3.11.7-blue.svg)](https://www.python.org/downloads/release/python-3117//)

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)


# Al Bukhari

And Allah Invites TO The Home OF PEACE

Discover a haven of spirituality and community at Al Bukhari 
Mosque. Nestled in the heart of Chicago, our mosque is more 
than a place of worship; it's a vibrant center for learning, charity, 
and communal harmony.


## Установка

1. Загрузите скрипт установки Docker:

   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   ```

2. Запустите скрипт установки Docker:

   ```bash
   sudo sh get-docker.sh
   ```

3. Инициализируйте репозиторий Git и настройте удаленный доступ:

   ```bash
   git init
   git config credential.helper '!aws codecommit credential-helper $@'
   git config credential.UseHttpPath true
   экспорт ключей
   git remote add origin <url>
   git pull origin main
   ```

4. Сборка и запуск Docker-контейнеров:

    ```bash
   docker-compose up -d --build
   ```

5. Запустите Docker-контейнеры (на переднем плане):

    ```bash
   docker-compose up
   ```