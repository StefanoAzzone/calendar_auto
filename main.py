import os
import pandas

from ics import Calendar, Event


def populate_file(calendar_name):
    calendar_folder = 'C:\\Users\\user\\Downloads\\stefanoazzone98@gmail.com.ical\\'
    matches = [elem for elem in os.listdir(calendar_folder) if elem.startswith(calendar_name) and
               elem.endswith('.ics')]
    assert len(matches) == 1
    calendar_file_name = matches[0]
    with open(calendar_folder + calendar_name + '_out.csv', 'w') as out_file:
        with open(calendar_folder + calendar_file_name, 'r') as calendar_file:
            cal = Calendar(calendar_file.read())
            out_file.write(f'EVENT, DURATION\n')
            for event in cal.events:
                out_file.write(f'{event.name}, {event.duration.seconds/3600}\n')

    df = pandas.read_csv(calendar_folder + calendar_name + '_out.csv')

    df = df.sort_values('EVENT')

    df = df.groupby(['EVENT']).sum()
    print(df)



if __name__ == '__main__':

    populate_file("Ferrero")



