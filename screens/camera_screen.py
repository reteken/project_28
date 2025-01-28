from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy_garden.xcamera import XCamera
from kivy.properties import ColorProperty, StringProperty, NumericProperty
from kivy.uix.button import Button
from kivy.metrics import dp
from datetime import datetime
import os
import cv2
from ultralytics import YOLO

Builder.load_string(
    """
#:import xcamera kivy_garden.xcamera.xcamera

<CameraIconButton>:
    background_color: (0, 0, 0, 0)
    color: self.icon_color
    markup: True
    font_size: self.icon_size * 0.7
    size_hint: (None, None)
    size: (self.icon_size, self.icon_size)
    canvas.before:
        Color:
            rgba: self.background_color
        Ellipse:
            pos: self.pos
            size: self.size

<XCameraScreen>:
    xcamera: xcamera
    BoxLayout:
        orientation: 'vertical'
        XCamera:
            id: xcamera
            resolution: (640, 480)
            play: True
            fit_mode: 'contain'
            on_picture_taken: root.process_picture(args[1])
        
        BoxLayout:
            size_hint_y: None
            height: dp(100)
            padding: dp(20)
            spacing: dp(20)
            
            CameraIconButton:
                text: root.back_icon
                icon_color: '#ffffff'
                background_color: '#e74c3c'
                icon_size: dp(50)
                on_release: root.manager.current = 'main_menu'
            
            CameraIconButton:
                text: '[font=data/icons.ttf]\\ue800[/font]'
                icon_color: '#0A79DF'
                icon_size: dp(70)
                on_release: xcamera.shoot()
                background_color: (0.13, 0.58, 0.95, 0.5)
"""
)


class CameraIconButton(Button):
    icon_color = ColorProperty("#ffffff")
    icon_size = NumericProperty(dp(50))
    back_icon = StringProperty("[font=data/icons.ttf]\\ue801[/font]")


class XCameraScreen(Screen):
    back_icon = StringProperty(
        "[font=data/icons.ttf]\\ue801[/font]"
    )  # Значок для кнопки назад

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = YOLO("best.pt")
        if not os.path.exists("photos"):
            os.makedirs("photos")

    def process_picture(self, filepath):
        """Обработка файла после съемки."""
        if not filepath or not os.path.exists(filepath):
            print("Файл не найден:", filepath)
            return

        # Переименовать и сохранить файл
        new_filename = os.path.join(
            "photos", f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        os.rename(filepath, new_filename)

        # Использовать YOLO для обработки
        results = self.model.predict(source=new_filename, save=False, save_txt=False)
        result = results[0]
        annotated_frame = result.plot()

        # Сохранить аннотированный файл
        processed_filename = os.path.join(
            "photos", f"processed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        )
        cv2.imwrite(processed_filename, annotated_frame)

        # Обновить экран анализа
        self.manager.current = "analysis"
        self.manager.get_screen("analysis").result_label.text = (
            f"Обнаружен: {result.names[0]}"
        )
