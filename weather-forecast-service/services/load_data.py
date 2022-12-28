from data_access.data_access_db import get_load


class LoadData:
    @staticmethod
    def loadDataForDisplay(index):
        data_from_db = get_load({"index": index})
        return data_from_db['data']

