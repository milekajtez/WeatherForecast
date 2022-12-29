from data_access.data_access_db import get_load
from helpers.help_data import monthIncrement
from models.Temperature import Temperature


class LoadData:
    @staticmethod
    def loadDataForDisplay(index):
        data_from_db = get_load({"index": index})
        return data_from_db['data']

    @staticmethod
    def getTemperaturesAveragePerYear():
        data_from_db = get_load({"index": "weather"})
        avg_2018 = 0
        avg_2019 = 0
        avg_2020 = 0
        avg_2021 = 0
        cnt_2018 = 0
        cnt_2019 = 0
        cnt_2020 = 0
        cnt_2021 = 0

        for item in data_from_db['data']:
            if '2018' in item['datetime']:
                avg_2018 += float(item['temp'])
                cnt_2018 += 1
            elif '2019' in item['datetime']:
                avg_2019 += float(item['temp'])
                cnt_2019 += 1
            elif '2020' in item['datetime']:
                avg_2020 += float(item['temp'])
                cnt_2020 += 1
            elif '2021' in item['datetime']:
                avg_2021 += float(item['temp'])
                cnt_2021 += 1

        return [
            avg_2018 / cnt_2018,
            avg_2019 / cnt_2019,
            avg_2020 / cnt_2020,
            avg_2021 / cnt_2021
        ]

    @staticmethod
    def getNumberOfDaysWithSpecificConditionsPerYear(year):
        data_from_db = get_load({"index": "weather"})

        clear = 0
        partially_cloudy = 0
        overcast = 0
        rain_partially_cloudy = 0
        rain_overcast = 0
        snow_partially_cloudy = 0
        snow_overcast = 0
        every_condition = 0

        for item in data_from_db['data']:
            if year in item['datetime']:
                if item['conditions'] == 'Clear':
                    clear += 1
                elif item['conditions'] == 'Partially cloudy':
                    partially_cloudy += 1
                elif item['conditions'] == 'Overcast':
                    overcast += 1
                elif item['conditions'] == 'Rain, Partially cloudy':
                    rain_partially_cloudy += 1
                elif item['conditions'] == 'Rain, Overcast':
                    rain_overcast += 1
                elif item['conditions'] == 'Snow, Partially cloudy':
                    snow_partially_cloudy += 1
                elif item['conditions'] == 'Snow, Overcast':
                    snow_overcast += 1

                every_condition += 1

        return [
            clear * 100 / every_condition,
            partially_cloudy * 100 / every_condition,
            overcast * 100 / every_condition,
            rain_partially_cloudy * 100 / every_condition,
            rain_overcast * 100 / every_condition,
            snow_partially_cloudy * 100 / every_condition,
            snow_overcast * 100 / every_condition
        ]

    @staticmethod
    def getMonthsTemperature():
        data_from_db = get_load({"index": "weather"})
        months2018 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        months2019 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        months2020 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        months2021 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        cnt2018 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cnt2019 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cnt2020 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cnt2021 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for item in data_from_db['data']:
            if '2018' in item['datetime']:
                obj = monthIncrement(item['datetime'], item['temp'], months2018, cnt2018, '-')
                months2018 = obj.month_array
                cnt2018 = obj.cnt_array
            elif '2019' in item['datetime']:
                obj = monthIncrement(item['datetime'], item['temp'], months2019, cnt2019, '-')
                months2019 = obj.month_array
                cnt2019 = obj.cnt_array
            elif '2020' in item['datetime']:
                obj = monthIncrement(item['datetime'], item['temp'], months2020, cnt2020, '-')
                months2020 = obj.month_array
                cnt2020 = obj.cnt_array
            elif '2021' in item['datetime']:
                obj = monthIncrement(item['datetime'], item['temp'], months2021, cnt2021, '-')
                months2021 = obj.month_array
                cnt2021 = obj.cnt_array

        y2018 = []
        y2019 = []
        y2020 = []
        y2021 = []

        for i in range(0, 12):
            if cnt2018[i] != 0:
                y2018.append(months2018[i] / cnt2018[i])
            if cnt2019[i] != 0:
                y2019.append(months2019[i] / cnt2019[i])
            if cnt2020[i] != 0:
                y2020.append(months2020[i] / cnt2020[i])
            if cnt2021[i] != 0:
                y2021.append(months2021[i] / cnt2021[i])

        return Temperature(y2018, y2019, y2020, y2021)

    @staticmethod
    def getMonthsLoads():
        data_from_db = get_load({"index": "load"})
        months2018 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        months2019 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        months2020 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        months2021 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        cnt2018 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cnt2019 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cnt2020 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        cnt2021 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for item in data_from_db['data']:
            if '2018' in item['Time Stamp']:
                obj = monthIncrement(item['Time Stamp'], item['Load'], months2018, cnt2018, '/')
                months2018 = obj.month_array
                cnt2018 = obj.cnt_array
            elif '2019' in item['Time Stamp']:
                obj = monthIncrement(item['Time Stamp'], item['Load'], months2019, cnt2019, '/')
                months2019 = obj.month_array
                cnt2019 = obj.cnt_array
            elif '2020' in item['Time Stamp']:
                obj = monthIncrement(item['Time Stamp'], item['Load'], months2020, cnt2020, '/')
                months2020 = obj.month_array
                cnt2020 = obj.cnt_array
            elif '2021' in item['Time Stamp']:
                obj = monthIncrement(item['Time Stamp'], item['Load'], months2021, cnt2021, '/')
                months2021 = obj.month_array
                cnt2021 = obj.cnt_array

        y2018 = []
        y2019 = []
        y2020 = []
        y2021 = []

        for i in range(0, 12):
            if cnt2018[i] != 0:
                y2018.append(months2018[i] / cnt2018[i])
            if cnt2019[i] != 0:
                y2019.append(months2019[i] / cnt2019[i])
            if cnt2020[i] != 0:
                y2020.append(months2020[i] / cnt2020[i])
            if cnt2021[i] != 0:
                y2021.append(months2021[i] / cnt2021[i])

        return Temperature(y2018, y2019, y2020, y2021)
