import json

data = {'tests': [{'id': 2, 'title': 'Smoke test', 'value': ''}, {'id': 41, 'title': 'Debug test', 'value': ''}, {'id': 73, 'title': 'Performance test', 'value': '', 'values': [{'id': 345, 'title': 'Maxperf', 'value': '', 'values': [{'id': 230, 'title': 'Percent', 'values': [{'id': 234, 'title': '200', 'value': ''}, {'id': 653, 'title': '300', 'value': ''}]}]}, {'id': 110, 'title': 'Stability test', 'value': '', 'values': [{'id': 261, 'title': 'Percent', 'values': [{'id': 238, 'title': '160', 'value': ''}, {'id': 690, 'title': '240', 'value': ''}]}]}]}, {'id': 122, 'title': 'Security test', 'value': '', 'values': [{'id': 5321, 'title': 'Confidentiality', 'value': ''}, {'id': 5322, 'title': 'Integrity', 'value': ''}]}}]
with open('tests.json') as file1:
    file1.read()

data['values'] += list(json_data)

with open('values.json') as file2:
    file2.read()

def add_to_json():
    json_data = {
        'values': [{
            'id': 2,
            'value': 'passed'
        }, {
            'id': 41,
            'value': 'passed'
        }, {
            'id': 73,
            'value': 'passed'
        }, {
            'id': 110,
            'value': 'failed'
        }, {
            'id': 122,
            'value': 'failed'
        }, {
            'id': 234,
            'value': 'passed'
        }, {
            'id': 238,
            'value': 'passed'
        }, {
            'id': 345,
            'value': 'passed'
        }, {
            'id': 653,
            'value': 'passed'
        }, {
            'id': 690,
            'value': 'failed'
        }, {
            'id': 5321,
            'value': 'passed'
        }, {
            'id': 5322,
            'value': 'failed'
        }]
    }

data.append(json_data)
data = json.load(open('report.json'))

add_to_json()
