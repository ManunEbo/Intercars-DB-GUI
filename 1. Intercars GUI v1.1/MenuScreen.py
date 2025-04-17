from kivy.uix.screenmanager import Screen, ScreenManager


class MenuScreen(Screen):
    # def auction_menu(self):
    #     self.manager.current = "auction_menu_screen"

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name
