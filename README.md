# Взлом электронного дневника школы
Данный код дает возможность изменять содержимое базы данных сайта электронного дневника школы при условии наличия доступа к серверу. А именно, исправлять двойки и тройки на пятерки, удалять замечания учителей и добавлять похвалы.

## Запуск

- Скачайте код
- Скопируйте файл `scripts.py` на сервер в директорию, содержащую файл `manage.py`
- Запустите Django shell на сервере командой `python3 manage.py shell`
- В интерактивной консоли введите `import scripts`
- Для исправления плохих оценок на пятерки в интерактивной консоли введите `scripts.fix_marks('имя ученика')`
- Для удаления замечаний от учителей в интерактивной консоли введите `scripts.remove_chastisements('имя ученика')`
- Для добавления похвалы от учителя по определенному предмету в интерактивной консоли введите `scripts.create_commendation('имя ученика', 'название предмета с заглавной буквы')`

## Локальное тестирование

Для тестирования можно запустить сайт электронного дневника локально. ([Ссылка на репозиторий](https://github.com/devmanorg/e-diary/tree/master)) Также потребуется файл с заполненной базой данных sqlite.


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
