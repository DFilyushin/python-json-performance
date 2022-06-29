# python-json-performance

## Назначение

Тестирование производительности встроенного сериализатора 
json, orjson, а также модуля Pydantic для обработки больших наборов данных


## Установка и запуск

`pip install -r requirements.txt`

`psql -f /some/path/database.sql`

`python main.py`


## Результаты

PostgreSQL 12.5, compiled by Visual C++ build 1914, 64-bit

Python 3.9.6

```
Cursor return 100000 records
sql query:  0.5110068321228027 

json dumps:  1.5209925174713135 

orjson dumps:  0.05404520034790039 

Cursor return 100000 records
sql query again:  0.4459836483001709 

pydantic json:  6.6844751834869385

```