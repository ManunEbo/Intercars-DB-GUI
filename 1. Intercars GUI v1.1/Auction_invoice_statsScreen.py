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


class Auction_invoice_statsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    # **********************************************************
    # **************** Auction invoice all data ****************
    # **********************************************************
    def Auction_invoice_all_inhouse_data(self):
        sql_str = """ select a.Auction_id,
            		a.Entity_Name,
            		b.Invoice_nbr,
                    b.Invoice_Date,
                    b.Reg_nbr,
                    b.Make,
                    b.Model,
                    b.Date_first_Reg,
                    b.MOT_Expiry_date,
                    b.Mileage,
                    b.Cash_Payment,
                    b.Price,
                    b.Buyers_Fee,
                    b.Assurance_Fee,
                    b.Other_Fee,
                    b.Storage_Fee,
                    b.Cash_Handling_fee,
                    b.Auction_VAT,
                    b.Total,
                    b.Date_added

            from icp.Entity a
            left join icp.Auction_invoice b
            on a.Auction_id = b.Auction_id
            where b.Auction_id is not null; """

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
                ("Auction_id", dp(30)),
                ("Entity_Name", dp(40)),
                ("Invoice_nbr", dp(40)),
                ("Invoice_Date", dp(30)),
                ("Reg_nbr", dp(30)),
                ("Make", dp(30)),

                ("Model", dp(30)),
                ("Date_first_Reg", dp(30)),
                ("MOT_Expiry_date", dp(30)),
                ("Mileage", dp(30)),
                ("Cash_Payment", dp(30)),
                ("Price", dp(30)),

                ("Buyers_Fee", dp(30)),
                ("Assurance_Fee", dp(30)),
                ("Other_Fee", dp(30)),
                ("Storage_Fee", dp(30)),
                ("Cash_Handling_fee", dp(30)),
                ("Auction_VAT", dp(30)),
                ("Total", dp(30)),
                ("Date_added", dp(40)),
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
                text="There is no Chart 1 for\nAuction invoice all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nAuction invoice all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nAuction invoice all inhouse data",
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
                text="There is no Graph 1 for\nAuction invoice all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nAuction invoice all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nAuction invoice all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *********************************************************************
    # **************** Auction invoice all data by auction ****************
    # *********************************************************************
    def Auction_invoice_by_auction_bar1(self):
        sql_str = """ select a.Auction_id,
                		a.Entity_Name,
                        count(a.Auction_id) as Auction_frequency,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                    from icp.Entity a
                    left join icp.Auction_invoice b
                    on a.Auction_id = b.Auction_id
                    where b.Auction_id is not null
                    group by a.Entity_Name
                    order by Auction_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Auction_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Auction frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Auction invoice\nTotal frequency by auction", fontdict=font1)
        plt.xlabel("Entity Name", fontdict=font2)
        plt.ylabel("Total frequency", fontdict=font2)
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

    def Auction_invoice_by_auction_bar2(self):
        sql_str = """ select a.Auction_id,
                		a.Entity_Name,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                    from icp.Entity a
                    left join icp.Auction_invoice b
                    on a.Auction_id = b.Auction_id
                    where b.Auction_id is not null
                    group by a.Entity_Name
                    order by Expenditure desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Total_Vat'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Vat")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Auction invoice\nTotal vat by auction", fontdict=font1)
        plt.xlabel("Entity Name", fontdict=font2)
        plt.ylabel("Total vat (£)", fontdict=font2)
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

    def Auction_invoice_by_auction_bar3(self):
        sql_str = """ select a.Auction_id,
                    		a.Entity_Name,
                            sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                            sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by a.Entity_Name
                        order by Expenditure desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Expenditure'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Expenditure")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Auction invoice\nTotal Expenditure by auction", fontdict=font1)
        plt.xlabel("Entity_Name", fontdict=font2)
        plt.ylabel("Expenditure (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_invoice_by_auction_pie1(self):
        sql_str = """ select a.Auction_id,
                		a.Entity_Name,
                        count(a.Auction_id) as Auction_frequency,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                    from icp.Entity a
                    left join icp.Auction_invoice b
                    on a.Auction_id = b.Auction_id
                    where b.Auction_id is not null
                    group by a.Entity_Name
                    order by Auction_frequency desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Auction_frequency'].to_numpy()

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

        plt.legend(title="Auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Auction invoice\nTotal frequency by auction', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_invoice_by_auction_pie2(self):
        sql_str = """ select a.Auction_id,
                		a.Entity_Name,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                    from icp.Entity a
                    left join icp.Auction_invoice b
                    on a.Auction_id = b.Auction_id
                    where b.Auction_id is not null
                    group by a.Entity_Name
                    order by Expenditure desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Total_Vat'].to_numpy()

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

        plt.legend(title="Auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Auction invoice\nTotal vat by auction', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_invoice_by_auction_pie3(self):
        sql_str = """ select a.Auction_id,
                		a.Entity_Name,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                    from icp.Entity a
                    left join icp.Auction_invoice b
                    on a.Auction_id = b.Auction_id
                    where b.Auction_id is not null
                    group by a.Entity_Name
                    order by Expenditure desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Expenditure'].to_numpy()

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

        plt.legend(title="Auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Auction invoice\nTotal Expenditure by auction', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_invoice_by_auction(self):
        sql_str = """ select a.Auction_id,
                		a.Entity_Name,
                        count(a.Auction_id) as Auction_frequency,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                    from icp.Entity a
                    left join icp.Auction_invoice b
                    on a.Auction_id = b.Auction_id
                    where b.Auction_id is not null
                    group by a.Entity_Name
                    order by Expenditure desc; """

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
                ("Auction_id", dp(30)),
                ("Entity_Name", dp(40)),
                ("Auction_frequency", dp(40)),
                ("Total_Vat", dp(40)),
                ("Expenditure", dp(30)),
            ],
            row_data=Ar_tup
        )

        Auction_invoice = self.ids.Data_id
        Auction_invoice.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the graphs
        self.Auction_invoice_by_auction_bar1()
        self.Auction_invoice_by_auction_bar2()
        self.Auction_invoice_by_auction_bar3()

        # Calling the charts
        self.Auction_invoice_by_auction_pie1()
        self.Auction_invoice_by_auction_pie2()
        self.Auction_invoice_by_auction_pie3()

    # ******************************************************************
    # **************** Auction invoice summary by month ****************
    # ******************************************************************
    def Auction_summary_monthly_bar1(self):
        sql_str = """ select year(b.Invoice_Date) as The_year,
    					month(b.Invoice_Date) as The_month,
    					concat(year(b.Invoice_Date), "/", month(b.Invoice_Date)) as Year_and_month,
                        count(a.Auction_id) as Auction_frequency,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by The_year,The_month, Year_and_month
                        order by The_year desc , The_month desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        v = mydata['Auction_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Auction frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Auction invoice\nTotal Auction frequency by year and month", fontdict=font1)
        plt.xlabel("Year and month", fontdict=font2)
        plt.ylabel("Total frequency", fontdict=font2)
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

    def Auction_summary_monthly_bar2(self):
        sql_str = """ select year(b.Invoice_Date) as The_year,
    					month(b.Invoice_Date) as The_month,
    					concat(year(b.Invoice_Date), "/", month(b.Invoice_Date)) as Year_and_month,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by The_year,The_month, Year_and_month
                        order by The_year desc , The_month desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        v = mydata['Total_Vat'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Vat")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Auction invoice\nTotal vat by year and month", fontdict=font1)
        plt.xlabel("Year and month", fontdict=font2)
        plt.ylabel("Total vat (£)", fontdict=font2)
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

    def Auction_summary_monthly_bar3(self):
        sql_str = """ select year(b.Invoice_Date) as The_year,
        					month(b.Invoice_Date) as The_month,
        					concat(year(b.Invoice_Date), "/", month(b.Invoice_Date)) as Year_and_month,
                            sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                            sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by The_year,The_month, Year_and_month
                        order by The_year desc , The_month desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        v = mydata['Expenditure'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Expenditure")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Auction invoice\nTotal expenditure by year and month", fontdict=font1)
        plt.xlabel("Year and month", fontdict=font2)
        plt.ylabel("Expenditure (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_summary_monthly_pie1(self):
        sql_str = """ select year(b.Invoice_Date) as The_year,
        					month(b.Invoice_Date) as The_month,
        					concat(year(b.Invoice_Date), "/", month(b.Invoice_Date)) as Year_and_month,
                            count(a.Auction_id) as Auction_frequency,
                            sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                            sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by The_year,The_month, Year_and_month
                        order by The_year desc , The_month desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        w = mydata['Auction_frequency'].to_numpy()

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

        plt.legend(title="Auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Auction invoice\nTotal Auction frequency by year and month', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_summary_monthly_pie2(self):
        sql_str = """ select year(b.Invoice_Date) as The_year,
        					month(b.Invoice_Date) as The_month,
        					concat(year(b.Invoice_Date), "/", month(b.Invoice_Date)) as Year_and_month,
                            sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                            sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by The_year,The_month, Year_and_month
                        order by The_year desc , The_month desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        w = mydata['Total_Vat'].to_numpy()

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

        plt.legend(title="Auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Auction invoice\nTotal vat by year and month', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_summary_monthly_pie3(self):
        sql_str = """ select year(b.Invoice_Date) as The_year,
    					month(b.Invoice_Date) as The_month,
    					concat(year(b.Invoice_Date), "/", month(b.Invoice_Date)) as Year_and_month,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by The_year,The_month, Year_and_month
                        order by The_year desc , The_month desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        w = mydata['Expenditure'].to_numpy()

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

        plt.legend(title="Auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Auction invoice\nTotal expenditure by year and month', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Auction_summary_monthly(self):
        sql_str = """ select year(b.Invoice_Date) as The_year,
    					month(b.Invoice_Date) as The_month,
    					concat(year(b.Invoice_Date), "/", month(b.Invoice_Date)) as Year_and_month,
                        count(a.Auction_id) as Auction_frequency,
                        sum(ifnull(b.Auction_VAT,0)) as Total_Vat,
                        sum(ifnull(b.Total,0)) as Expenditure
                        from icp.Entity a
                        left join icp.Auction_invoice b
                        on a.Auction_id = b.Auction_id
                        where b.Auction_id is not null
                        group by The_year,The_month, Year_and_month
                        order by The_year desc , The_month desc; """

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
            size_hint=(0.9, 0.9),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("The_year", dp(30)),
                ("The_month", dp(40)),
                ("Year_and_month", dp(40)),
                ("Auction_frequency", dp(30)),
                ("Total_Vat", dp(30)),
                ("Expenditure", dp(30)),
            ],
            row_data=Ar_tup
        )

        Auction_summary_monthly = self.ids.Data_id
        Auction_summary_monthly.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the graphs
        self.Auction_summary_monthly_bar1()
        self.Auction_summary_monthly_bar2()
        self.Auction_summary_monthly_bar3()

        # Calling the charts
        self.Auction_summary_monthly_pie1()
        self.Auction_summary_monthly_pie2()
        self.Auction_summary_monthly_pie3()

    # *************************************************************
    # **************** Fiscal auction invoice data ****************
    # *************************************************************
    def Fiscal_auction_invoice_inhouse_data(self):
        sql_str = """ call Fiscal_auction_invoice_data_call(); """

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
                ("Auction_id", dp(30)),
                ("Entity_Name", dp(40)),
                ("Invoice_nbr", dp(40)),

                ("Invoice_Date", dp(30)),
                ("financial_year", dp(30)),
                ("Invoice_Year", dp(30)),
                ("Invoice_Month", dp(30)),
                ("Year_and_month", dp(30)),

                ("Reg_nbr", dp(30)),
                ("Make", dp(30)),
                ("Model", dp(30)),

                ("Date_first_Reg", dp(30)),
                ("MOT_Expiry_date", dp(30)),
                ("Mileage", dp(30)),
                ("Cash_Payment", dp(30)),
                ("Price", dp(30)),

                ("Buyers_Fee", dp(30)),
                ("Assurance_Fee", dp(30)),
                ("Other_Fee", dp(30)),
                ("Storage_Fee", dp(30)),
                ("Cash_Handling_fee", dp(30)),
                ("Auction_VAT", dp(30)),
                ("Total", dp(30)),
                ("Date_added", dp(40)),
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
                text="There is no Chart 1 for\nFiscal auction invoice all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal auction invoice all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal auction invoice all data",
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
                text="There is no Graph 1 for\nFiscal auction invoice all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal auction invoice all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal auction invoice all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # *************************************************************
    # **************** Fiscal auction invoice data ****************
    # *************************************************************

    def Fiscal_Auction_invoice_bar1(self):
        sql_str = """ call Fiscal_auction_invoice_by_auction_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Auction_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Auction frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal auction invoice\nAuction frequency by auction", fontdict=font1)
        plt.xlabel("Entity_Name", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
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

    def Fiscal_Auction_invoice_bar2(self):
        sql_str = """ call Fiscal_auction_invoice_by_auction_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Total_Vat'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Vat")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal auction invoice\nTotal vat by auction", fontdict=font1)
        plt.xlabel("Entity_Name", fontdict=font2)
        plt.ylabel("Total vat (£)", fontdict=font2)
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

    def Fiscal_Auction_invoice_bar3(self):
        sql_str = """ call Fiscal_auction_invoice_by_auction_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        v = mydata['Expenditure'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Expenditure")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal auction invoice\nTotal Expenditure by auction", fontdict=font1)
        plt.xlabel("Entity_Name", fontdict=font2)
        plt.ylabel("Expenditure (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Auction_invoice_pie1(self):
        sql_str = """ call Fiscal_auction_invoice_by_auction_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Auction_frequency'].to_numpy()

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

        plt.legend(title="Fiscal auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal auction invoice\nAuction frequency by auction', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Auction_invoice_pie2(self):
        sql_str = """ call Fiscal_auction_invoice_by_auction_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Total_Vat'].to_numpy()

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

        plt.legend(title="Fiscal auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal auction invoice\nTotal vat by auction', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Auction_invoice_pie3(self):
        sql_str = """ call Fiscal_auction_invoice_by_auction_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Entity_Name'].to_numpy()
        w = mydata['Expenditure'].to_numpy()

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

        plt.legend(title="Fiscal auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal auction invoice\nTotal Expenditure by auction', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_auction_invoice_by_auction(self):
        sql_str = """ call Fiscal_auction_invoice_by_auction_call(); """

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
                ("Auction_id", dp(30)),
                ("Entity_Name", dp(40)),
                ("Auction_frequency", dp(40)),
                ("Total_Vat", dp(40)),
                ("Expenditure", dp(30)),
            ],
            row_data=Ar_tup
        )

        Auction_invoice = self.ids.Data_id
        Auction_invoice.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the graphs
        self.Fiscal_Auction_invoice_bar1()
        self.Fiscal_Auction_invoice_bar2()
        self.Fiscal_Auction_invoice_bar3()

        # Calling the charts
        self.Fiscal_Auction_invoice_pie1()
        self.Fiscal_Auction_invoice_pie2()
        self.Fiscal_Auction_invoice_pie3()

    # ********************************************************************************
    # **************** Fiscal auction invoice summary by year & month ****************
    # ********************************************************************************
    def Fiscal_Auction_summary_monthly_bar1(self):
        sql_str = """ call Fiscal_auction_invoice_by_year_and_month_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        v = mydata['Auction_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Auction frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal auction invoice\nAuction frequency by year and month", fontdict=font1)
        plt.xlabel("Year and month", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
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

    def Fiscal_Auction_summary_monthly_bar2(self):
        sql_str = """ call Fiscal_auction_invoice_by_year_and_month_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        v = mydata['Total_Vat'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Vat")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal auction invoice\nTotal vat by year and month", fontdict=font1)
        plt.xlabel("Year and month", fontdict=font2)
        plt.ylabel("Total vat (£)", fontdict=font2)
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

    def Fiscal_Auction_summary_monthly_bar3(self):
        sql_str = """ call Fiscal_auction_invoice_by_year_and_month_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        v = mydata['Expenditure'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Expenditure")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal auction invoice\nTotal expenditure by year and month", fontdict=font1)
        plt.xlabel("Year and month", fontdict=font2)
        plt.ylabel("Expenditure (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Auction_summary_monthly_pie1(self):
        sql_str = """ call Fiscal_auction_invoice_by_year_and_month_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        w = mydata['Auction_frequency'].to_numpy()

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

        plt.legend(title="Fiscal auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal auction invoice\nAuction frequency by year and month', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Auction_summary_monthly_pie2(self):
        sql_str = """ call Fiscal_auction_invoice_by_year_and_month_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        w = mydata['Total_Vat'].to_numpy()

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

        plt.legend(title="Fiscal auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal auction invoice\nTotal vat by year and month', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Auction_summary_monthly_pie3(self):
        sql_str = """ call Fiscal_auction_invoice_by_year_and_month_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Year_and_month'].to_numpy()
        w = mydata['Expenditure'].to_numpy()

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

        plt.legend(title="Fiscal auction invoice \nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal auction invoice\nTotal expenditure by year and month', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_auction_invoice_by_year_and_month(self):
        sql_str = """ call Fiscal_auction_invoice_by_year_and_month_call(); """

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
            size_hint=(0.9, 0.9),

            check=True,
            use_pagination=True,
            rows_num=15,
            column_data=[
                ("The_year", dp(30)),
                ("The_month", dp(40)),
                ("Year_and_month", dp(40)),
                ("Auction_frequency", dp(30)),
                ("Total_Vat", dp(30)),
                ("Expenditure", dp(30)),
            ],
            row_data=Ar_tup
        )

        Fiscal_auction_invoice_by_year_and_month = self.ids.Data_id
        Fiscal_auction_invoice_by_year_and_month.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the graphs
        self.Fiscal_Auction_summary_monthly_bar1()
        self.Fiscal_Auction_summary_monthly_bar2()
        self.Fiscal_Auction_summary_monthly_bar3()

        # Calling the charts
        self.Fiscal_Auction_summary_monthly_pie1()
        self.Fiscal_Auction_summary_monthly_pie2()
        self.Fiscal_Auction_summary_monthly_pie3()
