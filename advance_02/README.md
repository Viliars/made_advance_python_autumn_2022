# Advance HW2 - Client/Server

#### Запуск сервера
```bash
python3 server.py -w 10 -k 7
```

#### Запуск клиента
```bash
python3 client.py 10 urls.txt
```

#### Генерация "хороших" урлов
```bash
python3 generate_urls.py
```

#### Запуск тестов
```bash
python3 -m unittest tests/blackbox_tests.py
```

```bash
pytest
```

#### Проверка pylint
```bash
pylint .
```

#### Проверка flake8
```bash
flake8 .
```

#### Использовние Black
```bash
black .
```