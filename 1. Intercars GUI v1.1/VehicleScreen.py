from kivy.uix.screenmanager import Screen, ScreenManager


class VehicleScreen(Screen):
    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name
