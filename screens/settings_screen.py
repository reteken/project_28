from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from models import RoundedButton

Builder.load_string(
    """
<SettingsScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        RoundedButton:
            text: "Опция 1"
            size_hint: (1, 0.2)
            on_release: print("Опция 1 выбрана")

        RoundedButton:
            text: "Опция 2"
            size_hint: (1, 0.2)
            on_release: print("Опция 2 выбрана")

        RoundedButton:
            text: "Назад"
            size_hint: (1, 0.2)
            on_release: root.manager.current = 'main_menu'
    """
)


class SettingsScreen(Screen):
    pass
