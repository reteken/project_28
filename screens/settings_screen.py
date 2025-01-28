from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from models import RoundedButton
from theme_manager import theme_manager

Builder.load_string(
    """
<SettingsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        canvas.before:
            Color:
                rgba: app.theme.get("background_color")
            Rectangle:
                pos: self.pos
                size: self.size

        RoundedButton:
            text: "Переключить тему"
            background_color: app.theme.get("button_color")
            color: app.theme.get("text_color")
            on_release: root.toggle_theme()

        RoundedButton:
            text: "Назад"
            background_color: app.theme.get("button_color")
            color: app.theme.get("text_color")
            on_release: root.manager.current = 'main_menu'
    """
)


class SettingsScreen(Screen):
    def toggle_theme(self):
        # Переключение темы
        theme_manager.toggle_theme()
        # Обновляем все экраны
        for screen in self.manager.screens:
            if hasattr(screen, "update_theme"):
                screen.update_theme()

    def update_theme(self):
        self.canvas.ask_update()
