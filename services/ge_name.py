import random
def random_name():
    names = [
    {'name': 'Александр', 'is_man': True}, {'name': 'Михаил', 'is_man': True}, {'name': 'Екатерина', 'is_man': False},
    {'name': 'Анна', 'is_man': False}, {'name': 'Дмитрий', 'is_man': True}, {'name': 'Иван', 'is_man': True},
    {'name': 'Ольга', 'is_man': False}, {'name': 'Наталья', 'is_man': False}, {'name': 'Артем', 'is_man': True},
    {'name': 'София', 'is_man': False}, {'name': 'Мария', 'is_man': False}, {'name': 'Алексей', 'is_man': True},
    {'name': 'Елена', 'is_man': False}, {'name': 'Владимир', 'is_man': True}, {'name': 'Ксения', 'is_man': False},
    {'name': 'Андрей', 'is_man': True}, {'name': 'Алиса', 'is_man': False}, {'name': 'Павел', 'is_man': True},
    {'name': 'Евгения', 'is_man': False}, {'name': 'Николай', 'is_man': True}, {'name': 'Татьяна', 'is_man': False},
    {'name': 'Сергей', 'is_man': True}, {'name': 'Виктория', 'is_man': False}, {'name': 'Ирина', 'is_man': False},
    {'name': 'Денис', 'is_man': True}, {'name': 'Юлия', 'is_man': False}, {'name': 'Анастасия', 'is_man': False},
    {'name': 'Антон', 'is_man': True}, {'name': 'Олег', 'is_man': True}, {'name': 'Кристина', 'is_man': False},
    {'name': 'Артур', 'is_man': True}, {'name': 'Ева', 'is_man': False}, {'name': 'Григорий', 'is_man': True},
    {'name': 'Людмила', 'is_man': False}, {'name': 'Роман', 'is_man': True}, {'name': 'Алина', 'is_man': False},
    {'name': 'Дарина', 'is_man': False}, {'name': 'Василий', 'is_man': True}, {'name': 'Егор', 'is_man': True},
    {'name': 'Лариса', 'is_man': False}, {'name': 'Полина', 'is_man': False}, {'name': 'Станислав', 'is_man': True},
    {'name': 'Карина', 'is_man': False}, {'name': 'Нина', 'is_man': False}, {'name': 'Максим', 'is_man': True},
    {'name': 'Любовь', 'is_man': False}, {'name': 'Георгий', 'is_man': True}, {'name': 'Маргарита', 'is_man': False},
    {'name': 'Константин', 'is_man': True}, {'name': 'Валентина', 'is_man': False}, {'name': 'Валентин', 'is_man': True},
    {'name': 'Тимур', 'is_man': True}, {'name': 'Милана', 'is_man': False}, {'name': 'Вероника', 'is_man': False},
    {'name': 'Артемий', 'is_man': True}, {'name': 'Надежда', 'is_man': False}, {'name': 'Валерия', 'is_man': False},
    {'name': 'Светлана', 'is_man': False}, {'name': 'Владислав', 'is_man': True}, {'name': 'Айгуль', 'is_man': False},
    {'name': 'Глеб', 'is_man': True}, {'name': 'Елена', 'is_man': False}, {'name': 'Ангелина', 'is_man': False},
    {'name': 'Руслан', 'is_man': True}, {'name': 'Тамара', 'is_man': False}, {'name': 'Диана', 'is_man': False},
    {'name': 'Эдуард', 'is_man': True}, {'name': 'Юрий', 'is_man': True}, {'name': 'Нелли', 'is_man': False},
    {'name': 'Дарья', 'is_man': False}, {'name': 'Марина', 'is_man': False}, {'name': 'Игорь', 'is_man': True},
    {'name': 'Маргарита', 'is_man': False}, {'name': 'Арсений', 'is_man': True}, {'name': 'Жанна', 'is_man': False},
    {'name': 'Раиса', 'is_man': False}, {'name': 'Федор', 'is_man': True}, {'name': 'Семен', 'is_man': True},
    {'name': 'Таисия', 'is_man': False}, {'name': 'Милена', 'is_man': False}, {'name': 'Эмилия', 'is_man': False},
    {'name': 'Алевтина', 'is_man': False}, {'name': 'Эльмира', 'is_man': False}, {'name': 'Марианна', 'is_man': False},
    {'name': 'Дмитрий', 'is_man': True}, {'name': 'Игнатий', 'is_man': True}, {'name': 'Матвей', 'is_man': True},
    {'name': 'Юрий', 'is_man': True}, {'name': 'Юлиана', 'is_man': False}, {'name': 'Анатолий', 'is_man': True},
    {'name': 'Галина', 'is_man': False}, {'name': 'Серафим', 'is_man': True}, {'name': 'Милан', 'is_man': True},
    {'name': 'Исидор', 'is_man': True}, {'name': 'Антонина', 'is_man': False}, {'name': 'Александра', 'is_man': False},
    {'name': 'Радмила', 'is_man': False}, {'name': 'Игнат', 'is_man': True}, {'name': 'Снежана', 'is_man': False},
    {'name': 'Эльвира', 'is_man': False}, {'name': 'Ефим', 'is_man': True}, {'name': 'Ника', 'is_man': False},
    {'name': 'Юстина', 'is_man': False}, {'name': 'Анфиса', 'is_man': False}, {'name': 'Майя', 'is_man': False},
    {'name': 'Валерий', 'is_man': True}, {'name': 'Валентин', 'is_man': True}, {'name': 'Виктор', 'is_man': True},
    {'name': 'Аркадий', 'is_man': True}, {'name': 'Борис', 'is_man': True}, {'name': 'Клавдия', 'is_man': False},
    {'name': 'Спиридон', 'is_man': True}, {'name': 'Игнатий', 'is_man': True}, {'name': 'Эмиль', 'is_man': True},
    {'name': 'Фаддей', 'is_man': True}, {'name': 'Тихон', 'is_man': True}, {'name': 'Григорий', 'is_man': True},
    {'name': 'Геннадий', 'is_man': True}, {'name': 'Ириней', 'is_man': True}, {'name': 'Владислав', 'is_man': True},
    {'name': 'Артем', 'is_man': True}, {'name': 'Римма', 'is_man': False}, {'name': 'Раиса', 'is_man': False},
    {'name': 'Юрий', 'is_man': True}, {'name': 'Георгий', 'is_man': True}, {'name': 'Дарина', 'is_man': False},
    {'name': 'Наталья', 'is_man': False}, {'name': 'Екатерина', 'is_man': False}, {'name': 'Ирина', 'is_man': False},
    {'name': 'Тамара', 'is_man': False}, {'name': 'Анастасия', 'is_man': False}, {'name': 'Василий', 'is_man': True},
    {'name': 'Лариса', 'is_man': False}, {'name': 'Светлана', 'is_man': False}, {'name': 'Алексей', 'is_man': True},
    {'name': 'Илья', 'is_man': True}, {'name': 'Марина', 'is_man': False}, {'name': 'Анатолий', 'is_man': True},
    {'name': 'Маргарита', 'is_man': False}, {'name': 'Дмитрий', 'is_man': True}, {'name': 'Ирина', 'is_man': False},
    {'name': 'Ева', 'is_man': False}, {'name': 'Софья', 'is_man': False}, {'name': 'Людмила', 'is_man': False},
    {'name': 'Игнат', 'is_man': True}, {'name': 'Александра', 'is_man': False}, {'name': 'Михаил', 'is_man': True},
    {'name': 'Лев', 'is_man': True}, {'name': 'Эльмира', 'is_man': False}, {'name': 'Игнат', 'is_man': True},
    {'name': 'Игнатий', 'is_man': True}, {'name': 'Инесса', 'is_man': False}, {'name': 'Евгений', 'is_man': True},
    {'name': 'Эльмира', 'is_man': False}, {'name': 'Антон', 'is_man': True}, {'name': 'Анастасия', 'is_man': False},
    {'name': 'Анатолий', 'is_man': True}, {'name': 'Надежда', 'is_man': False}, {'name': 'Игнатий', 'is_man': True},
    {'name': 'Стефания', 'is_man': False}, {'name': 'Серафим', 'is_man': True}, {'name': 'Варвара', 'is_man': False},
    {'name': 'Юрий', 'is_man': True}, {'name': 'Филипп', 'is_man': True}, {'name': 'Алла', 'is_man': False},
    {'name': 'Кирилл', 'is_man': True}, {'name': 'Влад', 'is_man': True}, {'name': 'Иван', 'is_man': True},
    {'name': 'Евгения', 'is_man': False}, {'name': 'Никита', 'is_man': True}, {'name': 'Анастасия', 'is_man': False},
    {'name': 'Елена', 'is_man': False}, {'name': 'Роман', 'is_man': True}, {'name': 'Арсений', 'is_man': True},
    {'name': 'Олег', 'is_man': True}, {'name': 'Ирина', 'is_man': False}, {'name': 'Артем', 'is_man': True},
    {'name': 'Наталья', 'is_man': False}, {'name': 'Таисия', 'is_man': False}, {'name': 'Марина', 'is_man': False},
    {'name': 'Игнатий', 'is_man': True}, {'name': 'Лариса', 'is_man': False}, {'name': 'Инга', 'is_man': False},
    {'name': 'Филипп', 'is_man': True}, {'name': 'Алла', 'is_man': False}, {'name': 'Кирилл', 'is_man': True},
    {'name': 'Таисия', 'is_man': False}, {'name': 'Влад', 'is_man': True}, {'name': 'Алиса', 'is_man': False},
    {'name': 'Иван', 'is_man': True}, {'name': 'Дарина', 'is_man': False}, {'name': 'Игнат', 'is_man': True},
    {'name': 'Рената', 'is_man': False}, {'name': 'Никита', 'is_man': True}, {'name': 'Ева', 'is_man': False},
    {'name': 'Дмитрий', 'is_man': True}, {'name': 'Маргарита', 'is_man': False}, {'name': 'Светлана', 'is_man': False},
    {'name': 'Александр', 'is_man': True}, {'name': 'Евгения', 'is_man': False}, {'name': 'Артемий', 'is_man': True},
    {'name': 'Ева', 'is_man': False}, {'name': 'Инесса', 'is_man': False}, {'name': 'Василий', 'is_man': True},
    {'name': 'Карина', 'is_man': False}, {'name': 'Антон', 'is_man': True}, {'name': 'Марина', 'is_man': False},
    {'name': 'Игнат', 'is_man': True}, {'name': 'Виктория', 'is_man': False}, {'name': 'Николай', 'is_man': True},
    {'name': 'Елена', 'is_man': False}, {'name': 'Ксения', 'is_man': False}, {'name': 'Игнат', 'is_man': True},
    {'name': 'Владимир', 'is_man': True}, {'name': 'Марина', 'is_man': False}, {'name': 'Иван', 'is_man': True},
    {'name': 'Дарина', 'is_man': False}, {'name': 'Артем', 'is_man': True}, {'name': 'Анастасия', 'is_man': False},
    {'name': 'Анатолий', 'is_man': True}, {'name': 'Лилия', 'is_man': False}, {'name': 'Антон', 'is_man': True},
    {'name': 'Ксения', 'is_man': False}, {'name': 'Дмитрий', 'is_man': True}, {'name': 'Светлана', 'is_man': False},
    {'name': 'Нина', 'is_man': False}, {'name': 'Владислав', 'is_man': True}, {'name': 'Ольга', 'is_man': False},
    {'name': 'Артур', 'is_man': True}, {'name': 'Ирина', 'is_man': False}, {'name': 'Даниил', 'is_man': True},
    {'name': 'Роза', 'is_man': False}, {'name': 'Андрей', 'is_man': True}, {'name': 'Ева', 'is_man': False},
    {'name': 'Алексей', 'is_man': True}, {'name': 'Лариса', 'is_man': False}, {'name': 'Артемий', 'is_man': True},
    {'name': 'Таисия', 'is_man': False}, {'name': 'Игорь', 'is_man': True}, {'name': 'Анастасия', 'is_man': False},
    {'name': 'Артем', 'is_man': True}, {'name': 'Софья', 'is_man': False}, {'name': 'Александра', 'is_man': False},
    {'name': 'Дмитрий', 'is_man': True}, {'name': 'Ирина', 'is_man': False}, {'name': 'Николай', 'is_man': True},
    {'name': 'Маргарита', 'is_man': False}, {'name': 'Сергей', 'is_man': True}, {'name': 'Людмила', 'is_man': False},
    {'name': 'Павел', 'is_man': True}, {'name': 'Марина', 'is_man': False}, {'name': 'Анна', 'is_man': False},
    {'name': 'Александр', 'is_man': True}, {'name': 'Таисия', 'is_man': False}, {'name': 'Артем', 'is_man': True},
    {'name': 'Алеся', 'is_man': False}, {'name': 'Даниил', 'is_man': True}, {'name': 'Александра', 'is_man': False},
    {'name': 'Игорь', 'is_man': True}, {'name': 'Татьяна', 'is_man': False}, {'name': 'Никита', 'is_man': True},
    {'name': 'Анастасия', 'is_man': False}, {'name': 'Максим', 'is_man': True}, {'name': 'Елена', 'is_man': False},
    {'name': 'Роман', 'is_man': True}, {'name': 'Карина', 'is_man': False}, {'name': 'Сергей', 'is_man': True},
    {'name': 'Валентина', 'is_man': False}, {'name': 'Дмитрий', 'is_man': True}, {'name': 'Людмила', 'is_man': False},
    {'name': 'Александр', 'is_man': True}, {'name': 'Ирина', 'is_man': False}, {'name': 'Игорь', 'is_man': True},
    {'name': 'Татьяна', 'is_man': False}, {'name': 'Дмитрий', 'is_man': True}, {'name': 'Маргарита', 'is_man': False},
    {'name': 'Артем', 'is_man': True}, {'name': 'Светлана', 'is_man': False}, {'name': 'Алексей', 'is_man': True},
    {'name': 'Евгения', 'is_man': False}, {'name': 'Андрей', 'is_man': True}, {'name': 'Ксения', 'is_man': False},
    {'name': 'Илья', 'is_man': True}, {'name': 'Алена', 'is_man': False}, {'name': 'Анатолий', 'is_man': True},
    {'name': 'Лилия', 'is_man': False}, {'name': 'Андрей', 'is_man': True}, {'name': 'Елена', 'is_man': False},
    {'name': 'Николай', 'is_man': True}, {'name': 'Маргарита', 'is_man': False}, {'name': 'Дмитрий', 'is_man': True},
    {'name': 'Светлана', 'is_man': False}, {'name': 'Павел', 'is_man': True}, {'name': 'Екатерина', 'is_man': False},
    {'name': 'Игорь', 'is_man': True}, {'name': 'Таисия', 'is_man': False}, {'name': 'Артем', 'is_man': True},
    {'name': 'Ева', 'is_man': False}
]
    return random.choice(names)