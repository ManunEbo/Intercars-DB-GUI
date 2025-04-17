from kivy.uix.screenmanager import Screen, ScreenManager


class StaffScreen(Screen):
    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # Only authorised staff members can create a new staff entry
    # Validate Password
    def verify(self):

        Authorised = [1, 5]
        if self.manager.get_screen('welcomescreen').Staff_id in Authorised:
            self.ids.Staff_lbl.text = "Staff"

            if self.ids.Passwd_textf.text == self.ids.Passwd_confirm_textf.text:
                self.manager.current = "staff_details_screen"
            else:
                self.ids.Passwd_confirm_lbl.text = "Confirm Password\n[color=#D50000][b]Mismatch[/b][/color]"

        else:
            self.ids.Staff_lbl.text = "Staff\n[color=#D50000][b][size=16]Unauthorized[/size][/b][/color]"
            return

    def password_Reset(self):
        Authorised = [1, 5]
        if self.manager.get_screen('welcomescreen').Staff_id in Authorised:
            self.manager.current = "password_reset_screen"
            self.ids.Staff_lbl.text = "Staff"
        else:
            self.ids.Staff_lbl.text = "Staff\n[color=#D50000][b][size=16]Unauthorized[/size][/b][/color]"
            return

    def disable_password(self):
        Authorised = [1, 5]
        if self.manager.get_screen('welcomescreen').Staff_id in Authorised:
            self.ids.Staff_lbl.text = "Staff"
            self.manager.current = "disable_password_screen"
        else:
            self.ids.Staff_lbl.text = "Staff\n[color=#D50000][b][size=16]Unauthorized[/size][/b][/color]"
            return
