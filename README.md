# Nginx и WSGI-сервер на Python с Docker

Этот проект демонстрирует запуск контейнеров для Nginx и WSGI-сервера на Python с использованием Docker и Docker Compose.

## Шаги выполнения

### 1. Создание контейнеров
#### 1.1 Контейнер Nginx
- Запуск контейнера:
  ```bash
  docker run -d -p 8081:80 --name my-nginx nginx
  ```

- заходим на localhost:8081

#### 2.1 Создание образа nginx из Dockerfile
- запукс контейнера на базе python 
```docker run -it python:3.10-slim bash```
- Установка Flask 
```pip install flask```
- Cоздадим файл app.py с нашим WSGI-приложением
```#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    
    response_body = b'Hello from Python WSGI Application!'
    return [response_body]

if __name__ == '__main__':
    print("Starting server on port 8082...")
    with make_server('0.0.0.0', 8082, application) as httpd:
        print("Server is running on port 8082...")
        httpd.serve_forever()
 ```
- Создадим Dockerfile
```FROM python:3.9-slim 

WORKDIR /app

COPY requirements.txt .
COPY app.py .

RUN pip install -r requirements.txt

# Явно указываем, что контейнер слушает все интерфейсы
ENV HOST=0.0.0.0
EXPOSE 8082

CMD ["python", "app.py"]
```
- Заупстим Flask сервер
```python app.py```
- Выйдем из контейнера
```exit```
- Собираем образ
```docker build -t python-wsgi .```

- Запустим контейнер
```docker run -d -p 8082:8082 --name my-python-app python-wsgi```

-проверяем образ
```docker ps```


#### 2.2 Cоздание образа nginx на Python

-Создаем файл Dockerfile для Nginx
```
FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
```
- Создаем файл index.html в той же папке
```
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Hello from custom Nginx container</h1>
</body>
</html>
```
-Собираем образ
```docker build -t custom-nginx .```

- Провереряем образ
```docker images```

[Скриншоты из docker] (https://disk.yandex.ru/d/qmIB_QvFNs9LSg)