import os
import sys
from calendar import Calendar
from os.path import expanduser

from lib.backend import map_calendar_name_to_path, get_hour_per_day_map, print_calendar_week_map, \
    get_hour_per_project_map, print_calendar_project_map
from lib.configuration import parse_args, load_config

if __name__ == '__main__':
    home = expanduser("~")
    config_folder = os.path.join(home, '.calendar_auto')

    # creds = authenticate(config_folder)

    calendar_names = [x.split('_')[0] for x in os.listdir(os.path.join(config_folder, "calendars"))]
    calendar_names.remove('stefanoazzone98@gmail.com.ics')

    config = load_config(os.path.join(config_folder, 'config.yaml'))

    calendar_folder = os.path.join(config_folder, 'calendars')

    args = parse_args()
    year = int(args.year)
    month = int(args.month)
    scope = args.scope

    cal = Calendar()
    weeks = cal.monthdayscalendar(year=year, month=month)
    name_to_file_map = map_calendar_name_to_path(calendar_folder, calendar_names)

    calendar_day_map = {}
    for name, path in name_to_file_map.items():
        calendar_day_map[name] = get_hour_per_day_map(path, year, month)

    calendar_project_map = {}
    for name, path in name_to_file_map.items():
        calendar_project_map[name] = get_hour_per_project_map(path, year, month)

    print(calendar_project_map)

    calendar_week_map = {}
    for name in calendar_names:
        hour_per_week_map = {}
        for i, week in enumerate(weeks):
            hour_per_week_map[i] = 0
            for day in week:
                if day != 0:
                    hour_per_week_map[i] = hour_per_week_map[i] + calendar_day_map[name][day]

        calendar_week_map[name] = hour_per_week_map

    print_calendar_week_map(calendar_week_map, weeks, scope)
    print_calendar_project_map(calendar_project_map)





