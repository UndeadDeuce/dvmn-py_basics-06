SCORE_PER_CHECK = 2
MIN_LENGTH = 12


def has_digit(password: str):
    return any(ch.isdigit() for ch in password)


def is_very_long(password: str):
    return len(password) > MIN_LENGTH


def has_upper_letters(password: str):
    return any(ch.isupper() for ch in password)


def has_lower_letters(password: str):
    return any(ch.islower() for ch in password)


def has_symbols(password: str):
    return any(not ch.isdigit() and not ch.isalpha() for ch in password)


def main() -> None:
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
            score += SCORE_PER_CHECK

    print("Рейтинг пароля: {score}".format(score=score))


if __name__ == "__main__":
    main()
