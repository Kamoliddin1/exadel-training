# Cleaning Company
##### _Project for exadel training by 
### [Database Design](https://dbdiagram.io/d/62739fdc7f945876b6bf0c12)
- ✨Magic ✨

## Installation

Project requires [Django](https://docs.djangoproject.com/) 3.2+ to run.

```sh
cd crm
pip3 install requirements.txt
```
## Celery
```sh
celery -A crm.celery worker -B -l info
celery -A crm.celery beat -l info
```
## Development

```sh
python manage.py runserver
127.0.0.1:8000
```

## License

MIT
