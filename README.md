﻿
mymail-parser
==========
**mymail-parser** — это простой Python-скрипт, использующий мощности модуля *Selenium* для автоматизации парсинга почтовых адресов социальной сети "Мой мир@Mail.Ru".

***ДИСКЛЕЙМЕР.*** Инструмент был написан из исследовательских соображений и не несет в себе цели навредить кому-либо (чему-либо). Слово бойскаута.

Порядок использования
==========
Для использования скрипта необходимо провести ряд подготовительных мероприятий, о которых ниже по порядку:

 1. :warning: Заполнить поля `LOGIN` и `PASSWORD` в файле *credentials.py* своими логином и паролем от соц. сети "Мой мир@Mail.Ru" соответственно.
 2. Скачать и распаковать веб-драйвер браузера Firefox ([geckodriver](https://github.com/mozilla/geckodriver/releases/latest)), после чего указать к нему путь в переменной `GECKODRIVER_PATH` в файле *mymail_parser.py*.
 3. Отправиться на [Мой Мир](https://my.mail.ru/) и сформировать поисковой запрос, почтовые адреса из результата которого мы хотели бы ~~поиметь~~ спарсить, и скопировать получившуюся ссылку из поисковой строки (должно получиться что-то вроде https://my.mail.ru/my/search_people?&name=John%20Doe&gender=1&agerange=16) в переменную `SEARCH_QUERY` в файле *mymail_parser.py*.
 4. **(опционально)** Включить дебаг-режим можно присвоив флагу `HEADLESS` в файле *mymail_parser.py* значение `True`. В этом случае при запуске скрипта будет открываться окно виртуального Firefox'а, по которому будет прыгать эфемерный курсор, нажимая на вполне реальные кнопки :wink:

Запуск
==========
Выполнив описанные выше подготовления и разрешив необходимые зависимости с помощью *pip*
```
$ pip install -r requirements.txt
```
можно запустить скрипт как
```
$ python3 mymail_parser.py <ЧИСЛО_СКРОЛЛОВ>
```
где `<ЧИСЛО_СКРОЛЛОВ>` — количество раз, сколько будет прокручена вниз до конца лента результатов поиска (при каждой прокрутке вниз происходит подгрузка следующей порции результатов).

:warning: **Иметь в виду:**
 - *1 скролл $\approx$ 10 email-адресов*
при $0 <$ `<ЧИСЛО_СКРОЛЛОВ>` $\leqslant 5$;
*1 скролл $\approx$ 9 email-адресов*
при $5 <$ `<ЧИСЛО_СКРОЛЛОВ>` $\leqslant 10$;
*1 скролл $\to$ 5 email-адресам*
при `<ЧИСЛО_СКРОЛЛОВ>` $> 10$.
Количество *валидных* адресов, умещающихся на одной странице (в пределах одного скролла), также зависит от самого поискового запроса — особенности строения социальной сети.
- Максимальное количество email-адресов, которые можно спарсить через поисковую форму Моего Мира таким способом, примерно равно 450, дальше страница результатов просто не прокручивается.
- Через определенное количество успешно совершённых поисковых запросов мейл.ру дает таймаут аккаунту на выполнение поиска в Моем Мире. Таймаут временный (не более суток — время блокировки зависит от степени превышения допустимого лимита), пугаться не нужно, это не перманент. В скрипте маячком получения таймаута служит появление сообщения `[-] Failure: server timeout or bad search query`.

Результат сохраняется в файл *out.csv*.

Post Scriptum
==========
Скрипт разрабатывался и тестировался под ОС Windows.

Если этот инструмент оказался полезен кому-либо, угостить меня кофе можно по ссылке ниже :coffee:

[![Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://buymeacoff.ee/snovvcrash)
