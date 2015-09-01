import csv
import os
import json
import shutil

mapping = dict()

for l in ('NL', 'EN'):
    for i in range(13):
        dirname = l + str(i + 1)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        mapping[dirname] = i + 30 + (13 * 1 if l == 'EN' else 0)

with open('results-survey759455.csv') as f:
    reader = csv.reader(f, delimiter=',')
    next(reader)  # skip header row
    for row in reader:
        participant_id = row[0]
        for k, v in mapping.items():
            result = json.loads(row[v])
            result_name = result[0].get('filename')
            result_file = 'data/' + result_name
            new_file = k + '/' + participant_id + '.wav'
            if os.path.isfile(result_file):
                shutil.copyfile(result_file, new_file)
            else:
                print "File not found!"
