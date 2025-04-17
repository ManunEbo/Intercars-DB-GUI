from kivy.uix.screenmanager import Screen, ScreenManager

import mysql.connector
import numpy as np
import pandas as pd
from kivy.uix.tabbedpanel import TabbedPanel

# Importing Display Pixles: allows you to say how many pixles in width you want to use
from kivy.metrics import dp

from kivymd.uix.label import MDLabel
from kivymd.uix.datatables import MDDataTable

# kivy garden stuff
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt

# Importing the database connection
import sql_import
# Import Chart_colors.py
import Chart_colors


class Staff_StatsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def Staff_contact_details(self):
        sql_str = """ select a.Staff_id,
                        		c.Fname,
                        		c.Mname,
                        		c.Lname,
                        		b.Address1,
                        		b.Address2,
                        		b.Address3,
                        		b.Address4,
                        		b.Address5,
                        		b.Address6,
                        		b.email,
                        		b.Tel,
                        		a.Date_added

                        from icp.Staff a left join
                        icp.Contact_details b
                        on a.Staff_id = b.Staff_id
                        left join icp.Names c
                        on a.Staff_id = c.Staff_id; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Fname", dp(40)),
                ("Mname", dp(30)),
                ("Lname", dp(60)),
                ("Address1", dp(30)),
                ("Address2", dp(50)),
                ("Address3", dp(50)),
                ("Address4", dp(50)),
                ("Address5", dp(50)),
                ("Address6", dp(30)),

                ("email", dp(100)),
                ("Tel", dp(30)),
                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Staff_contact_details = self.ids.Data_id
        Staff_contact_details.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nStaff contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nStaff contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nStaff contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nStaff contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nStaff contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nStaff contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    def Deposit_all_data_by_staff(self):
        sql_str = """ select a.Staff_id,
                    		c.Fname,
                    		c.Mname,
                    		c.Lname,
                            d.Make,
                            d.Model,
                            d.Reg_Numb,
                            b.Deposit_Date,
                            b.Deposit_Time,
                            b.Deposit_Amount

                    from icp.Staff a left join
                    icp.Names c
                    on a.Staff_id = c.Staff_id
                    left join icp.Deposit b
                    on a.Staff_id = b.Staff_id
                    left join icp.V5C d
                    on b.V5C_id = d.V5C_id
                    ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Fname", dp(40)),
                ("Mname", dp(30)),
                ("Lname", dp(60)),
                ("Make", dp(30)),
                ("Model", dp(50)),
                ("Reg_Numb", dp(50)),
                ("Deposit_Date", dp(50)),
                ("Deposit_Time", dp(50)),
                ("Deposit_Amount", dp(30)),
            ],
            row_data=Ar_tup
        )

        Deposit_all_data_by_staff = self.ids.Data_id
        Deposit_all_data_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nDeposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nDeposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nDeposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nDeposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nDeposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nDeposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ****************************************************************
    # ***************** Deposit frequency and amount *****************
    # ****************************************************************
    def Deposit_freq_amount_by_staff_bar1(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Deposit_frequency,
                                sum(ifnull(b.Deposit_Amount,0)) as Deposit_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Deposit b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Deposit_Total desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Deposit_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Deposit frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Deposit frequency\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Deposit frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Deposit_freq_amount_by_staff_bar2(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Deposit_frequency,
                                sum(ifnull(b.Deposit_Amount,0)) as Deposit_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Deposit b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Deposit_Total desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Deposit_Total'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Deposit amount total")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Deposit amount total\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Deposit frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Deposit_freq_amount_by_staff_pie1(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Deposit_frequency,
                                sum(ifnull(b.Deposit_Amount,0)) as Deposit_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Deposit b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Deposit_Total desc
                        ; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Deposit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Deposit frequency\nBy staff', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Deposit_freq_amount_by_staff_pie2(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Deposit_frequency,
                                sum(ifnull(b.Deposit_Amount,0)) as Deposit_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Deposit b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Deposit_Total desc
                        ; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Deposit_Total'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Deposit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Deposit amount total\nBy staff', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Deposit_freq_amount_by_staff(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Deposit_frequency,
                                sum(ifnull(b.Deposit_Amount,0)) as Deposit_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Deposit b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Deposit_Total desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Deposit_frequency", dp(40)),
                ("Deposit_Total", dp(40)),
            ],
            row_data=Ar_tup
        )

        Deposit_freq_amount_by_staff = self.ids.Data_id
        Deposit_freq_amount_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Deposit_freq_amount_by_staff_bar1()
        self.Deposit_freq_amount_by_staff_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nDeposit frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Deposit_freq_amount_by_staff_pie1()
        self.Deposit_freq_amount_by_staff_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nDeposit frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ************************************************************************************
    # ******************** Deposit Frequency and amount total by Make ********************
    # ************************************************************************************
    def Deposit_freq_amount_by_staff_Make(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		d.Make,
                        		count(b.V5C_id) as Deposit_frequency,
                                format(sum(ifnull(b.Deposit_Amount,0)),2) as Deposit_Total
                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Deposit b
                        on a.Staff_id = b.Staff_id
                        left join icp.V5C d
                        on b.V5C_id = d.V5C_id
                        group by a.Staff_id,d.Make
                        order by d.Make,Deposit_Total desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Make", dp(50)),
                ("Deposit_frequency", dp(40)),
                ("Deposit_Total", dp(40)),
            ],
            row_data=Ar_tup
        )

        Deposit_all_data_by_staff = self.ids.Data_id
        Deposit_all_data_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nDeposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nDeposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nDeposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nDeposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nDeposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nDeposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ************************************************************************************
    # ******************** Deposit Frequency and amount total by Model ********************
    # ************************************************************************************
    def Deposit_freq_amount_by_staff_Model(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		d.Make,
                                d.Model,
                        		count(b.V5C_id) as Deposit_frequency,
                                format(sum(ifnull(b.Deposit_Amount,0)),2) as Deposit_Total
                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Deposit b
                        on a.Staff_id = b.Staff_id
                        left join icp.V5C d
                        on b.V5C_id = d.V5C_id
                        group by a.Staff_id,d.Make,d.Model
                        order by d.Make,d.Model,Deposit_Total desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Make", dp(50)),
                ("Model", dp(50)),
                ("Deposit_frequency", dp(40)),
                ("Deposit_Total", dp(40)),
            ],
            row_data=Ar_tup
        )

        Deposit_all_data_by_staff = self.ids.Data_id
        Deposit_all_data_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nDeposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nDeposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nDeposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nDeposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nDeposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nDeposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # **********************************************************************
    # ******************** Fiscal deposit data by staff ********************
    # **********************************************************************
    def Fiscal_Deposit_data_by_staff(self):
        sql_str = """ call Fiscal_Deposit_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(80)),
                ("Make", dp(30)),
                ("Model", dp(50)),
                ("Reg_Numb", dp(50)),
                ("Deposit_Date", dp(50)),
                ("financial_year", dp(50)),
                ("Deposit_Time", dp(50)),
                ("Deposit_Amount", dp(30)),
            ],
            row_data=Ar_tup
        )

        Deposit_all_data_by_staff = self.ids.Data_id
        Deposit_all_data_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal deposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal deposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal deposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal deposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal deposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal deposit by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *********************************************************************************************
    # ******************** Fiscal deposit frequency and amount total  by staff ********************
    # *********************************************************************************************
    def Fiscal_Deposit_freq_amount_by_staff_bar1(self):
        sql_str = """ Call Fiscal_Deposit_freq_amount_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Fiscal_deposit_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Deposit frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal deposit frequency\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Fiscal deposit frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Deposit_freq_amount_by_staff_bar2(self):
        sql_str = """ Call Fiscal_Deposit_freq_amount_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Fiscal_deposit_amount'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Deposit amount total")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal deposit amount total\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Fiscal deposit frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Deposit_freq_amount_by_staff_pie1(self):
        sql_str = """ Call Fiscal_Deposit_freq_amount_by_Staff(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Fiscal_deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal deposit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal deposit frequency\nBy staff', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Deposit_freq_amount_by_staff_pie2(self):
        sql_str = """ Call Fiscal_Deposit_freq_amount_by_Staff(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Fiscal_deposit_amount'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal deposit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal deposit amount total\nBy staff', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Deposit_freq_amount_by_staff(self):
        sql_str = """ Call Fiscal_Deposit_freq_amount_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Deposit_frequency", dp(40)),
                ("Deposit_Total", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Deposit_freq_by_staff = self.ids.Data_id
        Fiscal_Deposit_freq_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Fiscal_Deposit_freq_amount_by_staff_bar1()
        self.Fiscal_Deposit_freq_amount_by_staff_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal deposit frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Fiscal_Deposit_freq_amount_by_staff_pie1()
        self.Fiscal_Deposit_freq_amount_by_staff_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal deposit frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *******************************************************************************************
    # ******************** Fiscal deposit Frequency and amount total by Make ********************
    # *******************************************************************************************

    def Fiscal_Deposit_freq_amount_by_staff_Make(self):
        sql_str = """ call Fiscal_Deposit_freq_amount_by_Make(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Make", dp(50)),
                ("Fiscal_deposit_frequency", dp(40)),
                ("Fiscal_deposit_amount", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Deposit_freq_by_Make = self.ids.Data_id
        Fiscal_Deposit_freq_by_Make.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal deposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal deposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal deposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal deposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal deposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal deposit frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ********************************************************************************************
    # ******************** Fiscal deposit Frequency and amount total by Model ********************
    # ********************************************************************************************
    def Fiscal_Deposit_freq_amount_by_staff_Model(self):
        sql_str = """ call Fiscal_Deposit_freq_amount_by_Model(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Make", dp(50)),
                ("Model", dp(80)),
                ("Fiscal_deposit_frequency", dp(50)),
                ("Fiscal_deposit_amount", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Deposit_freq_by_Make = self.ids.Data_id
        Fiscal_Deposit_freq_by_Make.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal deposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal deposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal deposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal deposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal deposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal deposit frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *********************************************************************
    # ******************** All time Sale data by Staff ********************
    # *********************************************************************

    def Sale_all_data_by_Staff(self):
        sql_str = """ select a.Staff_id,
                        concat(c.Fname," ",c.Mname," ",c.Lname) as Staff_Name,
                                d.Make,
                                d.Model,
                                d.Reg_Numb,
                                b.Sale_Date,
                                b.Sale_Time,
                                b.Sale_Amount

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id
                        left join icp.V5C d
                        on b.V5C_id = d.V5C_id
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff_Name", dp(60)),
                ("Make", dp(50)),
                ("Model", dp(50)),
                ("Reg_Numb", dp(40)),
                ("Sale_Date", dp(40)),
                ("Sale_Time", dp(40)),
                ("Sale_Amount", dp(40)),
            ],
            row_data=Ar_tup
        )

        Sale_all_data_by_Staff = self.ids.Data_id
        Sale_all_data_by_Staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nSale all data by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nSale all data by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nSale all data by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nSale all data by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nSale all data by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nSale all data by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *************************************************************
    # ***************** Sale frequency and amount *****************
    # *************************************************************

    def Sale_freq_amount_by_staff_bar1(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Sale_frequency,
                                sum(ifnull(b.Sale_Amount,0)) as Sale_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Sale_frequency desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Sale_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Sale frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Sale frequency\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Sale frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Sale_freq_amount_by_staff_bar2(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Sale_frequency,
                                sum(ifnull(b.Sale_Amount,0)) as Sale_Total
                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Sale_frequency desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Sale_Total'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Sale amount total")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Sale amount total\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Sale frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Sale_freq_amount_by_staff_pie1(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Sale_frequency,
                                sum(ifnull(b.Sale_Amount,0)) as Sale_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Sale_frequency desc
                        ; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Sale_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Sale\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Sale frequency\nBy staff', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Sale_freq_amount_by_staff_pie2(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Sale_frequency,
                                sum(ifnull(b.Sale_Amount,0)) as Sale_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Sale_frequency desc
                        ; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Sale_Total'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Sale\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Sale amount total\nBy staff', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Sale_freq_amount_by_staff(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		count(b.V5C_id) as Sale_frequency,
                                format(sum(ifnull(b.Sale_Amount,0)),2) as Sale_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id

                        group by a.Staff_id
                        order by Sale_frequency desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Sale_frequency", dp(40)),
                ("Sale_Total", dp(40)),
            ],
            row_data=Ar_tup
        )

        Deposit_freq_amount_by_staff = self.ids.Data_id
        Deposit_freq_amount_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Sale_freq_amount_by_staff_bar1()
        self.Sale_freq_amount_by_staff_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nSale frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Sale_freq_amount_by_staff_pie1()
        self.Sale_freq_amount_by_staff_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nSale frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *********************************************************************************
    # ******************** Sale Frequency and amount total by Make ********************
    # *********************************************************************************
    def Sale_freq_amount_by_staff_Make(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		d.Make,
                        		count(b.V5C_id) as Sale_frequency,
                                format(sum(ifnull(b.Sale_Amount,0)),2) as Sale_Total

                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id
                        left join icp.V5C d
                        on b.V5C_id = d.V5C_id

                        group by a.Staff_id,d.Make
                        order by d.Make,Sale_Total desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Make", dp(50)),
                ("Sale_frequency", dp(40)),
                ("Sale_Total", dp(40)),
            ],
            row_data=Ar_tup
        )

        Deposit_all_data_by_staff = self.ids.Data_id
        Deposit_all_data_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nSale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nSale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nSale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nSale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nSale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nSale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # **********************************************************************************
    # ******************** Sale Frequency and amount total by Model ********************
    # **********************************************************************************
    def Sale_freq_amount_by_staff_Model(self):
        sql_str = """ select a.Staff_id,
                        		concat(c.Fname, " ", c.Mname," ", c.Lname) as Staff,
                        		d.Make,
                                d.Model,
                        		count(b.V5C_id) as Sale_frequency,
                                format(sum(ifnull(b.Sale_Amount,0)),2) as Sale_Total
                        from icp.Staff a left join
                        icp.Names c
                        on a.Staff_id = c.Staff_id
                        left join icp.Sale b
                        on a.Staff_id = b.Staff_id
                        left join icp.V5C d
                        on b.V5C_id = d.V5C_id

                        group by a.Staff_id,d.Make,d.Model
                        order by d.Make,d.Model,Sale_Total desc
                        ; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Make", dp(50)),
                ("Model", dp(60)),
                ("Sale_frequency", dp(40)),
                ("Sale_Total", dp(40)),
            ],
            row_data=Ar_tup
        )

        Deposit_all_data_by_staff = self.ids.Data_id
        Deposit_all_data_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nSale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nSale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nSale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nSale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nSale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nSale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # **********************************************************************
    # ******************** Fiscal deposit data by staff ********************
    # **********************************************************************
    def Fiscal_Sale_data_by_staff(self):
        sql_str = """ call Fiscal_Sale_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(80)),
                ("Make", dp(30)),
                ("Model", dp(50)),
                ("Reg_Numb", dp(50)),
                ("Sale_Date", dp(50)),
                ("financial_year", dp(50)),
                ("Sale_Time", dp(50)),
                ("Sale_Amount", dp(30)),
            ],
            row_data=Ar_tup
        )

        Deposit_all_data_by_staff = self.ids.Data_id
        Deposit_all_data_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Sale by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Sale by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Sale by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal Sale by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Sale by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Sale by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ******************************************************************************************
    # ******************** Fiscal Sale frequency and amount total  by staff ********************
    # ******************************************************************************************
    def Fiscal_Sale_freq_amount_by_staff_bar1(self):
        sql_str = """ Call Fiscal_Sale_freq_amount_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Fiscal_Sale_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Sale frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal sale frequency\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Fiscal sale frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Sale_freq_amount_by_staff_bar2(self):
        sql_str = """ Call Fiscal_Sale_freq_amount_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        v = mydata['Fiscal_Sale_amount'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))

        fig = plt.figure(figsize=(10, 5))
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')

        # Setting the size of the bar graph
        ax.figsize = (10, 5)

        # ax.patch.set_alpha(1.0)
        ax.patch.set_alpha(0.80)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, v, w, color="#D50000", label="Sale amount total")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal sale amount total\nBy staff", fontdict=font1)
        plt.xlabel("Staff", fontdict=font2)
        plt.ylabel("Fiscal sale amount total", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Sale_freq_amount_by_staff_pie1(self):
        sql_str = """ Call Fiscal_Sale_freq_amount_by_Staff(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Fiscal_Sale_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal sale\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal sale frequency\nBy staff', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Sale_freq_amount_by_staff_pie2(self):
        sql_str = """ Call Fiscal_Sale_freq_amount_by_Staff(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Staff'].to_numpy()
        w = mydata['Fiscal_Sale_amount'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.2)

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}

        # Creating the pie chart
        patches, texts, pcts = ax.pie(
            w, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            # textprops={'size': 'x-large'},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal sale\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal sale amount total\nBy staff', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Sale_freq_amount_by_staff(self):
        sql_str = """ Call Fiscal_Sale_freq_amount_by_Staff(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(80)),
                ("Fiscal_Sale_frequency", dp(50)),
                ("Fiscal_Sale_amount", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Deposit_freq_by_staff = self.ids.Data_id
        Fiscal_Deposit_freq_by_staff.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Fiscal_Sale_freq_amount_by_staff_bar1()
        self.Fiscal_Sale_freq_amount_by_staff_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Sale frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Fiscal_Sale_freq_amount_by_staff_pie1()
        self.Fiscal_Sale_freq_amount_by_staff_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Sale frequency and amount by staff",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ****************************************************************************************
    # ******************** Fiscal sale Frequency and amount total by Make ********************
    # ****************************************************************************************

    def Fiscal_Sale_freq_amount_by_staff_Make(self):
        sql_str = """ call Fiscal_Sale_freq_amount_by_Make(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(60)),
                ("Make", dp(50)),
                ("Fiscal_sale_frequency", dp(40)),
                ("Fiscal_sale_amount", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Sale_freq_by_Make = self.ids.Data_id
        Fiscal_Sale_freq_by_Make.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal sale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal sale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal sale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal sale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal sale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal sale frequency and amount by staff and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ********************************************************************************************
    # ******************** Fiscal sale Frequency and amount total by Model ********************
    # ********************************************************************************************
    def Fiscal_Sale_freq_amount_by_staff_Model(self):
        sql_str = """ call Fiscal_Sale_freq_amount_by_Model(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        # Define Table
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("Staff_id", dp(40)),
                ("Staff", dp(80)),
                ("Make", dp(50)),
                ("Model", dp(80)),
                ("Fiscal_sale_frequency", dp(50)),
                ("Fiscal_sale_amount", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Sale_freq_by_Model = self.ids.Data_id
        Fiscal_Sale_freq_by_Model.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal sale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal sale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal sale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal sale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal sale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal sale frequency and amount by staff and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
