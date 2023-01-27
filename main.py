import os
from calendar import Calendar, monthrange

from lib.backend import populate_file, map_calendar_name_to_path, get_hour_per_day_map, print_calendar_week_map
from lib.configuration import parse_args, load_config

if __name__ == '__main__':
    config = load_config(f'{os.path.dirname(os.path.realpath(__file__))}\\config\\config.yaml')

    calendar_folder = config["calendar_folder"]
    calendar_names = config["calendar_names"]
    # for calendar_name in ["Avvale", "Ferrero", "Stellantis", "Luxottica", "Eni"]:
    #     populate_file(calendar_folder, calendar_name)

    args = parse_args()
    year = int(args.year)
    month = int(args.month)

    cal = Calendar()
    weeks = cal.monthdayscalendar(year=year, month=month)
    _, num_days = monthrange(year=year, month=month)
    name_to_file_map = map_calendar_name_to_path(calendar_folder, calendar_names)

    calendar_day_map = {}
    for name, path in name_to_file_map.items():
        calendar_day_map[name] = get_hour_per_day_map(path, num_days, year, month)

    calendar_week_map = {}
    for name in calendar_names:
        hour_per_week_map = {}
        for i, week in enumerate(weeks):
            hour_per_week_map[i] = 0
            for day in week:
                if day != 0:
                    hour_per_week_map[i] = hour_per_week_map[i] + calendar_day_map[name][day]

        calendar_week_map[name] = hour_per_week_map

    print_calendar_week_map(calendar_week_map, weeks)





