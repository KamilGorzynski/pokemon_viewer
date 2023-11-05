run:
	docker-compose up --build

down:
	docker-compose down

shell:
	docker-compose exec app bash

django_shell:
	docker-compose exec app ./manage.py shell_plus

test:
	docker-compose exec -T app pytest

coverage:
	docker-compose exec -T app coverage report -m
