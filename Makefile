
define-challenge:
	dts challenges define --config simple_prediction.challenge.yaml

define-challenge-no-cache:
	dts challenges define --config simple_prediction.challenge.yaml --no-cache

test-with-local-repos:
	docker-compose -f docker-compose-devel.yaml down -v
	docker-compose -f docker-compose-devel.yaml up -V --build

test:
	docker-compose -f docker-compose.yaml down -v
	docker-compose -f docker-compose.yaml up -V --build
