
start:
	docker-compose up -d
	python initial.py

install:
	pip install -r requirements.txt

stop:
	docker-compose down