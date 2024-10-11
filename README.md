# Виджет банковских операций клиента
Этот виджет показывает несколько последних банковских операций клиента. 
Он умеет обрабатывать информацию как о картах, так и о счетах, и выдает их замаскированные данные. 
Также программа реализует вывод даты, совершенной операции. Выводит успешные и отмененные операции клиента, а так же сортирует все операции клиента от последней совершенной.
Дополнительно реализовано, что при данном списке транзакций поочередно выводятся транзакции, где валюта операции соответствует заданной,
возвращает описание каждой операции из этого списка, а так же генерируются номера карт. 

Добавлен декоратор, который будет автоматически регистрировать детали выполнения функций, такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках. Это позволит обеспечить более глубокий контроль и анализ поведения программы в процессе ее выполнения

## Использование программы
**Весь процесс работы программы заключен в файле main.py**
1. Запустите файл main.py
2. По запросу программы введите тип и номер карты или счета
3. Программа выведет замаскированные данные введенных значений
4. По запросу программы введите данные по операции, в формате 2024-03-11T02:26:18.671407
5. Программа выведет дату совершенной операции
6. По запросу программы введите, какие операции нужно просмотреть
7. Программа выведет только те операции, которые необходимы, на основании ввода
8. По запросу программы введите параметр, чтобы определить метод сортировки
9. Программа выведет все операции, отсортированные от последней совершенной до самой ранней
10. Автоматически программа выведет описание каждой операции по всем транзакциям по очереди
11. Автоматически сгенерируются номера карт
12. По запросу программы введите валюту операции для вывода транзакций

**Работа декоратора**
1. Запустите файл src/decorators.py
2. Если будет введено название файла, в который нужно записать данные, то результат будет выведен в него
3. Если название файла не будет указано, то результаты будут выведены в консоль
4. Обратите внимание, что если будут введены не числовые значения, то будет выведено сообщение об ошибке


## Примеры использования
```
Введите тип и номер карты или введите счет:
Visa 1111222233334444
Visa 1111 22** **** 4444
Введите дату:
2024-03-11T02:26:18.671407
11.03.2024
Введите параметр для ключа состояния операций state, успешные или отмененные (EXECUTED/CANCELED):
EXECUTED
[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
Введите метод сортировки операций, по убыванию или по возрастанию (True/False):
False
[{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
Описание каждой операции по всем транзакциям по очереди:
Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации
Генерация номеров банковских карт в формате XXXX XXXX XXXX XXXX:
0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
Введите валюту операции для вывода транзакций:
USD
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
{'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}

Process finished with exit code 0
```
```
Function my_function started
my_function ok
Result = 3
Function my_function finished
```
```
Function my_function started
my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: ((1, '2'), {})
Function my_function finished
```

## Тестирование
**Программа прошла тестирование по всем модулям**

### *Модуль masks*

Функция `get_mask_card_number:`
1. Тестирование правильности маскирования номера карты.
2. Проверка работы функции на различных входных форматах номеров карт, включая нестандартные длины номеров.
3. Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.

Функция `get_mask_account:`
1. Тестирование правильности маскирования номера счета.
2. Проверка работы функции с различными форматами и длинами номеров счетов.
3. Проверка, что функция корректно обрабатывает входные строки, где номер счета меньше ожидаемой длины или отсутствует.

### *Модуль widget*

Функция `mask_account_card:`
1. Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
2. Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
3. Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

Функция `get_data:`
1. Тестирование правильности преобразования даты.
2. Проверка работы функции на различных входных форматах даты, включая нестандартные строки с датами.
3. Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.

### *Модуль processing*

Функция `filter_by_state:`
1. Тестирование фильтрации списка словарей по заданному статусу state.
3. Параметризация тестов для различных возможных значений статуса state.

Функция `sort_by_date:`
1. Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
3. Тесты на работу функции с некорректными или нестандартными форматами дат.

### *Модуль generators*

Функция `filter_by_currency:`
1. Тестирование, проверяющее, что функция корректно фильтрует транзакции по заданной валюте.
2. Тестирование, проверяющее, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют.
3. Тестирование, проверяющее, что генератор не завершается ошибкой при обработке пустого списка или списка без соответствующих валютных операций.

Функция `transaction_descriptions:`
1. Тестирование, проверяющее, что функция возвращает корректные описания для каждой транзакции.
2. Тестирование очередности вывода операций, а также тестирование пустого списка транзакий.

Функция `card_number_generator:`
1. Тестирование, которое проверяет, что генератор выдает правильные номера карт в заданном диапазоне.
2. Проверка верной очередности вывода номеров карт.

### *Модуль decorators*

Функция `log:`
1. Тестирование на запись в файл
2. Тестирование на вывод в консоль
3. Тестирование на ошибку (если вместо числа ввели строковый тип/ запись в файл
4. Тестирование на ошибку (если вместо числа ввели строковый тип/ вывод в консоль
5. Тестирование на то, что функция выдает верный результат


Этот проект лицензирован по [лицензии MIT](LICENSE)