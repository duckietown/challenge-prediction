ARG AIDO_REGISTRY
FROM ${AIDO_REGISTRY}/duckietown/aido-base-python3:daffy-amd64


ARG PIP_INDEX_URL="https://pypi.org/simple"
ENV PIP_INDEX_URL=${PIP_INDEX_URL}
RUN echo PIP_INDEX_URL=${PIP_INDEX_URL}
COPY requirements.txt requirements.txt
RUN pip install -U "pip>=20.2"
RUN pip install  -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "predictor_mean.py"]
