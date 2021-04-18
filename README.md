# ToDoapp
#### Приложение - задачник

##### Функционал:
- Просматривать текущие записи в списке;
- Добавлять запись в список;
- Править запись;
- Удалять запись;
- Перемещать запись на уровень выше, ниже;
- Отмечать задачу как сделанную;
- Фильтровать задачи по приоритету.

##### Написан с использованием:
- [Django](https://www.djangoproject.com/);
- [Bootstrap](https://getbootstrap.com/).

CRUD описан представлениями, основанными на [классах](https://djbook.ru/rel1.5/topics/class-based-views/generic-display.html). 
Фильтр представлен функциями.

##### Чтобы запустить проект локально:
- сделать импорты файла [requirements.txt](./requirements.txt);
- выполнить __python manage.py runserver__.

##### Использование:
- Приложение размещено на Heroku (https://todoverlan.herokuapp.com/);
- Доступ в админку: логин - _admin_, пароль - _admin_.

##### Что пофиксят/добавят:
- Перемещение задач на уровень выше/ниже;
- Покрытие [views](./todoapp/views.py) тестами.

##### Контакты:
- Vk (https://vk.com/lanfor)
- Ссылка на проект (https://github.com/Nik-Verlan/ToDoapp)
