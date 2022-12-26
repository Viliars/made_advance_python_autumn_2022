from __future__ import annotations
from time import time
from typing import Any

Number = int | float


class BaseMetric:
    def __init__(self, name: str):
        self.name: str = name
        self.value: Any = None

    def get_name(self) -> str:
        return self.name

    def get_value(self) -> Number | None:
        return self.value

    def add(self, value: Any) -> BaseMetric:
        if self.value:
            self.value += value
        else:
            self.value = value

        return self

    def clear(self) -> BaseMetric:
        self.value = None

        return self


class MetricTimer(BaseMetric):
    def __init__(self, name):
        super().__init__(name=name)

    def get_name(self) -> str:
        return f"{self.name}.timer"

    def __enter__(self) -> MetricTimer:
        self.start_time: float = time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time()

        execution_time = end_time - self.start_time

        if self.value:
            self.value += execution_time
        else:
            self.value = execution_time

        del self.start_time


class MetricAvg(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.value: Number | None = None
        self.size: int = 0

    def get_name(self) -> str:
        return f"{self.name}.avg"

    def get_value(self) -> Number | None:
        if self.value:
            return self.value / self.size

        return None

    def add(self, value: Number) -> MetricAvg:
        if self.value:
            self.value += value
        else:
            self.value = value

        self.size += 1

        return self

    def clear(self) -> MetricAvg:
        self.value = None
        self.size = 0

        return self


class MetricCount(BaseMetric):
    def get_name(self) -> str:
        return f"{self.name}.count"

    def add(self, value: int = 1) -> MetricCount:
        if self.value:
            self.value += value
        else:
            self.value = value
        return self


class Stats:
    __metrics: dict[str, Any] = {}

    @staticmethod
    def timer(name: str) -> MetricTimer:
        metric_type = "timer"
        metric_name = f"{name}.{metric_type}"

        if metric_name not in Stats.__metrics:
            Stats.__metrics[metric_name] = MetricTimer(name)

        return Stats.__metrics[metric_name]

    @staticmethod
    def avg(name: str) -> MetricAvg:
        metric_type = "avg"
        metric_name = f"{name}.{metric_type}"

        if metric_name not in Stats.__metrics:
            Stats.__metrics[metric_name] = MetricAvg(name)

        return Stats.__metrics[metric_name]

    @staticmethod
    def count(name: str) -> MetricCount:
        metric_type = "count"
        metric_name = f"{name}.{metric_type}"

        if metric_name not in Stats.__metrics:
            Stats.__metrics[metric_name] = MetricCount(name)

        return Stats.__metrics[metric_name]

    @staticmethod
    def collect() -> dict[str, Number]:
        metrics = {}
        for name, metric in Stats.__metrics.items():
            value = metric.get_value()
            if type(value) is float:
                value = round(value, 1)

            if value:
                metrics[name] = value

        Stats.__metrics = {}

        return metrics
