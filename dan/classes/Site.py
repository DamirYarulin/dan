class Site:
    def __init__(self):
        self.db = False  # Объект подключения к БД
        self.request = False   # request aiohttp
        # self.request.method = 'GET' / 'POST' / 'PUT' - метод передачи данных
        self.post = False  # объект post
        self.path = ''  # Путь
        self.p = ''  # Список элементов пути
        self.head = ''  # Материал выводимыей в внутри тега шаблона <head>
        self.tag_title = ''  # Тег title
        self.tag_description = ''  # Метатег descripton
        self.content = ''  # Основное содержимое
        self.modules = {}  # Словарь модуле
        self.salt = 'DAN_core_salt'  # Соль
        self.settings = ''  # Словарь настроек сайта
        self.headFile = []  # Файлы для вывода в шапке шаблона

    def addHeadFile(self, path):
        # Добавляет файлы для вывода в шапке шаблона
        if path in self.headFile:
            return
        self.headFile.append(path)

    def getHead(self):
        out = ''
        for file in self.headFile:
            file_list = file.split('.')
            if file_list[-1] == 'js':
                out += '<script src="' + file + '"></script>'
            if file_list[-1] == 'css':
                out += '<link rel="stylesheet" href="' + file + '" />'
        print(out)
        return out
