# HW7

#### Запуск тестов
```bash
python3 -m coverage run -m unittest tests.py
```

#### Просмотр покрытия
```bash
python3 -m coverage report
```

#### Проверка pylint
```bash
pylint src/ --disable=missing-docstring
pylint tests.py --disable=missing-docstring
```

#### Проверка flake8
```bash
flake8 src/
flake8 tests.py
```