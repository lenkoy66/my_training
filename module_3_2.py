def send_email (message, recipient, *, sender = "university.help@gmail.com"):
    result = ""
    domains = ['.com', '.ru', '.net']
    if (('@' not in recipient or '@' not in sender)
        or (recipient[-4:] not in domains and recipient[-3:] not in domains)
        or (sender[-4:] not in domains and sender[-3:] not in domains)):
        result = f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}."
        return result
    if sender == recipient:
        result = "Нельзя отправить письмо самому себе!"
        return result
    if sender == "university.help@gmail.com":
        result = f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}."
    else:
        result = f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}."
    return result

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))

