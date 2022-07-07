
start:
	docker-compose up -d
	sleep 10s
	python initial.py

install:
	pip install -r requirements.txt

stop:
	docker-compose down