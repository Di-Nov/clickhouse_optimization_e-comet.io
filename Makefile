up-ch:
	docker-compose up -d --build clickhouse

up-ld:
	docker-compose up --build load_data

build:
	docker-compose build

down:
	docker-compose down

restart:
	docker-compose restart

stop:
	docker-compose stop

logs:
	docker-compose logs

ls:
	docker-compose ls

ps:
	docker ps -a