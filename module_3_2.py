def send_email(message,  recipient, sender = "university.help@gmail.com"):
    while 1 > 0:
        #if b not in recipient or sender:
        if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')) \
                or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
            break

        elif recipient == sender:
            print('Нельзя отправить письмо самому себе!')
            break
        elif sender == "university.help@gmail.com":
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            break
        elif sender != "university.help@gmail.com":
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
            break

send_email(input('Введите сообщение'), input('Введите поту получателя'))
