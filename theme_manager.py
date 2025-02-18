class ThemeManager:
    def __init__(self):
        self.current_theme = "dark"  # По умолчанию — тёмная тема
        self.themes = {
            "dark": {
                "background_color": [0.1, 0.1, 0.1, 1],
                "button_color": [0.2, 0.2, 0.2, 1],
                "text_color": [1, 1, 1, 1],
            },
            "light": {
                "background_color": [1, 1, 1, 1],
                "button_color": [0.9, 0.9, 0.9, 1],
                "text_color": [0, 0, 0, 1],
            },
        }
        self.observers = set()

    def get(self, key):
        return self.themes[self.current_theme][key]

    def toggle_theme(self):
        """Переключение темы с уведомлением всех подписчиков."""
        self.current_theme = "light" if self.current_theme == "dark" else "dark"
        for callback in list(self.observers):
            callback()

    def subscribe(self, callback):
        """Подписка на изменения темы."""
        self.observers.add(callback)

    def auto_toggle_on_start(self):
        """Автоматическое переключение темы при запуске."""
        self.toggle_theme()  # Меняем тему один раз при запуске


theme_manager = ThemeManager()
