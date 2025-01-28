from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from models import MushroomCard
from database import get_mushrooms
from theme_manager import theme_manager

Builder.load_string(
    """
<HistoryScreen>:
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

        ScrollView:
            BoxLayout:
                id: history_container
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
    """
)


class HistoryScreen(Screen):
    def on_enter(self):
        self.load_history()

    def load_history(self):
        history_container = self.ids.history_container
        history_container.clear_widgets()

        for mushroom in get_mushrooms():
            card = MushroomCard(
                name=mushroom[1],
                date=mushroom[2],
                image_path=mushroom[3],
                size_hint=(1, None),
                height=dp(100),
            )
            history_container.add_widget(card)

    def update_theme(self):
        self.canvas.ask_update()
