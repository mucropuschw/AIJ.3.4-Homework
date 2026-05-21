import json
from pathlib import Path
import unittest

from leap_year import is_leap_year, is_valid_year

GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
YELLOW = '\033[93m'

DATA_FILE = Path(__file__).with_name('leap_year_test_data.json')


class TestLeapYear(unittest.TestCase):
    def test_leap_year_cases(self):
        with DATA_FILE.open('r', encoding='utf-8') as f:
            cases = json.load(f)

        passed = 0
        failed = 0

        for case in cases:
            case_id = case.get('id')
            year = case['year']
            description = case.get('description', '')
            is_valid = case.get('check_valid', case.get('valid', True))

            with self.subTest(id=case_id, year=year, description=description):
                try:
                    if is_valid:
                        expected = case['expected']
                        actual = is_leap_year(year)
                        success = actual == expected

                        if success:
                            if description:
                                print(f'{GREEN}PASS{RESET}: {year} ({description})')
                            else:
                                print(f'{GREEN}PASS{RESET}: {year}')
                            passed += 1
                        else:
                            if description:
                                print(f'{RED}FAIL{RESET}: {year} ({description})')
                            else:
                                print(f'{RED}FAIL{RESET}: {year}')
                            failed += 1

                        self.assertEqual(actual, expected)
                    else:
                        self.assertFalse(is_valid_year(year))
                        with self.assertRaises(ValueError):
                            is_leap_year(year)
                        if description:
                            print(f'{RED}FAIL{RESET}: {year} ({description})')
                        else:
                            print(f'{RED}FAIL{RESET}: {year}')
                        passed += 1
                except Exception:
                    failed += 1
                    raise

        total = len(cases)
        print(f'\n{YELLOW}Summary:{RESET}')
        print(f'Total cases: {total}')
        print(f'Passed: {passed}')
        print(f'Failed: {failed}')


if __name__ == '__main__':
    unittest.main(verbosity=2)
