import random
import string
from unittest.mock import Mock
import pytest
from predict import predict_message_mood

COUNT_TESTS = 10


def random_message():
    length = random.randint(0, 20)
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


@pytest.mark.parametrize(
    "prob,bad_thresholds,good_thresholds,expected",
    [
        (0.0, 0.3, 0.8, "неуд"),
        (0.29, 0.3, 0.8, "неуд"),
        (0.7, 0.8, 0.9, "неуд"),
        (0.3, 0.3, 0.8, "норм"),
        (0.4, 0.3, 0.8, "норм"),
        (0.81, 0.3, 0.8, "отл"),
        (0.5, 0.3, 0.4, "отл"),
        (1.0, 0.3, 0.9, "отл"),
    ],
)
def test_predict_message_mood(prob, bad_thresholds, good_thresholds, expected):
    model = Mock()
    model.predict.return_value = prob

    for i in range(COUNT_TESTS):
        message = random_message()
        assert (
            predict_message_mood(message, model, bad_thresholds, good_thresholds)
            == expected
        )
        assert len(model.predict.call_args_list[i].args) == 1
        assert type(model.predict.call_args_list[i].args[0]) is str
        assert model.predict.call_args_list[i].args[0] == message

    assert model.predict.call_count == COUNT_TESTS


@pytest.mark.parametrize(
    "message,prob,bad_thresholds,good_thresholds",
    [
        (None, 0.0, 0.3, 0.8),
        ((1, 2, 3), 0.29, 0.3, 0.8),
        ([1, 2, 3], 0.7, 0.8, 0.9),
        (Mock(), 0.3, 0.3, 0.8),
        (42, 0.4, 0.3, 0.8),
        (42.0, 0.81, 0.3, 0.8),
        (True, 0.5, 0.3, 0.4),
        ({}, 1.0, 0.3, 0.9),
    ],
)
def test_predict_message_mood_errors(message, prob, bad_thresholds, good_thresholds):
    model = Mock()
    model.predict.return_value = prob

    with pytest.raises(TypeError):
        predict_message_mood(message, model, bad_thresholds, good_thresholds)

    assert model.predict.call_count == 0
