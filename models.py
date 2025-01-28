from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex


class RoundedButton(ButtonBehavior, Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.padding = [20, 10]
        self.font_size = "16sp"
        self.size_hint = (None, None)
        self.size = (240, 60)
        self.halign = "center"
        self.valign = "middle"
        self.color = get_color_from_hex("#ffffff")
        with self.canvas.before:
            Color(*get_color_from_hex("#444444"))
            self.rect = RoundedRectangle(radius=[30], size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class MushroomCard(BoxLayout):
    def __init__(self, name, date, image_path, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.spacing = 15
        self.padding = [10, 5]
        self.size_hint_y = None
        self.height = 100

        # Изображение гриба
        img = Image(
            source=image_path, size_hint=(None, 1), width=80, allow_stretch=True
        )
        self.add_widget(img)

        # Текстовая информация
        text_box = BoxLayout(orientation="vertical")
        text_box.add_widget(
            Label(text=name, font_size="16sp", halign="left", bold=True)
        )
        text_box.add_widget(
            Label(text=date, font_size="12sp", color=get_color_from_hex("#666666"))
        )
        self.add_widget(text_box)

        # Кнопка удаления
        btn_delete = Button(
            text="×",
            font_size="24sp",
            size_hint=(None, None),
            size=(50, 50),
            color=get_color_from_hex("#ff0000"),
            background_color=(0, 0, 0, 0),
        )
        btn_delete.bind(on_release=lambda x: self.delete_card())
        self.add_widget(btn_delete)

    def delete_card(self):
        # Метод для удаления карточки
        self.parent.remove_widget(self)
