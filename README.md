# SeleniumLanguageTask

Условия задачи и критерии оценки смотрите на [stepik](https://stepik.org/lesson/237240/step/9?unit=209628) (для зарегистрированных пользователей).

В коде есть комментарии, поясняющие моё решение.

### Варианты запуска
```
pytest --language=es test_items.py
pytest --language=fr --browser_name=firefox test_items.py
pytest test_items.py
```

* В тест можно передавать любой язык, если не передать - по умолчанию будет использован _en-gb_.
* В тест можно передавать имя браузера (chrome, firefox), если не передать - по умолчанию будет использован _chrome_.