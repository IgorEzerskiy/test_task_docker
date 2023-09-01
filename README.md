# Для старту контейнерів:
`docker-compose up --build -d`
# Команда, що створює користувачів
`docker-compose exec server python ./test_task/manage.py loaddata ./test_task/users_fixture.json`