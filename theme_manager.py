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

    def get(self, key):
        return self.themes[self.current_theme][key]

    def toggle_theme(self):
        self.current_theme = "light" if self.current_theme == "dark" else "dark"


theme_manager = ThemeManager()
