from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from database import get_saved_mushrooms  # Функция для получения данных из базы
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle
from theme_manager import theme_manager

Builder.load_string(
    """
<HistoryScreen>:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)
        canvas.before:
            Color:
                rgba: app.theme.get("background_color")
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: "История сканирований"
            size_hint_y: None
            height: dp(40)
            font_size: "20sp"
            halign: "center"
            color: app.theme.get("text_color")

        ScrollView:
            size_hint: (1, 1)
            BoxLayout:
                id: history_list
                orientation: "vertical"
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(10)
    """
)


class HistoryCard(BoxLayout):
    """Карточка для отображения гриба."""

    def __init__(self, name, scan_date, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.size_hint_y = None
        self.height = dp(80)
        self.padding = dp(10)
        self.spacing = dp(5)
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*theme_manager.get("button_color"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(size=self.update_rect, pos=self.update_rect)

        # Добавляем название гриба
        self.add_widget(
            Label(
                text=f"[b]{name}[/b]",
                markup=True,
                size_hint_y=None,
                height=dp(30),
                color=theme_manager.get("text_color"),
                halign="left",
                valign="middle",
                font_size="16sp",
            )
        )
        # Добавляем дату сканирования
        self.add_widget(
            Label(
                text=f"Дата сканирования: {scan_date}",
                size_hint_y=None,
                height=dp(20),
                color=theme_manager.get("text_color"),
                halign="left",
                valign="middle",
                font_size="14sp",
            )
        )

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class HistoryScreen(Screen):
    def on_pre_enter(self):
        """Вызывается перед входом на экран."""
        self.update_history()

    def update_history(self):
        """Обновляет список истории сканирований."""
        history_list = self.ids.history_list
        history_list.clear_widgets()

        # Получаем данные из базы
        mushrooms = get_saved_mushrooms()

        # Заполняем список
        for mushroom in mushrooms:
            name = mushroom["name"]
            scan_date = mushroom["scan_date"]
            history_list.add_widget(HistoryCard(name=name, scan_date=scan_date))
