from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens.main_menu import MainMenuScreen
from screens.camera_screen import XCameraScreen
from screens.analysis_screen import AnalysisScreen
from screens.history_screen import HistoryScreen
from screens.settings_screen import SettingsScreen
from database import init_db
from theme_manager import theme_manager


class DigitalViewApp(App):
    theme = theme_manager

    def build(self):
        init_db()

        self.sm = ScreenManager()
        self.sm.add_widget(MainMenuScreen(name="main_menu"))
        self.sm.add_widget(XCameraScreen(name="camera"))
        self.sm.add_widget(AnalysisScreen(name="analysis"))
        self.sm.add_widget(HistoryScreen(name="history"))
        self.sm.add_widget(SettingsScreen(name="settings"))
        return self.sm


if __name__ == "__main__":
    DigitalViewApp().run()
