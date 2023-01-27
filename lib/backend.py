import os

import pandas
from ics import Calendar, Event
from datetime import datetime


def populate_file(calendar_folder, calendar_name):
    matches = [elem for elem in os.listdir(calendar_folder) if elem.startswith(calendar_name) and
               elem.endswith('.ics')]
    assert len(matches) <= 1
    if len(matches) == 0:
        print(f"Calendar not found: {calendar_name}")
        return
    calendar_file_name = matches[0]
    with open(calendar_folder + calendar_name + '_out.csv', 'w') as out_file:
        with open(calendar_folder + calendar_file_name, 'r') as calendar_file:
            cal = Calendar(calendar_file.read())
            out_file.write(f'EVENT, DURATION\n')
            for event in cal.events:
                out_file.write(f'{event.name}, {event.duration.seconds/3600}\n')

    df = pandas.read_csv(calendar_folder + calendar_name + '_out.csv')

    df['CODE'] = df['EVENT'].str[0:3]

    df = df.sort_values('EVENT')

    df = df.drop('EVENT', axis=1)
    print(df)

    df = df.groupby(['CODE']).sum()
    print(df)


def map_calendar_name_to_path(calendar_folder, calendar_names):
    calendar_paths = os.listdir(calendar_folder)
    calendar_map = {}
    for name in calendar_names:
        for path in calendar_paths:
            if path.startswith(name) and path.endswith('.ics'):
                calendar_map[name] = f'{calendar_folder}/{path}'

    return calendar_map


def get_hour_per_day_map(path, num_days):
    hour_per_day_map = {}
    for day in range(1, num_days + 1):
        hour_per_day_map[day] = 0

    with open(path, 'r') as calendar_file:
        cal = Calendar(calendar_file.read())
        for event in cal.events:
            begin = event.begin
            day = int(begin.format('D'))
            duration = event.duration
            hour_per_day_map[day] = hour_per_day_map[day] + duration.seconds / 3600

    print(hour_per_day_map)
    return hour_per_day_map


def get_week_beginning_and_end(week):
    beginning = -1
    end = -1
    i = 0
    for day in week:
        if day != 0:
            beginning = day
            break

    counter = -1
    while True:
        if week[counter] != 0:
            end = week[counter]
            break
        counter = counter - 1

    return beginning, end


def print_calendar_week_map(calendar_week_map, weeks):
    header = "Company,"
    for week in weeks:
        beginning, end = get_week_beginning_and_end(week)
        header = header + f'{beginning}-{end},'
    print(header[:-1])
    for name, week_map in calendar_week_map.items():
        row = name
        for i, hours in week_map.items():
            row = row + ',' + str(hours)
        print(row)




