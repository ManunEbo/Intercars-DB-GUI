from kivy.uix.screenmanager import Screen, ScreenManager


class Cust_AddressScreen(Screen):

    # def customer_address(self):
    #     self.manager.current = "deposit_or_sale"

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name
