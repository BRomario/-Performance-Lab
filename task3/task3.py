import json
import sys


def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def fill_report(tests, values_dict):
    for test in tests:
        test_id = test.get('id')
        if test_id in values_dict:
            test['value'] = values_dict[test_id]
        if 'values' in test:
            fill_report(test['values'], values_dict)


def main(values_path, tests_path, report_path):
    values = load_json(values_path)['values']
    tests = load_json(tests_path)['tests']

    values_dict = {item['id']: item['value'] for item in values}

    fill_report(tests, values_dict)

    with open(report_path, 'w') as report_file:
        json.dump({'tests': tests}, report_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("python task3.py values.json tests.json report.json")
        sys.exit(1)

    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]

    main(values_path, tests_path, report_path)

# python task3.py values.json tests.json report.json
