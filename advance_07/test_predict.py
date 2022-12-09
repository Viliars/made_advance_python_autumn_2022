import random
import string
from unittest.mock import Mock
import pytest
from predict import predict_message_mood


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

    message = random_message()
    assert (
        predict_message_mood(message, model, bad_thresholds, good_thresholds)
        == expected
    )
