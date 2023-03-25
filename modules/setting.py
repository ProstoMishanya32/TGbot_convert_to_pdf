from modules.creater_config import CreatingConfig


class MainConfig(CreatingConfig):
    def __init__(self) -> None:
        super().__init__(path = 'data/config.json')
        self.bot = self.Bot(config = self)
        self.logs = self.Logs(config = self)
    class Bot:
        def __init__(self, config : CreatingConfig) -> None:
            self.token = config.config_field(key = 'token', layer = 'bot', default = 'Здесь ваш Telegram Токен')
            self.main_front =  config.config_field(key = 'main_front', layer = 'bot', default = 'Основной шрифт')
            self.dict_paragraph = config.config_field(key = 'dict_paragraph', layer = 'bot', default = [])
            self.title = config.config_field(key = 'title', layer = 'bot', default = 'Заголовок')
            self.path_logo  = config.config_field(key = 'path_logo', layer = 'bot', default = 'Логотип.png')
            self.size_logo = config.config_field(key = 'size_logo', layer = 'bot', default = 'Длина логотипа')
    class Logs:
        def __init__(self, config : CreatingConfig) -> None:
            self.main_path_logs = config.config_field(key = 'main_path_logs', layer = 'logs', default = 'Путь к папке логов')
