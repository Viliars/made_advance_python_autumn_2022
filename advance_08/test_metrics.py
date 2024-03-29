from time import time, sleep
from random import randint
from metrics import Stats, MetricTimer, MetricAvg, MetricCount, BaseMetric


EPS = 0.1


def test_base_metric():
    metric = BaseMetric("test")

    values = []
    for _ in range(20):
        value = randint(0, 200)
        metric.add(value)
        values.append(value)

    assert metric.get_name() == "test"

    value = metric.get_value()
    mean = sum(values)

    assert type(value) is int
    assert value == mean

    metric.clear()

    assert metric.get_value() is None


def test_metric_timer():
    metric = MetricTimer("test")

    with metric:
        sleep(1)

    assert metric.get_name() == "test.timer"

    value = metric.get_value()

    assert type(value) is float
    assert abs(value - 1.0) < EPS

    metric.clear()

    assert metric.get_value() is None


def test_metric_avg():
    metric = MetricAvg("test")

    values = []
    for _ in range(20):
        value = randint(0, 200)
        metric.add(value)
        values.append(value)

    assert metric.get_name() == "test.avg"

    value = metric.get_value()
    mean = sum(values) / len(values)

    assert type(value) is float
    assert abs(value - mean) < EPS

    metric.clear()

    assert metric.get_value() is None


def test_metric_count():
    metric = MetricCount("test")

    values = []
    for _ in range(20):
        value = randint(0, 200)
        metric.add(value)
        values.append(value)

    assert metric.get_name() == "test.count"

    value = metric.get_value()
    mean = sum(values)

    assert type(value) is int
    assert value == mean

    metric.clear()

    assert metric.get_value() is None


def test_stats_timer():
    with Stats.timer("test"):
        sleep(1)

    with Stats.timer("test"):
        sleep(1)

    assert Stats.collect() == {"test.timer": 2.0}


def test_stats_avg():
    Stats.avg("test").add(5)
    Stats.avg("test").add(7)
    Stats.avg("test").add(5)
    Stats.avg("test").add(3)

    assert Stats.collect() == {"test.avg": 5.0}


def test_stats_count():
    for _ in range(15):
        Stats.count("test").add()
    Stats.count("test").add(5)

    assert Stats.collect() == {"test.count": 20}


def test_stats_collect():
    assert Stats.collect() == {}

    Stats.count("test").add()
    Stats.avg("test").add(7.0)
    Stats.avg("test").add(5.0)
    with Stats.timer("test"):
        sleep(1)

    assert Stats.collect() == {
        "test.count": 1,
        "test.avg": 6.0,
        "test.timer": 1.0,
    }

    assert Stats.collect() == {}


def test_stats_no_used():
    Stats.count("test")
    Stats.avg("test")
    Stats.timer("test")

    assert Stats.collect() == {}


def test_all():
    def calc() -> float:
        calc_count = getattr(calc, "call_count", 0)

        calc_count += 1
        match calc_count:
            case 1:
                sleep(0.1)
                setattr(calc, "call_count", calc_count)
                return 3
            case 2:
                sleep(0.3)
                setattr(calc, "call_count", calc_count)
                return 7
        return 0

    with Stats.timer("calc"):  # 0.1
        res = calc()  # 3

    Stats.count("calc").add()
    Stats.avg("calc").add(res)

    t1 = time()
    res = calc()  # 7
    t2 = time()
    Stats.timer("calc").add(t2 - t1)  # 0.3
    Stats.count("calc").add()
    Stats.avg("calc").add(res)

    Stats.count("http_get_data").add()
    Stats.avg("http_get_data").add(0.7)

    Stats.count("no_used")  # не попадет в результат collect

    metrics = Stats.collect()
    assert metrics == {
        "calc.count": 2,
        "calc.avg": 5.0,
        "calc.timer": 0.4,
        "http_get_data.count": 1,
        "http_get_data.avg": 0.7,
    }

    metrics = Stats.collect()
    assert metrics == {}
