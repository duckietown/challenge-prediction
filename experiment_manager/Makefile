repo=challenge-prediction-experiment_manager
# repo=$(shell basename -s .git `git config --get remote.origin.url`)
branch=$(shell git rev-parse --abbrev-ref HEAD)
tag=duckietown/$(repo):$(branch)

build:
	docker build -t $(tag) .

build-no-cache:
	docker build -t $(tag)  --no-cache .

push: build
	docker push $(tag)

