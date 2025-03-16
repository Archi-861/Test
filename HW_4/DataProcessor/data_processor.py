import json

class DataProcessor:
    """Класс для чтения и обработки JSON-файлов"""

    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        """Читает JSON-файл и возвращает данные"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_value(self, key):
        """Получает значение по ключу из JSON"""
        data = self.load_data()
        return data.get(key, None)