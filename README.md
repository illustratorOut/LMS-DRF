<h1>Перед началом использования программы заполните шаблон данными:</h1>

<h4>✔️ Команда для заполнения таблиц данными: </h4>

| Описание                                | Команды                        |
|-----------------------------------------|--------------------------------|
| Приминить миграции                      | ```python manage.py migrate``` |
| Создать пользователей и заполнить курсы | ```python manage.py fill```    |

<H3 style="text-align: center;  color:red;"> .env </H3> 

 <div style="display: flex; align-items: center;">
    <div style="display: inline-block; margin: 2px;" >

| Шаблон |
|--------|

```text 
CACHE_ENABLED=True
REDIS=redis://127.0.0.1:6379

POSTGRES_NAME=
POSTGRES_PASSWORD=
POSTGRES_USER=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=

STRIPE_API_KEY=

YANDEX_MAIL=
MAIL_PASSWORD=
 ```

</div>
  </div>

