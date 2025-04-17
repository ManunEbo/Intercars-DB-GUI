import Garages_StatsScreen
import GarageScreen
import Op_VAT_StatsScreen
import Disable_password_Screen
import Password_reset_Screen
import Staff_details_Screen
import CustomerScreen
import Cust_AddressScreen
import Deposit_or_SaleScreen
import Deposit_in_two_Screen
import Deposit_in_one_Screen
import Deposit_in_three_Screen
import Sale_in_one_Screen
import Sale_in_two_Screen
import Sale_in_three_Screen
import Sale_with_Deposit_in_one_Screen
import Sale_with_Deposit_in_two_Screen
import Sale_with_Deposit_in_three_Screen
import Vehicle_StatsScreen
import VehicleScreen
import V5CScreen
import MenuScreen
import MOTHistoryScreen
import MOTRefusalScreen
import ServiceHistoryScreen
import MileageHistoryScreen
import CallLogScreen
import VehicleViewingScreen
import StaffScreen
import Staff_StatsScreen
import VendorScreen
import FundScreen
import ElectricalScreen
import MechanicScreen
import MOT_GarageScreen
import CarwashScreen
import Send_to_ServiceScreen
import Return_from_ServiceScreen
import Invoice_for_ServiceScreen
import Op_Service_ReceiptScreen
import Op_Bank_TransferScreen
import Op_Miscellaneous_ReceiptScreen
import Op_serviceScreen
import OperationScreen
import AuctionScreen
import Auction_invoice_statsScreen
import Auction_invoice
import AuctionMenuScreen
import WelcomeScreen

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.app import MDApp

# Disabling the red dots when I click on a screen
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch')


class MainApp(MDApp):
    # def build(self):
    #     return WelcomeScreen()

    def on_start(self):
        self.theme_cls.primary_palette = 'LightGreen'
        self.theme_cls.primary_hue = "700"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.accent_palette = "Gray"
        self.title = "Intercars DB"
        screen_manager = self.root.ids.screen_manager
        screen_manager.current = 'welcomescreen'


if __name__ == '__main__':
    MainApp().run()
