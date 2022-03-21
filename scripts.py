import random
from datacenter.models import (
    Chastisement,
    Commendation,
    Lesson,
    Mark,
    Schoolkid,
    Subject
)


def get_schoolkid(schoolkid_name: str) -> Schoolkid:
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
    except Schoolkid.DoesNotExist:
        print('Неверно введено имя ученика')
        exit(1)
    except Schoolkid.MultipleObjectsReturned:
        print(
            'Найдено несколько учеников с таким именем. '
            'Введите полное имя ученика'
        )
        exit(1)
    return schoolkid


def fix_marks(schoolkid_name: str) -> None:
    schoolkid = get_schoolkid(schoolkid_name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid).filter(
        points__range=(2, 3)
    )
    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid_name: str) -> None:
    schoolkid = get_schoolkid(schoolkid_name)
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(schoolkid_name: str, subject: str) -> None:
    schoolkid = get_schoolkid(schoolkid_name)
    try:
        Subject.objects.get(
            title=subject,
            year_of_study=schoolkid.year_of_study
        )
    except Subject.DoesNotExist:
        print('Неверно введено название предмета')
        exit(1)
    lessons = Lesson.objects.filter(
        subject__title=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    )
    commendation_texts = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]
    lesson = random.choice(lessons)
    while Commendation.objects.filter(
        created=lesson.date,
        subject=lesson.subject
    ):
        lesson = random.choice(lessons)
    Commendation.objects.create(
        text=random.choice(commendation_texts),
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )
