from data_access.data_access_db import load_collection
from models.Temperature import Temperature


def get_loads_per_month_service():
    load_data = load_collection.find_one({"index": "load"})
    months = {
        2018: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2019: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2020: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2021: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    cnt = {
        2018: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2019: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2020: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2021: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }

    for item in load_data['data']:
        year = int(item['Time Stamp'].split('/')[2].split(' ')[0])
        month_index = int(item['Time Stamp'].split('/')[0]) - 1
        months[year][month_index] += item['Load']
        cnt[year][month_index] += 1

    y = {}
    for year in months.keys():
        y[year] = []
        for i in range(12):
            if cnt[year][i] != 0:
                y[year].append(months[year][i] / cnt[year][i])

    return Temperature(y[2018], y[2019], y[2020], y[2021])
