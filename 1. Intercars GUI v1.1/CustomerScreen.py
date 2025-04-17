# from re import X
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker


class CustomerScreen(Screen):

    def __init__(self, **kwargs):
        super(CustomerScreen, self).__init__(**kwargs)
        self.FirstName = ""
        self.MiddleName = ""
        self.LastName = ""
        self.AgeGroup = ""
        self.Customer_DOB = ""

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def agegroup_clicked(self, value):
        self.FirstName = self.ids.firstname_textf.text

        if self.ids.middlename_textf.text is None:
            self.MiddleName = ""
        else:
            self.MiddleName = self.ids.middlename_textf.text

        self.LastName = self.ids.lastname_textf.text

        self.AgeGroup = value

    # DOB
    def Customer_DOB_on_save(self, instance, value, date_range):
        self.Customer_DOB = value
        self.ids.DOB_label.text = "DOB:\n[color=#76FF03][b]{0}[/b][/color]".format(
            self.Customer_DOB)

    # click cancel
    def Customer_DOB_on_cancel(self, instance, value):
        pass

    def Customer_DOB_picker(self):
        date_dialog = MDDatePicker(
            primary_color="#76FF03",
            accent_color="#424242",
            selector_color="#000000",
            text_button_color="#000000",
            text_toolbar_color="#000000",
            text_color="#76FF03",
            min_year=2014,
            max_year=2050,)
        date_dialog.bind(on_save=self.Customer_DOB_on_save, on_cancel=self.Customer_DOB_on_cancel)
        date_dialog.open()
