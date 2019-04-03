#!/usr/bin/env python

import numpy as np

import duckietown_challenges as dc
from aido_schemas.estimation_demo import protocol_simple_predictor
from zuper_nodes_wrapper.wrapper_outside import ComponentInterface, MsgReceived

def get_time_series(N):
    t = np.linspace(0, 10, N)
    alpha = 0.1
    x = np.sin(alpha*t) + np.random.randn(N) * 0.1
    return x

def main(cie: dc.ChallengeInterfaceEvaluator):
    agent_ci = ComponentInterface(fnin='/fifos/predictor-in',
                                  fnout='/fifos/predictor-out',
                                  expect_protocol=protocol_simple_predictor,
                                  nickname="predictor")

    # check compatibility so that everything
    # fails gracefully in case of error
    agent_ci._get_node_protocol()

    try:
        seed = 42
        agent_ci.write('seed', seed)

        N = 100
        N_training = int(N / 2)

        values = get_time_series(200)

        values_training = values[:N_training]
        values_test = values[N_training:]
        for value in values_training:
            agent_ci.write('observations', value)

        guess = []
        truth = []
        for value in values_test:
            agent_ci.write('get_prediction', None)
            msg_prediction: MsgReceived[float] = agent_ci.read_one(expect_topic='prediction')
            guess.append(msg_prediction.data)

            truth.append(value)
            agent_ci.write('observations', value)

        truth = np.array(truth)
        guess = np.array(guess)
        cie.info('truth: %s' % truth)
        cie.info('guess: %s' % guess)

        error_L1 = np.mean(np.abs(truth - guess))
        error_L2 = np.mean(np.power(truth - guess, 2))

        cie.set_score('error_L1', error_L1)
        cie.set_score('error_L2', error_L2)

    except dc.InvalidSubmission:
        raise
    except BaseException as e:
        raise dc.InvalidEvaluator() from e

    finally:
        agent_ci.close()


if __name__ == '__main__':
    with dc.scoring_context() as cie:
        main(cie)