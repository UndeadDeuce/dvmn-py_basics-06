def has_digit(password):
    return any(ch.isdigit() for ch in password)


def is_very_long(password):
    return len(password) > 12


def has_upper_letters(password):
    return any(ch.isupper() for ch in password)


def has_lower_letters(password):
    return any(ch.islower() for ch in password)


def has_symbols(password):
    special_symbols = ['!', '@', '#', '$', '%', '&']
    return any(ch in special_symbols for ch in password)


my_pass = input()
score = 0

checks = [
    is_very_long,
    has_digit,
    has_upper_letters,
    has_lower_letters,
    has_symbols,
]

for check in checks:
    if check(my_pass):
        score += 2

print('Рейтинг пароля:', score)
