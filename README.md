# REST API для системы комментариев блога. 
## Сборка проекта
Установить зависимости:
```python
pip install -r requirements.txt
```
Создать базу ```'project_blog'``` в postgres

Cоздать миграции:
```python
python manage.py makemigrations
```
Применить миграции:
```python
python manage.py migrate
```
Выполнить команду:
```python
python manage.py runserver
```
Примеры запросов представлены в файле ```requests.http```