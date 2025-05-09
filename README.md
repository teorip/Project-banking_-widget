## Цель проекта: *создать виджет для личного кабинета клиента банка, который показывает несколько последних успешных банковских операций клиента.*

## Установка:
### Poetry

Установка Poetry выполняется вводом команды в командной строке:
* на Unix-системах
```
curl -sSL https://install.python-poetry.org | python3 -
```
* на Windows:
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Далее, в зависимости от вашей системы, необходимо добавить соответствующую директорию в PATH:
```
Linux, MacOS, WSL
$HOME/.local/bin
```
```
Windows
%APPDATA%\Python\Scripts
```

Перезагружаем оболочку и проверяем корректность установки:
poetry --version
 
Вывод должен быть примерно таким
```
Poetry (version 1.4.2)
```
### Пакеты: flake8, black, mypy, isort
Установка выполняется командой в терминале IDE:
```
poetry add –group lint flake8 black mypy isort
```
### Python
Переходим на официальный сайт https://www.python.org/downloads/ и жмем download (скачать). Сайт автоматически определит разрядность вашей операционной системы и предложит сохранить 32-bit, либо 64-bit версию. Устанавливаем выбранную версию ПО.
#### **При установке**
* в появившемся окне вы можете выбрать Install Now — в таком случае Python будет установлен в место по умолчанию
* отметить галочкой Add python.exe to PATH

### PyCharm
* •	Переходим на официальный сайт: https://www.jetbrains.com/ru-ru/pycharm/
* •	Выбираем для какой ОС. Жмем скачать.
* •	Далее выбираем бесплатную community версию 
* •	Запускаем загруженный файл


### В модуле masks реализованы следующие функции:

* Функция **get_mask_card_number**  - функция маскировки номера банковской карты,
принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и
отображается в формате XXXX XX** **** XXXX, где X — это цифра номера.
То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками,
номер разбит по блокам по 4 цифры, разделенным пробелами.
```
Пример работы функции:
7000792289606361     #входной аргумент
7000 79** **** 6361  #выход функции
```

* Функция **get_mask_account** - функция маскировки номера банковского счета,
принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXX, где X— это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
```
Пример работы функции:
73654108430135874305  #входной аргумент
**4305  #выход функции
```

### В модуле widget реализованы следующие функции:
* Функция **mask_account_card** - принимает один аргумент — строку, содержащую тип и номер карты или счета,
возвращает строку с замаскированным номером
```
Пример работы функции:
Visa Platinum 7000792289606361  # входной аргумент
Visa Platinum 7000 79** **** 6361  # выход функции
```

*	Функция **get_date**  - принимает на вход строку с датой в формате  "2024-03-11T02:26:18.671407"
и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").
```
Пример работы функции:
Счет 73654108430135874305  #входной аргумент
Счет **4305  #выход функции
```

### В модуле processing реализованы следующие функции:
*	Функция **filter_by_state** - принимает список словарей и опционально значение для ключа 
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению.
```
Пример работы функции:
#Входной аргумент
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] 

#Выход функции со статусом по умолчанию 'EXECUTED'
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

#Выход функции, если вторым аргументов передано 'CANCELED'
[{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
```
*	Функция **sort_by_date** - принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать новый список, отсортированный по дате (date).
```
Пример работы функции:
#Входной аргумент
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}] 

#Выход функции (сортировка по убыванию, т. е. сначала самые последние операции)
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```
### В модуле generators.py реализованы следующие функции:
* функция *filter_by_currency* принимает на вход список словарей,
представляющих транзакции.
Функция должна возвращать итератор, который поочередно выдает транзакции,
где валюта операции соответствует заданной (например, USD).
```
Пример использования функции:
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```
* Генератор *transaction_descriptions* принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
```
Пример использования функции
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```
* Генератор *card_number_generator* выдает номера банковских карт в формате 
*XXXX XXXX XXXX XXXX*, где *X* — цифра номера карты.
Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.

```
Пример использования функции
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```


### Тестирование
Используйте библиотеку pytest
```
poetry add --gpoup dev pytest
```
##### Для анализа покрытия кода установить библиотеку 
pytest-cov.
```
poetry add --group dev pytest-cov
```
pytest-cov с названием версии отобразится в группе dev файла pyprojeck.toml 
##### Установить Coverage.py через pip:
```
pip install coverage
```
Использование с Pytest:
```
pip install pytest-cov
```
#### Применённые тест-кейсы:
##### Модуль masks
###### Функция *get_mask_card_number*
* Тестирование правильности маскирования номера карты.
* Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
* Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.
###### Функция *get_mask_account*
* Тестирование правильности маскирования номера счета.
* Проверка работы функции с различными форматами и длинами номеров счетов.
* Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
#### Модуль widget
###### Функция *mask_account_card*
* Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
* Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
* Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.
###### Функция *get_date*
* Тестирование правильности преобразования даты.
* Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
* Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.
##### Модуль processing
###### Функция *filter_by_state*
* Тестирование фильтрации списка словарей по заданному статусу state.
* Проверка работы функции при отсутствии словарей с указанным статусом state в списке.
* Параметризация тестов для различных возможных значений статуса state.
###### Функция *sort_by_date*
* Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
* Проверка корректности сортировки при одинаковых датах.
* Тесты на работу функции с некорректными или нестандартными форматами дат.

##### Модуль generators
###### Функция *filter_by_currency*
* Напишите тесты, проверяющие, что функция корректно фильтрует транзакции по заданной валюте.
* Проверьте, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
* Убедитесь, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.
###### Генератор *transaction_descriptions*
* Проверьте, что функция возвращает корректные описания для каждой транзакции.
* Тестируйте работу функции с различным количеством входных транзакций, включая пустой список.
###### Генератор *card_number_generator*
* Напишите тесты, которые проверяют, что генератор выдает правильные номера карт в заданном диапазоне.
* Проверьте корректность форматирования номеров карт.
* Убедитесь, что генератор корректно обрабатывает крайние значения диапазона и правильно завершает генерацию.

##### Общие аспекты тестирования
* *Фикстуры*: для всех тестов создайте фикстуры, которые предоставят тестовые данные для списков словарей, включая различные случаи и комбинации state и date.
* *Покрытие тестами*: убедитесь, что все ветви кода и исключения, которые могут быть сгенерированы вашими функциями, тестируются.