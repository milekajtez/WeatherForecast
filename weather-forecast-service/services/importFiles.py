import os

TRAINING_DATA = './Training Data'


class ImportFiles:
    @staticmethod
    def loadNamesOfAllCSVFiles():
        result = []
        for path, dirs, files in os.walk(TRAINING_DATA):
            for f in files:
                result.append(f)

        return result
