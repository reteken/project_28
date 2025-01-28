from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from models import RoundedButton

Builder.load_string(
    """
<MainMenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        RoundedButton:
            text: "Сканировать гриб"
            size_hint: (1, 0.2)
            on_release: root.go_to_camera()

        RoundedButton:
            text: "История"
            size_hint: (1, 0.2)
            on_release: root.go_to_history()

        RoundedButton:
            text: "Настройки"
            size_hint: (1, 0.2)
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
