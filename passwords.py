import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
filthy = ['хуй', 'пидорас', 'уебище', 'гниль', 'сын_шлюхи', 'сын_говна', 'хуесос']
chars = ''


def generate_password(lenght, chars):
    psw = ''
    for _ in range(lenght):
        psw += random.choice(chars)
    return psw + random.choice(filthy)


cntPw = int(input('Количество паролей: '))
lenPw = int(input('Длина пароля: '))
digOn = input('Включить цифры: (y/n)')
abc_up = input('Прописные буквы: (y/n)')
abc_lo = input('Строчные буквы: (y/n)')
sp = input('Специальные символы: (y/n)')
fil = input('Включить русские маты: (y/n)')
exc = input('Исключить неоднозначные символы il1Lo0O: (y/n)')


if digOn == 'y':
    chars += digits
if abc_up == 'y':
    chars += uppercase_letters
if abc_lo == 'y':
    chars += lowercase_letters
if sp == 'y':
    chars += punctuation
if fil != 'y':
    filthy = ['', '']
if exc == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')


for i in range(cntPw):
    print(generate_password(lenPw, chars))
