# users-task
Клоним + создаем виртуалку(питон3.6) + миграции = профит
---
user/ - идет заброс 'https://randomuser.me/api/', получаем данные сохраняем в бд, ответом получаем сохраненные данные

Отдельно сделать роут на забпрос цифр из хешей. -- /user/hash/

Отдельно сделать роут для краткой инфы: Имя, фамилия, почта (созданная нами), город и код страны. -- /user/info/short/
посмотреть весь список -- /user/list/

писал доку в спешке, прошу сильно не ругать, так же ничего не менял в setting.py (в плане защиты ключей и тд)