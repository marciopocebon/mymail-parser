mymail-parser
==========
[![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/downloads/)
[![Built with Love](https://forthebadge.com/images/badges/built-with-love.svg)](https://emojipedia.org/growing-heart/)

**mymail-parser** — это простой Python-скрипт, использующий мощности модуля *Selenium* для автоматизации парсинга почтовых адресов социальной сети "Мой мир@Mail.Ru".

:warning: ***ДИСКЛЕЙМЕР.*** :warning: Инструмент был написан из исследовательских соображений и не несет в себе цели навредить кому-либо (чему-либо). Слово бойскаута.

![Screenshot-1](https://user-images.githubusercontent.com/23141800/43039200-281d9388-8d31-11e8-8b52-565d30248bc8.png "Немного скриншотов")

Порядок использования
==========
Для использования скрипта необходимо провести ряд подготовительных мероприятий, о которых ниже по порядку:

 1. Заполнить поля `LOGIN` и `PASSWORD` в файле *credentials.py* своими логином и паролем от соц. сети "Мой мир@Mail.Ru" соответственно.
 2. Скачать и распаковать веб-драйвер браузера Firefox ([geckodriver](https://github.com/mozilla/geckodriver/releases/latest)), после чего указать к нему путь в переменной `GECKODRIVER_PATH` в файле *mymail_parser.py*.
 3. Отправиться на [Мой Мир](https://my.mail.ru/) и сформировать поисковой запрос, почтовые адреса из результата которого мы хотели бы ~~поиметь~~ спарсить, и скопировать получившуюся ссылку из поисковой строки (должно получиться что-то вроде https://my.mail.ru/my/search_people?&name=John%20Doe&gender=1&agerange=16) в переменную `SEARCH_QUERY` в файле *mymail_parser.py*. Для успешного выполнения поиска аккаунт должен быть подтверждён, и одним из способов подтверждения аккаунта является привязка к нему номера телефона (механизм безопасности № 1).
 4. **(опционально)** Включить дебаг-режим можно присвоив флагу `HEADLESS` в файле *mymail_parser.py* значение `True`. В этом случае при запуске скрипта будет открываться окно виртуального Firefox'а, по которому будет прыгать эфемерный курсор, нажимая на вполне реальные кнопки :wink:

Запуск
==========
DEB-зависимости:
- интерпретатор python3.x (или выше)

PIP-зависимости:
 - selenium
 - tqdm

Выполнив описанные выше подготовления и разрешив необходимые зависимости в один клик с помощью `pip`
```
$ pip install -r requirements.txt
```
можно запустить скрипт как
```
$ python3 mymail_parser.py <ЧИСЛО_СКРОЛЛОВ>
```
где `ЧИСЛО_СКРОЛЛОВ` — количество раз, сколько будет прокручена вниз до конца лента результатов поиска (при каждой прокрутке вниз происходит подгрузка следующей порции результатов).

:warning: **Иметь в виду:**
 - 1 скролл ≈ 8 email-адресов, однако точно сказать, чему равен 1 скролл, нельзя — количество *валидных* адресов, умещающихся на одной странице (в пределах одного скролла), зависит от самого поискового запроса, а также уменьшается с увеличением параметра `ЧИСЛО_СКРОЛЛОВ` (особенности строения социальной сети).
- Максимальное количество email-адресов, которое можно спарсить через поисковую форму Моего Мира таким способом, равно 450, дальше страница результатов просто не прокручивается (механизм безопасности № 2). Так как нельзя точно рассчитать, сколько скроллов для этого понадобится, рекомендуется указывать заведомо большее значение параметра `ЧИСЛО_СКРОЛЛОВ`, например, `100`. При достижении конца страницы скрипт завершит свою работу.
- Через определенное количество успешно совершённых поисковых запросов мейл.ру дает таймаут аккаунту на выполнение поиска в Моем Мире (механизм безопасности № 3). Таймаут временный (не более суток — время блокировки зависит от степени превышения допустимого лимита), пугаться не нужно, это не перманент. Маячком получения таймаута служит появление сообщения `[-] Failure: server timeout or bad search query`.

Результат сохраняется в файл *out.csv*.

Постскриптум
==========
Скрипт разрабатывался и тестировался под ОС Windows.

Если этот инструмент оказался полезен кому-либо, угостить меня кофе можно по ссылке ниже :coffee:

[![Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoff.ee/snovvcrash)
