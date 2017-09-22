import sys
import csv

alarms = []

try:
    with open('DDC_Alarming.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            if len(row) != 4:
                continue
            alarm = {'Alarmlistennummer': row[0][5:], 'Alarmnummer': row[1], 'Alarmbezeichnung': row[3]}
            alarms.append(alarm)

    with open('DDC_AlarmGroups.csv') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        count = 0
        for row in reader:
            if len(row) != 4:
                continue
            alarm = alarms[count]
            alarm['System F-Box'] = row[0]
            alarm['Notification Class'] = row[1]
            alarm['F-Box'] = row[2]
            count += 1

    with open('ENG_Alarmliste.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        header = ['Alarmlistennummer', 'Alarmnummer', 'Zugehörige System Alarm F-Box', 'Zugehörige F-Box', 'Notification Class', 'Alarmbezeichnung Lokal']
        writer.writerow(header)
        for alarm in alarms:
            row = [alarm['Alarmlistennummer'], alarm['Alarmnummer'], alarm['System F-Box'], alarm['F-Box'], alarm['Notification Class'], alarm['Alarmbezeichnung']]
            writer.writerow(row)

    print('Alamrlist successfully generated')
    sys.exit(0)
except Exception as e:
    print(e)
    sys.exit(1)
