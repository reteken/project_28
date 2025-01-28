from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import (
    AnchorLayout,
)  # Главный контейнер с выравниванием по центру
from kivy.uix.label import Label
from models import RoundedButton
from database import save_mushroom


class AnalysisScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = AnchorLayout(anchor_x="center", anchor_y="center")

        content = BoxLayout(
            orientation="vertical", padding=20, spacing=20, size_hint=(0.9, 0.9)
        )

        self.result_label = Label(
            text="Результат анализа...", font_size="16sp", halign="center"
        )
        content.add_widget(self.result_label)

        button_box = BoxLayout(size_hint=(1, None), height=120, spacing=10)

        save_button = RoundedButton(text="Сохранить фото")
        save_button.bind(on_press=self.save_photo)

        back_button = RoundedButton(text="Назад")
        back_button.bind(on_press=self.go_back_to_camera)

        button_box.add_widget(save_button)
        button_box.add_widget(back_button)

        content.add_widget(button_box)
        main_layout.add_widget(content)
        self.add_widget(main_layout)

    def save_photo(self, instance):
        save_mushroom("Гриб", "path_to_image")
        self.manager.current = "main_menu"

    def go_back_to_camera(self, instance):
        self.manager.current = "camera"
