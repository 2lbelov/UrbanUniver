def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if '@' not in sender or (sender[-4:len(sender)] != '.com' and sender[-4:len(sender)] != '.net' and sender[-3:len(sender)] != '.ru'):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif '@' not in recipient or (recipient[-4:len(recipient)] != '.com' and recipient[-4:len(recipient)] != '.net' and recipient[-3:len(recipient)] != '.ru'):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

