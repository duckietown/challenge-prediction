ARG AIDO_REGISTRY
FROM ${AIDO_REGISTRY}/duckietown/aido-base-python3:daffy

ARG PIP_INDEX_URL
ENV PIP_INDEX_URL=${PIP_INDEX_URL}
RUN echo PIP_INDEX_URL=${PIP_INDEX_URL}

COPY requirements.txt .
RUN pip install -U pip>=20.2
RUN pip install --use-feature=2020-resolver -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "predictor_random.py"]
