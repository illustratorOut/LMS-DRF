<h1>Перед началом использования программы заполните шаблон данными:</h1>

<h4>✔️ Команды для заполнения таблиц данными: </h4>

| Описание                                | Команды                        |
|-----------------------------------------|--------------------------------|
| Приминить миграции                      | ```python manage.py migrate``` |
| Создать пользователей и заполнить курсы | ```python manage.py fill```    |

<div style="display: flex; align-items: center;">
<h3 style="margin-right: 3%">
Собрать контейнер
</h3>

```commandline
docker-compose up -d --build
```

</div>


<H3 style="text-align: center;  color:red;"> .env </H3> 

 <div style="display: flex; align-items: center;">
    <div style="display: inline-block; margin: 2px;" >

| Шаблон |
|--------|

```text 
CACHE_ENABLED=True
REDIS=redis://127.0.0.1:6379

POSTGRES_DB=
POSTGRES_PASSWORD=
POSTGRES_USER=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=

STRIPE_API_KEY=

YANDEX_MAIL=
MAIL_PASSWORD=

CELERY_BROKER_URL=redis://redis:6379
CELERY_RESULT_BACKEND=redis://redis:6379
 ```

</div>
  </div>

