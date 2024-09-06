.PHONY

install:
	pip install -r requirements.txt

test:
	python -m unittest discover tests

docker-build:
	docker build -t kafka-consumer .

docker-run:
	docker-compose up

clean:
	docker-compose down --rmi all
