from random import random


class SomeModel:
    def predict(self, message: str) -> float:
        return random()


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    prob = model.predict(message)

    if prob < bad_thresholds:
        return "неуд"
    if prob > good_thresholds:
        return "отл"

    return "норм"
