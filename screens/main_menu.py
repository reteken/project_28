from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from models import RoundedButton
from theme_manager import theme_manager

Builder.load_string(
    """
<MainMenuScreen>:
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
            text: "Сканировать гриб"
            background_color: app.theme.get("button_color")
            color: app.theme.get("text_color")
            on_release: root.go_to_camera()

        RoundedButton:
            text: "История"
            background_color: app.theme.get("button_color")
            color: app.theme.get("text_color")
            on_release: root.go_to_history()

        RoundedButton:
            text: "Настройки"
            background_color: app.theme.get("button_color")
            color: app.theme.get("text_color")
            on_release: root.go_to_settings()
    """
)


class MainMenuScreen(Screen):
    def go_to_camera(self):
        self.manager.current = "camera"

    def go_to_history(self):
        self.manager.current = "history"

    def go_to_settings(self):
        self.manager.current = "settings"

    def update_theme(self):
        self.canvas.ask_update()
