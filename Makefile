

update-reqs:
	$(MAKE) -C experiment_manager update-reqs


define-challenge: update-reqs
	dts challenges define --config aido2-PRED.challenge.yaml

define-challenge-no-cache:  update-reqs
	dts challenges define --config aido2-PRED.challenge.yaml --no-cache

test-with-local-repos:
	docker-compose -f docker-compose-devel.yaml down -v
	docker-compose -f docker-compose-devel.yaml up -V --build

test:
	docker-compose -f docker-compose.yaml down -v
	docker-compose -f docker-compose.yaml up -V --build

submit-bea:
	make -C predictor_last   submit-bea
	make -C predictor_random submit-bea
	make -C predictor_mean   submit-bea
