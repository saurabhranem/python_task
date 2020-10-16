import csv
import collections
from collections import Counter

def read_csv(file_name):
    csv_list = []
    with open(file_name, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            csv_list.append(dict(row))
    return csv_list


def logic_fun(file_name):
    csv_list = read_csv(file_name)
    data = {}
    average={}
    for item in csv_list:
        if item['subject'] in data.keys():
            marks = int(data[item['subject']]) + int(item['marks'])
            data.update({item['subject'] : marks})
        else:
            data.update({item['subject'] : item['marks']})
    subjects = Counter(k['subject'] for k in csv_list if k.get('subject'))
    for subject, count in subjects.most_common():
        average.update({subject: data[subject]//count})
    return {'average':average}


file_name = '/Users/saurabhrane/Documents/students.csv'
data = logic_fun(file_name)
print(data)