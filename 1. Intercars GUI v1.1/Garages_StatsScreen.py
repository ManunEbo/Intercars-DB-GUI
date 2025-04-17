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


class Garages_StatsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def Garages_contact_details(self):
        sql_str = """ call Garages_Contact_details_call(); """

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
                ("Garage_type", dp(40)),
                ("Entity_Name", dp(40)),
                ("VAT_Registration_Number", dp(50)),
                ("Fname", dp(30)),
                ("Mname", dp(30)),
                ("Lname", dp(30)),

                ("Address1", dp(30)),
                ("Address2", dp(30)),
                ("Address3", dp(30)),
                ("Address4", dp(30)),
                ("Address5", dp(30)),
                ("Address6", dp(30)),

                ("email", dp(100)),
                ("Tel", dp(30)),
            ],
            row_data=Ar_tup
        )

        Auction_invoice = self.ids.Data_id
        Auction_invoice.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nGarages contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nGarages contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarages contact details",
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
                text="There is no Graph 1 for\nGarages contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nGarages contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarages contact details",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # Garages service history and stats
    def Garages_service_history(self):
        sql_str = """ call Garages_Service_history_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        mydata['Price'] = mydata['Price'].fillna(0)

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
                ("Garage_type", dp(40)),
                ("Entity_Name", dp(60)),
                ("V5C_id", dp(40)),
                ("Make", dp(50)),
                ("Model", dp(50)),
                ("Reg_numb", dp(40)),

                ("Serv_date", dp(30)),
                ("Serv_type", dp(30)),
                ("Description", dp(100)),
                ("Serv_return_date", dp(30)),
                ("Service_quality_check_done", dp(50)),
                ("Service_quality_description", dp(100)),
                ("Serv_Invoice_nbr", dp(30)),
                ("Serv_Invoice_Date", dp(30)),
                ("Serv_Invoice_Description", dp(100)),
                ("Price", dp(30)),

            ],
            row_data=Ar_tup
        )

        Auction_invoice = self.ids.Data_id
        Auction_invoice.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nGarages service history",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nGarages service history",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarages service history",
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
                text="There is no Graph 1 for\nGarages service history",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nGarages service history",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarages service history",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # **********************************************************************
    # **************** Garages service history freq and sum ****************
    # **********************************************************************
    def Garages_service_history_freq_and_sum_bar1(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        v = mydata['Service_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Garages service history\nTotal frequency by garage type", fontdict=font1)
        plt.xlabel("Garage type", fontdict=font2)
        plt.ylabel("Service frequency", fontdict=font2)
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

    def Garages_service_history_freq_and_sum_bar2(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        v = mydata['Total_service_cost'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total service cost")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Garages service history\nService cost by garage type", fontdict=font1)
        plt.xlabel("Garage type", fontdict=font2)
        plt.ylabel("Service cost (£)", fontdict=font2)
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

    def Garages_service_history_freq_and_sum_pie1(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        w = mydata['Service_frequency'].to_numpy()

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

        plt.legend(title="Garage type \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Garages service history\nTotal frequency by garage type', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Garages_service_history_freq_and_sum_pie2(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        w = mydata['Total_service_cost'].to_numpy()

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

        plt.legend(title="Garage type \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Garages service history\nService cost by garage type', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    # Garages service history and stats
    def Garages_service_history_freq_and_sum(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_call(); """

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
                ("Garage_type", dp(50)),
                ("Service_frequency", dp(40)),
                ("Total_service_cost", dp(40)),
            ],
            row_data=Ar_tup
        )

        Garages_service_history_freq_and_sum = self.ids.Data_id
        Garages_service_history_freq_and_sum.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Garages_service_history_freq_and_sum_bar1()
        self.Garages_service_history_freq_and_sum_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarages service history\nfrequencies and sum",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Garages_service_history_freq_and_sum_pie1()
        self.Garages_service_history_freq_and_sum_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarages service history\nfrequencies and sum",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ****************************************************************************
    # **************** Garage company service history freq and sum ****************
    # ****************************************************************************
    def Garage_Entities_service_history_freq_and_sum_bar1(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_by_Entity_Name_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Service_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Garages service history\nTotal frequency by entity name", fontdict=font1)
        plt.xlabel("Entity name", fontdict=font2)
        plt.ylabel("Service frequency", fontdict=font2)
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

    def Garage_Entities_service_history_freq_and_sum_bar2(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_by_Entity_Name_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Total_service_cost'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total service cost")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Garages service history\nService cost by entity name", fontdict=font1)
        plt.xlabel("Entity name", fontdict=font2)
        plt.ylabel("Service cost (£)", fontdict=font2)
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

    def Garage_Entities_service_history_freq_and_sum_pie1(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_by_Entity_Name_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Service_frequency'].to_numpy()

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

        plt.legend(title="Garage entity \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Garages service history\nTotal frequency by entity name', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Garage_Entities_service_history_freq_and_sum_pie2(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_by_Entity_Name_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Total_service_cost'].to_numpy()

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

        plt.legend(title="Garage type \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Garages service history\nService cost by entity name', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    # Garages service history and stats
    def Garage_Entities_service_history_freq_and_sum(self):
        sql_str = """ call Garages_Service_history_freq_and_sum_by_Entity_Name_call(); """

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
                ("Garage_type", dp(50)),
                ("Entity_Name", dp(70)),
                ("Service_frequency", dp(40)),
                ("Total_service_cost", dp(40)),
            ],
            row_data=Ar_tup
        )

        Garages_service_history_freq_and_sum = self.ids.Data_id
        Garages_service_history_freq_and_sum.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Garage_Entities_service_history_freq_and_sum_bar1()
        self.Garage_Entities_service_history_freq_and_sum_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarage entity service history\nfrequencies and sum",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Garage_Entities_service_history_freq_and_sum_pie1()
        self.Garage_Entities_service_history_freq_and_sum_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarage entity service history\nfrequencies and sum",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # Garage companies service  history and stats by Make
    def Garage_Entities_service_freq_and_sum_by_Make(self):
        sql_str = """ call Garages_freq_and_sum_by_Entity_Name_and_Make_call(); """

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
                ("Garage_type", dp(40)),
                ("Entity_Name", dp(60)),
                ("Make", dp(40)),
                ("Service_frequency", dp(50)),
                ("Total_service_cost", dp(50)),
            ],
            row_data=Ar_tup
        )

        Garage_Entities = self.ids.Data_id
        Garage_Entities.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nGarages frequencies & sum by Entity Name and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nGarages frequencies & sum by Entity Name and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarages frequencies & sum by Entity Name and Make",
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
                text="There is no Graph 1 for\nGarages frequencies & sum by Entity Name and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nGarages frequencies & sum by Entity Name and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarages frequencies & sum by Entity Name and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # Garage Entities service  history and stats by Model
    def Garage_Entities_service_freq_and_sum_by_Model(self):
        sql_str = """ call Garages_freq_and_sum_by_Entity_Name_and_Model_call(); """

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
            rows_num=20,
            column_data=[
                ("Garage_type", dp(40)),
                ("Entity_Name", dp(60)),
                ("Make", dp(60)),
                ("Model", dp(40)),
                ("Service_frequency", dp(50)),
                ("Total_service_cost", dp(50)),
            ],
            row_data=Ar_tup
        )

        Garage_Entities = self.ids.Data_id
        Garage_Entities.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nGarages frequencies & sum by Entity Name and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nGarages frequencies & sum by Entity Name and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarages frequencies & sum by Entity Name and Model",
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
                text="There is no Graph 1 for\nGarages frequencies & sum by Entity Name and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nGarages frequencies & sum by Entity Name and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarages frequencies & sum by Entity Name and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ****************************************************************
    # *********** Fiscal garage service history and stats ***********
    # ****************************************************************
    # Fiscal garages service
    def Fiscal_garages_service(self):
        sql_str = """ call Fiscal_Garages_type_service_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        mydata['Price'] = mydata['Price'].fillna(0)

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
                ("Garage_type", dp(40)),
                ("Entity_Name", dp(60)),
                ("V5C_id", dp(40)),
                ("Make", dp(50)),
                ("Model", dp(50)),
                ("Reg_numb", dp(40)),

                ("Serv_date", dp(30)),
                ("financial_year", dp(30)),
                ("Serv_type", dp(30)),
                ("Description", dp(100)),
                ("Serv_return_date", dp(30)),
                ("Service_quality_check_done", dp(50)),
                ("Service_quality_description", dp(100)),
                ("Serv_Invoice_nbr", dp(30)),
                ("Serv_Invoice_Date", dp(30)),
                ("Serv_Invoice_Description", dp(100)),
                ("Price", dp(30)),
            ],
            row_data=Ar_tup
        )

        Auction_invoice = self.ids.Data_id
        Auction_invoice.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal garages service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal garages service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal garages service",
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
                text="There is no Graph 1 for\nFiscal garages service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal garages service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal garages service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ***********************************************************************
    # **************** Fiscal Garages service freq and price ****************
    # ***********************************************************************
    def Fiscal_grg_serv_freq_price_bar1(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        v = mydata['Service_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal garages service\nTotal frequency by garage type", fontdict=font1)
        plt.xlabel("Garage type", fontdict=font2)
        plt.ylabel("Service frequency", fontdict=font2)
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

    def Fiscal_grg_serv_freq_price_bar2(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        v = mydata['Total_service_cost'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total service cost")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal garages service\nService cost by garage type", fontdict=font1)
        plt.xlabel("Garage type", fontdict=font2)
        plt.ylabel("Service cost (£)", fontdict=font2)
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

    def Fiscal_grg_serv_freq_price_pie1(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        w = mydata['Service_frequency'].to_numpy()

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

        plt.legend(title="Fiscal garage type \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal garages service\nTotal frequency by garage type', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_grg_serv_freq_price_pie2(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Garage_type'].to_numpy()
        w = mydata['Total_service_cost'].to_numpy()

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

        plt.legend(title="Fiscal garage type \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal garages service\nService cost by garage type', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    # Fiscal garages service
    def Fiscal_grg_serv_freq_price(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_call(); """

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
                ("Garage_type", dp(50)),
                ("Service_frequency", dp(40)),
                ("Total_service_cost", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_grg_serv_freq_price = self.ids.Data_id
        Fiscal_grg_serv_freq_price.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Fiscal_grg_serv_freq_price_bar1()
        self.Fiscal_grg_serv_freq_price_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal garage service frequency and price",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Fiscal_grg_serv_freq_price_pie1()
        self.Fiscal_grg_serv_freq_price_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal garage service frequency and price",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *************************************************************************
    # **************** Garage service companies freq and price ****************
    # *************************************************************************
    def Fiscal_garage_service_comp_freq_and_pri_bar1(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_by_Entity_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Service_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal garages service companies\nTotal frequency", fontdict=font1)
        plt.xlabel("Entity name", fontdict=font2)
        plt.ylabel("Service frequency", fontdict=font2)
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

    def Fiscal_garage_service_comp_freq_and_pri_bar2(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_by_Entity_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Total_service_cost'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total service cost")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal garages service companies\nService cost", fontdict=font1)
        plt.xlabel("Entity name", fontdict=font2)
        plt.ylabel("Service cost (£)", fontdict=font2)
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

    def Fiscal_garage_service_comp_freq_and_pri_pie1(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_by_Entity_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Service_frequency'].to_numpy()

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

        plt.legend(title="Fiscal services\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal garages service companies\nTotal frequency', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_garage_service_comp_freq_and_pri_pie2(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_by_Entity_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Total_service_cost'].to_numpy()

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

        plt.legend(title="Fiscal services\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal garages service companies\nService cost', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    # Garages service history and stats
    def Fiscal_garage_service_comp_freq_and_pri(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_by_Entity_call(); """

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
                ("Garage_type", dp(50)),
                ("Entity_Name", dp(70)),
                ("Service_frequency", dp(40)),
                ("Total_service_cost", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_garage_service_comp_freq_and_pri = self.ids.Data_id
        Fiscal_garage_service_comp_freq_and_pri.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Adding the Graphs
        self.Fiscal_garage_service_comp_freq_and_pri_bar1()
        self.Fiscal_garage_service_comp_freq_and_pri_bar2()

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal garage service companies\nfrequencies and price",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding the Charts
        self.Fiscal_garage_service_comp_freq_and_pri_pie1()
        self.Fiscal_garage_service_comp_freq_and_pri_pie2()

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal garage service companies\nfrequencies and price",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ***************************************************************************
    # *********** Garage companies service  history and stats by Make ***********
    # ***************************************************************************
    def Fiscal_Grg_serv_freq_and_pri_by_Make(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_by_Make_call(); """

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
                ("Garage_type", dp(40)),
                ("Entity_Name", dp(60)),
                ("Make", dp(40)),
                ("Service_frequency", dp(50)),
                ("Total_service_cost", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Grg_serv_freq_and_pri_by_Make = self.ids.Data_id
        Fiscal_Grg_serv_freq_and_pri_by_Make.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nGarages frequencies & price by service company and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nGarages frequencies & price by service company and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarages frequencies & price by service company and Make",
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
                text="There is no Graph 1 for\nGarages frequencies & price by service company and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nGarages frequencies & price by service company and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarages frequencies & price by service company and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # Garage Entities service  history and stats by Model
    def Fiscal_Grg_serv_freq_and_pri_by_Model(self):
        sql_str = """ call Fiscal_Garages_service_freq_price_by_Model_call(); """

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
                ("Garage_type", dp(40)),
                ("Entity_Name", dp(60)),
                ("Make", dp(60)),
                ("Model", dp(40)),
                ("Service_frequency", dp(50)),
                ("Total_service_cost", dp(50)),
            ],
            row_data=Ar_tup
        )

        Garage_Entities = self.ids.Data_id
        Garage_Entities.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nGarages frequencies & price by service company and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nGarages frequencies & price by service company and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nGarages frequencies & price by service company and Model",
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
                text="There is no Graph 1 for\nGarages frequencies & price by service company and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nGarages frequencies & price by service company and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nGarages frequencies & price by service company and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
