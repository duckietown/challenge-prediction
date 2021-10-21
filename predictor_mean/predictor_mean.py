#!/usr/bin/env python3

import numpy as np

from aido_schemas import wrap_direct, Context
from aido_schemas.estimation_demo import protocol_simple_predictor


class PredictorMean:
    """Returns the mean of previous values as prediction."""

    def init(self):
        self.values = []

    def on_received_seed(self, data: int):
        np.random.seed(data)

    def on_received_observations(self, data: float):
        self.values.append(data)

    def on_received_get_prediction(self, context: Context):
        if not self.values:
            guess = 0.0
        else:
            guess = np.mean(self.values)

        context.write("prediction", guess)


def main():
    node = PredictorMean()
    protocol = protocol_simple_predictor
    wrap_direct(node=node, protocol=protocol)


if __name__ == "__main__":
    main()
