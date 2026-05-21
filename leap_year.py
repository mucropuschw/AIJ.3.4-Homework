GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'


def is_valid_year(year: int) -> bool:
    return 0 <= year <= 9999


def validate_year(year: int) -> None:
    if not is_valid_year(year):
        raise ValueError('Year must be between 0 and 9999 inclusive')


def is_leap_year(year: int) -> bool:
    validate_year(year)
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def main() -> None:
    try:
        year_input = input('Введите год: ').strip()
        year = int(year_input)
    except ValueError:
        print(f'{RED}Ошибка: введите целое число.{RESET}')
        return

    if year <= 0:
        print(f'{YELLOW}Ошибка: год должен быть положительным числом.{RESET}')
        return

    if is_leap_year(year):
        print(f'{GREEN}{year} — високосный год.{RESET}')
    else:
        print(f'{RED}{year} — не високосный год.{RESET}')


if __name__ == '__main__':
    main()
