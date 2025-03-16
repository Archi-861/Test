
class Logger:
    """Простой логгер, который записывает сообщения в файл"""

    def __init__(self, file_path):
        self.file_path = file_path

    def log(self, message):
        """Записывает сообщение в файл"""
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(message + "\n")

    def get_logs(self):
        """Читает все сообщения из файла"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.readlines()