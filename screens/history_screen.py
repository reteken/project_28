from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
from models import MushroomCard
from database import get_mushrooms


class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main_layout = AnchorLayout(anchor_x="center", anchor_y="top")

        scroll_container = BoxLayout(orientation="vertical", size_hint=(0.95, 0.95))

        scroll_view = ScrollView()
        self.scroll_layout = BoxLayout(
            orientation="vertical", size_hint_y=None, spacing=10
        )
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter("height"))

        mushrooms = get_mushrooms()
        for mushroom in mushrooms:
            card = MushroomCard(mushroom[1], mushroom[2], mushroom[3])
            self.scroll_layout.add_widget(card)

        scroll_view.add_widget(self.scroll_layout)
        scroll_container.add_widget(scroll_view)
        main_layout.add_widget(scroll_container)
        self.add_widget(main_layout)
