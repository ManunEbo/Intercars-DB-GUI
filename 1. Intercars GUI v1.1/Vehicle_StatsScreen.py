from kivy.uix.screenmanager import Screen, ScreenManager

import mysql.connector
import numpy as np
import pandas as pd
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.label import MDLabel

# kivy garden stuff
# 1
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
# 2
import matplotlib.pyplot as plt

# Import Chart_colors.py
import Chart_colors

# Importing the mysql connection from the sql_import module
import sql_import


class Vehicle_StatsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def V5C_Raw(self):
        sql_str = """ select * from icp.V5C; """

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
                ("V5C_id", dp(30)),
                ("Reg_numb", dp(30)),
                ("Prev_reg_num", dp(30)),
                ("Doc_ref_Numb", dp(40)),
                ("Date_first_Reg", dp(30)),
                ("Date_first_Reg_UK", dp(30)),

                ("Make", dp(30)),
                ("Model", dp(40)),
                ("Body_Type", dp(30)),
                ("Tax_Class", dp(30)),
                ("Type_Fuel", dp(30)),

                ("Nbr_seats", dp(30)),
                ("Vehicle_Cat", dp(30)),
                ("Colour", dp(30)),
                ("V5C_Lgbk_issue_date", dp(35)),
                ("Cylinder_capty", dp(30)),

                ("Nbr_prev_owners", dp(30)),

                ("Prev_owner1_Name", dp(40)),
                ("Prev_owner1_Addr", dp(90)),
                ("Prev_owner1_Acq_date", dp(40)),

                ("Prev_owner2_Name", dp(40)),
                ("Prev_owner2_Addr", dp(90)),
                ("Prev_owner2_Acq_date", dp(40)),

                ("Prev_owner3_Name", dp(40)),
                ("Prev_owner3_Addr", dp(90)),
                ("Prev_owner3_Acq_date", dp(40)),

                ("Prev_owner4_Name", dp(40)),
                ("Prev_owner4_Addr", dp(90)),
                ("Prev_owner4_Acq_date", dp(40)),

                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        v5c = self.ids.Data_id
        v5c.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nV5C in-house data ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nV5C in-house data ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nV5C in-house data ",
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
                text="There is no Graph 1 for\nV5C in-house data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nV5C in-house data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nV5C in-house data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # V5C all data frequencies by Make bar graph
    def V5C_by_Make_bar(self):
        sql_str = """ select Make,
                            count(make) as Vehicle_frequency
                    from icp.V5C
                    group by Make
                    order by Vehicle_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        # print("Length of x : {0}".format(len(x)))

        y = mydata['Vehicle_frequency'].to_numpy()

        mylabels = x
        # mycolors1 = ["#D50000", "#76FF03"]

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        # bar2 = [i+w for i in bar1]

        fig = plt.figure()
        fig.patch.set_facecolor('#212121')
        fig.patch.set_alpha(0.99)

        ax = fig.add_subplot(111)
        ax.patch.set_facecolor('grey')
        ax.patch.set_alpha(1.0)

        # Colouring the x and y axis labels
        ax.tick_params(axis="x", colors="lime")
        ax.tick_params(axis="y", colors="lime")

        # Create bars with different colors
        plt.bar(bar1, y, w, color="#D50000", label="Vehicle_frequency")

        plt.xticks(bar1, x)

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("V5C all data\nfrequencies by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("(Vehicle_frequency)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha="center", va="bottom")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # V5C all data frequencies by Make  pie chart
    def V5C_by_Make_pie(self):
        sql_str = """
            select Make,
                count(make) as Vehicle_frequency
                from icp.V5C
                group by Make
                order by Vehicle_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        # print("Length of x : {0}".format(len(x)))

        y = mydata['Vehicle_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        patches, texts, pcts = ax.pie(
            y, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="V5C statistics", bbox_to_anchor=(1.15, 1))
        plt.title('V5C frequencies by Make', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def V5C_by_Make(self):
        sql_str = """ select Make,
            count(make) as Vehicle_frequency
            from icp.V5C
            group by Make
            order by Vehicle_frequency desc; """

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
                ("Make", dp(50)),
                ("Vehicle_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        v5c_by_Make = self.ids.Data_id
        v5c_by_Make.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the V5C pie chart
        self.V5C_by_Make_pie()
        # Calling the V5C bar graph
        self.V5C_by_Make_bar()

        # Adding place holders for where there is no Chart and or Graph
        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nV5C by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nV5C by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nV5C by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nV5C by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # V5C all data frequencies by Model bar graph
    def V5C_by_Model_bar(self):
        sql_str = """  select Make,
                    Model,
                    count(Model) as Model_frequency
                    from icp.V5C
                    group by Make, Model
                    order by Model_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()

        y = mydata['Model_frequency'].to_numpy()

        mylabels = x
        # mycolors1 = ["#D50000", "#76FF03"]

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        # bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, y, w, color="#D50000", label="Vehicle_frequency")

        # plt.xticks(bar1, x, rotation='vertical')
        plt.xticks(bar1, x)

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("V5C all data\nfrequencies by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha="center", va="bottom")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # V5C all data frequencies by Make  pie chart
    def V5C_by_Model_pie(self):
        sql_str = """ select Make,
                    Model,
                    count(Model) as Model_frequency
                    from icp.V5C
                    group by Make, Model
                    order by Model_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        # print("Length of x : {0}".format(len(x)))

        y = mydata['Model_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        patches, texts, pcts = ax.pie(
            y, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="V5C statistics", bbox_to_anchor=(1.15, 1))
        plt.title('V5C frequencies by Model', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def V5C_by_Model(self):
        sql_str = """ select Make,
                    Model,
                    count(Model) as Model_frequency
                    from icp.V5C
                    group by Make, Model
                    order by Model_frequency desc; """

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
                ("Make", dp(50)),
                ("Model", dp(70)),
                ("Model_frequency", dp(50)),
            ],
            row_data=Ar_tup
        )

        v5c_by_Model = self.ids.Data_id
        v5c_by_Model.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling V5C frequencies by Model bar
        self.V5C_by_Model_bar()
        # Calling V5C frequencies by Model pie
        self.V5C_by_Model_pie()

        # Adding place holders for where there is no Chart and or Graph
        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nV5C by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nV5C by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nV5C by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nV5C by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    def Op_service_all_data(self):
        sql_str = """ call Op_service_Stats_call(); """

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
                ("Op_service_id", dp(35)),
                ("Make", dp(50)),
                ("Model", dp(70)),
                ("Reg_numb", dp(50)),
                ("Entity_Name", dp(70)),
                ("Serv_date", dp(50)),
                ("Serv_Invoice_nbr", dp(70)),
                ("Serv_Invoice_Date", dp(50)),
                ("financial_year", dp(50)),
                ("Serv_type", dp(50)),
                ("Description", dp(130)),
                ("Price", dp(40)),
                ("Serv_return_date", dp(70)),
                ("Service_quality_check_done", dp(70)),
                ("Service_quality_description", dp(130)),
                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Op_Service_all_data = self.ids.Data_id
        Op_Service_all_data.add_widget(table)

        # Adding place holders for where there is no Chart and or Graph
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nOp Service all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nOp Service all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nOp Service all data",
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
                text="There is no Graph 2 for\nOp Service all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nOp Service all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Service all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()
    # ****************************************************
    # **************** Op Service by Make ****************
    # *****************************************************

    # Op Service all data frequencies by Make bar graph
    def Op_service_by_Make_bar1(self):
        sql_str = """ call Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Make_frequency'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, v, w, color="#D50000", label="Make frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w/2, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Op Service all data\nfrequencies by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op_service_by_Make all data frequencies by Model bar graph
    def Op_service_by_Make_bar2(self):
        sql_str = """ call Op_service_service_cost_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        z = mydata['Service_cost'].to_numpy()

        mylabels = x
        # mycolors1 = ["#D50000", "#76FF03"]

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        # bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, z, w, color="#D50000", label="Service cost")

        # plt.xticks(bar1, x, rotation='vertical')
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Op Service all data\nService cost by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Service Cost (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op service all data frequencies by Make  pie chart
    def Op_service_by_Make_pie1(self):
        sql_str = """ call Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Make_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service Make frequencies', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op service all data service frequencies by Make pie chart
    def Op_service_by_Make_pie2(self):
        sql_str = """ call Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            y, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service\nService frequency by Make', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op_service_by_Make all data frequencies by Make  pie chart
    def Op_service_by_Make_pie3(self):
        sql_str = """ call Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        z = mydata['Service_cost'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            z, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service\nService cost by Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Op_service_by_Make(self):
        sql_str = """ call Op_service_by_Make_call(); """

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
                ("Make", dp(50)),
                ("Make_frequency", dp(50)),
                ("Service_frequency", dp(70)),
                ("Service_cost", dp(50)),
            ],
            row_data=Ar_tup
        )

        Op_Service_by_Make = self.ids.Data_id
        Op_Service_by_Make.add_widget(table)
        # Closing the database connection
        cnn.close()

        # calling the charts
        self.Op_service_by_Make_pie1()
        self.Op_service_by_Make_pie2()
        self.Op_service_by_Make_pie3()

        # Calling the Graphs
        self.Op_service_by_Make_bar1()
        self.Op_service_by_Make_bar2()

        # Adding a placeholder for Graph3
        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Service by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    # ****************************************************
    # *************** Op Service by Model ***************
    # ****************************************************

    # Op Service all data frequencies by Model bar graph
    def Op_service_by_Model_bar1(self):
        sql_str = """ call Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Model_frequency'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, v, w, color="#D50000", label="Model frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w/2, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Op Service\nfrequencies by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op_service_by_Make all data frequencies by Model bar graph
    def Op_service_by_Model_bar2(self):
        sql_str = """ call Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        z = mydata['Service_cost'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        # bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, z, w, color="#D50000", label="Service cost")

        # plt.xticks(bar1, x, rotation='vertical')
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Op Service\nService cost by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Service Cost (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op service all data frequencies by Make  pie chart
    def Op_service_by_Model_pie1(self):
        sql_str = """ call Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Model_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Model", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service Model frequencies', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op service all data service frequencies by Make pie chart
    def Op_service_by_Model_pie2(self):
        sql_str = """ call Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            y, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Model", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service\nService frequency by Model', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op_service_by_Make all data frequencies by Make  pie chart
    def Op_service_by_Model_pie3(self):
        sql_str = """ call Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        z = mydata['Service_cost'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            z, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Model", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service\nService cost by Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Op_service_by_Model(self):
        sql_str = """ call Op_service_by_Model_call(); """

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
                ("Make", dp(50)),
                ("Model", dp(70)),
                ("Model_frequency", dp(70)),
                ("Service_frequency", dp(70)),
                ("Service_cost", dp(50)),
            ],
            row_data=Ar_tup
        )
        Op_Service_by_Model = self.ids.Data_id
        Op_Service_by_Model.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling Op service pie charts
        self.Op_service_by_Model_pie1()
        self.Op_service_by_Model_pie2()
        self.Op_service_by_Model_pie3()

        # Calling Op Service bar graphs
        self.Op_service_by_Model_bar1()
        self.Op_service_by_Model_bar2()

        # Adding a placeholder for Graph3
        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Service by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    def Fiscal_Op_service(self):
        sql_str = """ call Fiscal_Op_service_call(); """

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
                ("Op_service_id", dp(40)),
                ("Make", dp(50)),
                ("Model", dp(70)),
                ("Reg_numb", dp(40)),
                ("Entity_Name", dp(130)),
                ("Serv_date", dp(50)),
                ("Serv_Invoice_nbr", dp(130)),
                ("Serv_Invoice_Date", dp(70)),
                ("financial_year", dp(70)),
                ("Serv_type", dp(70)),
                ("Description", dp(130)),
                ("Price", dp(40)),
                ("Serv_return_date", dp(40)),
                ("Service_quality_check_done", dp(70)),
                ("Service_quality_description", dp(130)),
                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Op_Service = self.ids.Data_id
        Fiscal_Op_Service.add_widget(table)

        # Adding place holders for where there is no Chart and or Graph
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Op service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Op service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Op service",
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
                text="There is no Graph 2 for\nFiscal Op service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Op service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Op service",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # ****************************************************
    # **************** Fiscal Op Service ****************
    # ****************************************************

    # Fiscal Op Service frequencies by Make bar graph
    def Fiscal_Op_service_by_Make_bar1(self):
        sql_str = """ call Fiscal_Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Make_frequency'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, v, w, color="#D50000", label="Make frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w/2, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Op Service\nfrequencies by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op_service frequencies by Make bar graph
    def Fiscal_Op_service_by_Make_bar2(self):
        sql_str = """ call Fiscal_Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        z = mydata['Service_cost'].to_numpy()

        mylabels = x
        # mycolors1 = ["#D50000", "#76FF03"]

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        # bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, z, w, color="#D50000", label="Service cost")

        # plt.xticks(bar1, x, rotation='vertical')
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Op Service\nService cost by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Service Cost (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op service frequencies by Make pie chart
    def Fiscal_Op_service_by_Make_pie1(self):
        sql_str = """ call Fiscal_Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Make_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service Make frequencies', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op service: service frequencies by Make pie chart
    def Fiscal_Op_service_by_Make_pie2(self):
        sql_str = """ call Fiscal_Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            y, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service\nService frequency by Make', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op_service frequencies by Make pie chart
    def Fiscal_Op_service_by_Make_pie3(self):
        sql_str = """ call Fiscal_Op_service_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        z = mydata['Service_cost'].to_numpy()
        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            z, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Service\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Service\nService cost by Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Op_service_by_Make(self):
        sql_str = """ call Fiscal_Op_service_by_Make_call(); """

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
                ("Make", dp(50)),
                ("Make_frequency", dp(50)),
                ("Service_frequency", dp(50)),
                ("Service_cost", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Op_Service_by_Make = self.ids.Data_id
        Fiscal_Op_Service_by_Make.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the graphs
        self.Fiscal_Op_service_by_Make_bar1()
        self.Fiscal_Op_service_by_Make_bar2()

        # Adding a placeholder for Graph 3
        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Service by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Calling the charts
        self.Fiscal_Op_service_by_Make_pie1()
        self.Fiscal_Op_service_by_Make_pie2()
        self.Fiscal_Op_service_by_Make_pie3()

    # **********************************************************
    # *************** Fiscal Op Service by Model ***************
    # **********************************************************

    # Fiscal Op Service frequencies by Model bar graph
    def Fiscal_Op_service_by_Model_bar1(self):
        sql_str = """ call Fiscal_Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Model_frequency'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, v, w, color="#D50000", label="Model frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Service frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w/2, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Op Service\nfrequencies by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op_service frequencies by Model bar graph
    def Fiscal_Op_service_by_Model_bar2(self):
        sql_str = """ call Fiscal_Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        z = mydata['Service_cost'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        # bar2 = [i+w for i in bar1]

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
        plt.bar(bar1, z, w, color="#D50000", label="Service cost")

        # plt.xticks(bar1, x, rotation='vertical')
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Op Service\nService cost by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Service Cost (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph2 = self.ids.Graph2
        Graph2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op service frequencies by Make  pie chart
    def Fiscal_Op_service_by_Model_pie1(self):
        sql_str = """ call Fiscal_Op_service_by_Model_call(); """
        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Model_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Service\nstatistics by Model", bbox_to_anchor=(1.30, 1))
        plt.title('Fiscal Op Service Model frequencies', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op service: service frequencies by Make pie chart
    def Fiscal_Op_service_by_Model_pie2(self):
        sql_str = """ call Fiscal_Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        y = mydata['Service_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            y, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Service\nstatistics by Model", bbox_to_anchor=(1.30, 1))
        plt.title('Fiscal Op Service\nService frequency by Model', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op_service frequencies by Make  pie chart
    def Fiscal_Op_service_by_Model_pie3(self):
        sql_str = """ call Fiscal_Op_service_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        z = mydata['Service_cost'].to_numpy()
        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            z, labels=mylabels, rotatelabels=True, radius=0.6, pctdistance=0.8, colors=mycolors, explode=myexplode, autopct='%1.1f%%',
            shadow=True,
            wedgeprops={'linewidth': 3.0},
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Service\nstatistics by Model", bbox_to_anchor=(1.30, 1))
        plt.title('Fiscal Op Service\nService cost by Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Op_service_by_Model(self):
        sql_str = """ call Fiscal_Op_service_by_Model_call(); """

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
                ("Make", dp(50)),
                ("Model", dp(70)),
                ("Model_frequency", dp(50)),
                ("Service_frequency", dp(50)),
                ("Service_cost", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Op_Service_by_Model = self.ids.Data_id
        Fiscal_Op_Service_by_Model.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the graphs
        self.Fiscal_Op_service_by_Model_bar1()
        self.Fiscal_Op_service_by_Model_bar2()

        # Adding a placeholder for Graph 3
        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Service by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Calling the charts
        self.Fiscal_Op_service_by_Model_pie1()
        self.Fiscal_Op_service_by_Model_pie2()
        self.Fiscal_Op_service_by_Model_pie3()

    # ***********************************************************
    # ******************** Call Log *****************************
    # ***********************************************************

    def Call_Log_all_data(self):
        sql_str = """ select a.Call_log_id,
                                a.Name,
                                a.Customer_sex,
                                a.Tel,
                                a.City_or_village,
                                a.Vehicle_of_interest,
                                a.V5C_id,
                                b.Make,
                                b.Model,
                                b.Reg_numb,
                                a.Date_of_call,
                                a.Time_of_Call,
                                a.Deposit_flag,
                                a.Date_added
                    from icp.Op_call_Log as a left join
                    icp.V5C as b
                    on a.V5C_id = b.V5C_id; """

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
                ("Call_log_id", dp(30)),
                ("Name", dp(40)),
                ("Customer_sex", dp(30)),
                ("Tel", dp(30)),
                ("City_or_village", dp(40)),
                ("Vehicle_of_interest", dp(50)),

                ("V5C_id", dp(30)),
                ("Make", dp(30)),
                ("Model", dp(50)),
                ("Reg_numb", dp(30)),

                ("Date_of_call", dp(30)),
                ("Time_of_Call", dp(30)),
                ("Deposit_flag", dp(30)),
                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Call_Log_all_data = self.ids.Data_id
        Call_Log_all_data.add_widget(table)

        # Adding place holders for where there is no Chart and or Graph
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nCall Log all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nCall Log all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nCall Log all data",
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
                text="There is no Graph 1 for\nCall Log all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nCall Log all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nCall Log all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # Call Log all data frequencies by Make bar graph
    def Op_Call_Log_by_Make_bar1(self):
        sql_str = """ select a.Make,
                        		count(distinct a.Reg_numb) as Make_frequency,
                        		count(b.V5C_id) as Call_frequency,
                                sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        		icp.V5C as a
                        	 on b.V5C_id = a.V5C_id
                        	 group by a.Make
                        	 order by Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Make_frequency'].to_numpy()
        y = mydata['Call_frequency'].to_numpy()
        z = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Make frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Call frequency")
        plt.bar(bar3, z, w, color="#E65100", label="Call Deposit frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Op Call Log all data\nfrequencies by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")
            plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op Call Log all data frequencies by Make  pie chart

    def Op_Call_Log_by_Make_pie1(self):
        sql_str = """ select a.Make,
                        		count(distinct a.Reg_numb) as Make_frequency,
                        		count(b.V5C_id) as Call_frequency,
                                sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        		icp.V5C as a
                        	 on b.V5C_id = a.V5C_id
                        	 group by a.Make
                        	 order by Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Make_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Call Log\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Call Log\nMake frequencies', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op Call Log all data frequencies by Make  pie chart 2
    def Op_Call_Log_by_Make_pie2(self):
        sql_str = """ select a.Make,
                        		count(distinct a.Reg_numb) as Make_frequency,
                        		count(b.V5C_id) as Call_frequency,
                                sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        		icp.V5C as a
                        	 on b.V5C_id = a.V5C_id
                        	 group by a.Make
                        	 order by Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Call_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Call Log\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Call Log\nMake Call frequencies', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op Call Log all data frequencies by Make  pie chart 2
    def Op_Call_Log_by_Make_pie3(self):
        sql_str = """ select a.Make,
                        		count(distinct a.Reg_numb) as Make_frequency,
                        		count(b.V5C_id) as Call_frequency,
                                sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        		icp.V5C as a
                        	 on b.V5C_id = a.V5C_id
                             where b.Deposit_flag=1
                        	 group by a.Make
                        	 order by Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Call Log\nStatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Op Call Log\nDeposit frequencies by Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Call_Log_by_Make(self):
        sql_str = """ select a.Make,
                        		count(distinct a.Reg_numb) as Make_frequency,
                        		count(b.V5C_id) as Call_frequency,
                                sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        		icp.V5C as a
                        	 on b.V5C_id = a.V5C_id
                        	 group by a.Make
                        	 order by Call_frequency desc; """

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
                ("Make", dp(40)),
                ("Make_frequency", dp(40)),
                ("Call_frequency", dp(40)),
                ("Call_Deposit_frequency", dp(50)),
            ],
            row_data=Ar_tup
        )

        Call_Log_by_Make = self.ids.Data_id
        Call_Log_by_Make.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the Graph
        self.Op_Call_Log_by_Make_bar1()

        # Adding placeholders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nOp Call Log by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Call Log by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Calling the charts
        self.Op_Call_Log_by_Make_pie1()
        self.Op_Call_Log_by_Make_pie2()
        self.Op_Call_Log_by_Make_pie3()

    # **********************************************
    # *********** Call Log by Model ****************
    # **********************************************

    # Call Log all data frequencies by Make bar graph
    def Op_Call_Log_by_Model_bar1(self):
        sql_str = """ select a.Make,
                        	a.Model,
                            count(distinct a.Reg_numb) as Model_frequency,
                        	count(b.V5C_id) as Model_Call_frequency,
                            sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make, a.Model
                         order by Model_Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Model_frequency'].to_numpy()
        y = mydata['Model_Call_frequency'].to_numpy()
        z = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Model frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Call frequency")
        plt.bar(bar3, z, w, color="#E65100", label="Call Deposit frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Op Call Log all data\nfrequencies by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")
            plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op Call Log all data frequencies by Make  pie chart
    def Op_Call_Log_by_Model_pie1(self):
        sql_str = """ select a.Make,
                        	a.Model,
                            count(distinct a.Reg_numb) as Model_frequency,
                        	count(b.V5C_id) as Model_Call_frequency,
                            sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make, a.Model
                         order by Model_Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Model_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Call Log\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Op Call Log\nModel frequencies', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op Call Log all data frequencies by Make  pie chart 2
    def Op_Call_Log_by_Model_pie2(self):
        sql_str = """ select a.Make,
                        	a.Model,
                            count(distinct a.Reg_numb) as Model_frequency,
                        	count(b.V5C_id) as Model_Call_frequency,
                            sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make, a.Model
                         order by Model_Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Model_Call_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Call Log\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Op Call Log\nModel Call frequencies', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op Call Log all data frequencies by Make  pie chart 2
    def Op_Call_Log_by_Model_pie3(self):
        sql_str = """ select a.Make,
                        	a.Model,
                            count(distinct a.Reg_numb) as Model_frequency,
                        	count(b.V5C_id) as Model_Call_frequency,
                            sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Deposit_flag = 1
                         group by a.Make, a.Model
                         order by Model_Call_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Call Log\nStatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Op Call Log\nDeposit frequencies by Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Call_Log_by_Model(self):
        sql_str = """ select a.Make,
                        	a.Model,
                            count(distinct a.Reg_numb) as Model_frequency,
                        	count(b.V5C_id) as Model_Call_frequency,
                            sum(b.Deposit_flag) as Call_Deposit_frequency
                        from icp.Op_call_Log as b left join
                        	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make, a.Model
                         order by Model_Call_frequency desc; """

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
                ("Make", dp(40)),
                ("Model", dp(40)),
                ("Model_frequency", dp(40)),
                ("Model_Call_frequency", dp(40)),
                ("Call_Deposit_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Call_Log_by_Model = self.ids.Data_id
        Call_Log_by_Model.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the Graph
        self.Op_Call_Log_by_Model_bar1()

        # Adding placeholders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nOp Call Log by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Call Log by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Calling the Charts
        self.Op_Call_Log_by_Model_pie1()
        self.Op_Call_Log_by_Model_pie2()
        self.Op_Call_Log_by_Model_pie3()

    # ******************************************************************
    # **************** Call Log by City or Village *********************
    # ******************************************************************

    # Call Log all data frequencies by City or Village bar graph
    def Op_Call_Log_by_City_or_village_bar1(self):
        sql_str = """ select City_or_village,
                    		count(Call_log_id) as Call_frequency
                    from icp.Op_call_Log
                    group by City_or_village
                    order by Call_frequency desc, City_or_village; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        v = mydata['Call_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Model frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Op Call Log all data\nfrequencies by City or Village", fontdict=font1)
        plt.xlabel("City or Village", fontdict=font2)
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

    # Op Call Log all data frequencies by Make  pie chart
    def Op_Call_Log_by_City_or_village_pie1(self):
        sql_str = """ select City_or_village,
                    		count(Call_log_id) as Call_frequency
                    from icp.Op_call_Log
                    group by City_or_village
                    order by Call_frequency desc, City_or_village; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        w = mydata['Call_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Op Call Log statistics\nby City or village", bbox_to_anchor=(1.60, 1))
        plt.title('Op Call Log frequencies\nBy City or Village', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Call_Log_by_City_or_Village(self):
        sql_str = """ select City_or_village,
                    		count(Call_log_id) as Call_frequency
                    from icp.Op_call_Log
                    group by City_or_village
                    order by Call_frequency desc, City_or_village; """

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
                ("City_or_village", dp(40)),
                ("Call_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Call_Log_by_City_or_Village = self.ids.Data_id
        Call_Log_by_City_or_Village.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the Graph
        self.Op_Call_Log_by_City_or_village_bar1()

        # Adding placeholders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nOp Call Log City or village",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp Call Log City or village",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Calling the Chart
        self.Op_Call_Log_by_City_or_village_pie1()

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nCall Log by City or Village ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nCall Log by City or Village",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    def Call_Log_by_City_or_Village_and_Make(self):
        sql_str = """ select a.City_or_village,
                    		b.Make,
                    		count(a.Call_log_id) as Call_frequency
                    from icp.Op_call_Log as a left join
                    	 icp.V5C as b
                         on a.V5C_id = b.V5C_id
                    group by a.City_or_village, b.Make
                    order by Call_frequency desc, a.City_or_village; """

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
                ("City_or_village", dp(50)),
                ("Make", dp(40)),
                ("Call_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Call_Log_by_City_or_Village_Make = self.ids.Data_id
        Call_Log_by_City_or_Village_Make.add_widget(table)

        # Adding a text place-holder for Chart
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nCall Log by City or Village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nCall Log by City or Village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nCall Log by City or Village\nand Make",
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
                text="There is no Graph 1 for\nCall Log by City or Village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nCall Log by City or Village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nCall Log by City or Village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    def Call_Log_by_City_or_Village_and_Model(self):
        sql_str = """ select a.City_or_village,
                    		b.Make,
                            b.Model,
                    		count(a.Call_log_id) as Call_frequency
                    from icp.Op_call_Log as a left join
                    	 icp.V5C as b
                         on a.V5C_id = b.V5C_id
                    group by a.City_or_village, b.Make, b.Model
                    order by Call_frequency desc, a.City_or_village; """

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
                ("City_or_village", dp(50)),
                ("Make", dp(40)),
                ("Model", dp(50)),
                ("Call_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Call_Log_by_City_or_Village_Model = self.ids.Data_id
        Call_Log_by_City_or_Village_Model.add_widget(table)

        # Chart place-holders:
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nCall Log by City or Village\nand Model ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nCall Log by City or Village\nand Model ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nCall Log by City or Village\nand Model ",
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
                text="There is no Graph 1 for\nCall Log by City or Village\nand Make ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nCall Log by City or Village\nand Make ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nCall Log by City or Village\nand Make ",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    def Fiscal_Call_Log(self):
        sql_str = """ call Fiscal_Call_Log(); """

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
                ("Call_log_id", dp(30)),
                ("Name", dp(40)),
                ("Customer_sex", dp(30)),
                ("Tel", dp(30)),
                ("City_or_village", dp(40)),
                ("Vehicle_of_interest", dp(50)),

                ("V5C_id", dp(30)),
                ("Make", dp(30)),
                ("Model", dp(50)),
                ("Reg_numb", dp(30)),

                ("Date_of_call", dp(30)),
                ("financial_year", dp(30)),
                ("Time_of_Call", dp(30)),
                ("Deposit_flag", dp(30)),
                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Call_Log = self.ids.Data_id
        Fiscal_Call_Log.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Call Log data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Call Log data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Call Log data",
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
                text="There is no Graph 1 for\nFiscal Call Log data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Call Log data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Call Log data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # ******************************************************
    # ************ Fiscal call log by Make *****************
    # ******************************************************

    # Fiscal Call Log all data frequencies by Make bar graph
    def Fiscal_Op_Call_Log_by_Make_bar1(self):
        sql_str = """ call Fiscal_Call_Log_by_Make(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Make_frequency'].to_numpy()
        y = mydata['Call_frequency'].to_numpy()
        z = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Make frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Call frequency")
        plt.bar(bar3, z, w, color="#E65100", label="Call Deposit frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Op Call Log\nfrequencies by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")
            plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Op Call Log all data frequencies by Make  pie chart
    def Fiscal_Op_Call_Log_by_Make_pie1(self):
        sql_str = """ call Fiscal_Call_Log_by_Make(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Make_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Call Log\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Fiscal Op Call Log\nFrequencies by Make', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op Call Log all data frequencies by Make  pie chart 2
    def Fiscal_Op_Call_Log_by_Make_pie2(self):
        sql_str = """ call Fiscal_Call_Log_by_Make(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Call_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Call Log\nstatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Fiscal Op Call Log\nCall frequencies by Make', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op Call Log all data frequencies by Make  pie chart 2
    def Fiscal_Op_Call_Log_by_Make_pie3(self):
        sql_str = """ call Fiscal_Call_Log_by_Make_Deposit_flag_1(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Call Log\nStatistics by Make", bbox_to_anchor=(1.30, 1))
        plt.title('Fiscal Op Call Log\nDeposit frequencies by Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Call_Log_by_Make(self):
        sql_str = """ call Fiscal_Call_Log_by_Make(); """

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
                ("Make", dp(40)),
                ("Make_frequency", dp(40)),
                ("Call_frequency", dp(40)),
                ("Call_Deposit_frequency", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Call_Log_by_Make = self.ids.Data_id
        Fiscal_Call_Log_by_Make.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the graph
        self.Fiscal_Op_Call_Log_by_Make_bar1()

        # Adding text place holders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Call Log by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Call Log by Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Calling the Charts
        self.Fiscal_Op_Call_Log_by_Make_pie1()
        self.Fiscal_Op_Call_Log_by_Make_pie2()
        self.Fiscal_Op_Call_Log_by_Make_pie3()

        # *****************************************************
        # *********** Fiscal Call Log by Model ****************
        # *****************************************************

    # Fiscal Call Log all data frequencies by Make bar graph
    def Fiscal_Op_Call_Log_by_Model_bar1(self):
        sql_str = """ call Fiscal_Call_Log_by_Model(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Model_frequency'].to_numpy()
        y = mydata['Call_frequency'].to_numpy()
        z = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Model frequency")
        plt.bar(bar2, y, w, color="#C6FF00", label="Call frequency")
        plt.bar(bar3, z, w, color="#E65100", label="Call Deposit frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1 + w, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Op Call Log\nfrequencies by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Frequency", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        for i in range(len(x)):
            plt.text(i, v[i], v[i], ha="center", va="bottom")
            plt.text(i + w, y[i], y[i], ha="center", va="bottom")
            plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph1 = self.ids.Graph1
        Graph1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op Call Log all data frequencies by Make  pie chart
    def Fiscal_Op_Call_Log_by_Model_pie1(self):
        sql_str = """ call Fiscal_Call_Log_by_Model(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Model_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Call Log\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Op Call Log\nFrequencies by Model', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op Call Log frequencies by Make  pie chart 2
    def Fiscal_Op_Call_Log_by_Model_pie2(self):
        sql_str = """ call Fiscal_Call_Log_by_Model(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Call_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Call Log\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Op Call Log\nCall frequencies by Model', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    # Fiscal Op Call Log frequencies by Make  pie chart 2
    def Fiscal_Op_Call_Log_by_Model_pie3(self):
        sql_str = """ call Fiscal_Call_Log_by_Model_Deposit_flag_1(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Call_Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Call Log\nStatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Op Call Log\nCall Deposit frequencies by Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Call_Log_by_Model(self):
        sql_str = """ call Fiscal_Call_Log_by_Model(); """

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
                ("Make", dp(40)),
                ("Model", dp(40)),
                ("Fiscal_Model_Call_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Call_Log_by_Model = self.ids.Data_id
        Fiscal_Call_Log_by_Model.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the graph
        self.Fiscal_Op_Call_Log_by_Model_bar1()

        # Adding text place holders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Call Log by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Call Log by Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Calling the Charts
        self.Fiscal_Op_Call_Log_by_Model_pie1()
        self.Fiscal_Op_Call_Log_by_Model_pie2()
        self.Fiscal_Op_Call_Log_by_Model_pie3()

    def Fiscal_Call_Log_by_City_or_village_bar1(self):
        sql_str = """ call Fiscal_Call_Log_by_City_or_village(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        v = mydata['Fiscal_Call_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Call frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Op Call Log\nfrequencies by City or village", fontdict=font1)
        plt.xlabel("City or village", fontdict=font2)
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

    # Fiscal Op Call Log all data frequencies by City or village  pie chart
    def Fiscal_Call_Log_by_City_or_village_pie1(self):
        sql_str = """ call Fiscal_Call_Log_by_City_or_village(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        w = mydata['Fiscal_Call_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Fiscal Op Call Log\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Op Call Log frequencies\nby City or village', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Call_Log_by_City_or_village(self):
        sql_str = """ call Fiscal_Call_Log_by_City_or_village(); """

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
                ("City_or_village", dp(50)),
                ("Fiscal_Call_frequency", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Call_Log_by_City_or_village = self.ids.Data_id
        Fiscal_Call_Log_by_City_or_village.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling Graph
        self.Fiscal_Call_Log_by_City_or_village_bar1()

        # Calling chart
        self.Fiscal_Call_Log_by_City_or_village_pie1()

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Call Log by City or village",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Call Log by City or village",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Call Log by City or village",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Call Log by City or village",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

    def Fiscal_Call_Log_by_City_or_village_Make(self):
        sql_str = """ call Fiscal_Call_Log_by_City_or_village_Make(); """

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
                ("City_or_village", dp(50)),
                ("Make", dp(40)),
                ("Make_frequency", dp(50)),
                ("Fiscal_Call_frequency", dp(60)),
                ("Call_Deposit_frequency", dp(60)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Call_Log_by_City_or_village_Make = self.ids.Data_id
        Fiscal_Call_Log_by_City_or_village_Make.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Call Log by City or village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Call Log by City or village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Call Log by City or village\nand Make",
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
                text="There is no Graph 1 for\nFiscal Call Log by City or village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Call Log by City or village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Call Log by City or village\nand Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    def Fiscal_Call_Log_by_City_or_village_Model(self):
        sql_str = """ call Fiscal_Call_Log_by_City_or_village_Model(); """

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
                ("City_or_village", dp(50)),
                ("Make", dp(40)),
                ("Model", dp(50)),
                ("Fiscal_Call_frequency", dp(50)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Call_Log_by_City_or_village_Model = self.ids.Data_id
        Fiscal_Call_Log_by_City_or_village_Model.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Call Log by City or village\nand Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Call Log by City or village\nand Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Call Log by City or village\nand Model",
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
                text="There is no Graph 1 for\nFiscal Call Log by City or village\nand Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Call Log by City or village\nand Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Call Log by City or village\nand Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # ***************************************************************
    # *********************** Vehicle viewing ***********************
    # ***************************************************************

    def Vehicle_viewing(self):
        sql_str = """ select a.Vehicle_viewing_id,
                    		a.Vehicle_of_interest,
                            a.V5C_id,
                            b.Make,
                            b.Model,
                            b.Reg_numb,
                            a.Nbr_Vehicles_viewed,
                            a.Customer_Age_Bracket,
                            a.Customer_sex,
                            a.City_or_village,
                            a.Viewing_date,
                            a.Viewing_time,
                            a.Deposit_Flag,
                            a.Sale_Flag,
                            a.Date_added

                    from icp.Op_vehicle_viewing as a left join
                    	 icp.V5C as b
                         on a.V5C_id = b.V5C_id; """

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
                ("Vehicle_viewing_id", dp(40)),
                ("Vehicle_of_interest", dp(50)),
                ("V5C_id", dp(30)),
                ("Make", dp(40)),
                ("Model", dp(50)),
                ("Reg_numb", dp(40)),

                ("Nbr_Vehicles_viewed", dp(40)),
                ("Customer_Age_Bracket", dp(40)),
                ("Customer_sex", dp(30)),
                ("City_or_village", dp(50)),

                ("Viewing_date", dp(30)),
                ("Viewing_time", dp(30)),
                ("Deposit_Flag", dp(30)),
                ("Sale_Flag", dp(30)),

                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Vehicle_viewing = self.ids.Data_id
        Vehicle_viewing.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nVehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nVehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nVehicle viewing all data",
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
                text="There is no Graph 1 for\nVehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nVehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nVehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # Bar graph for Vehicle viewing by make
    def Vehicle_viewing_by_Make_bar1(self):
        sql_str = """ select a.Make,
                    		count(b.V5C_id) as Viewing_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make
                         order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Viewing_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Viewing frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nfrequencies by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Viewing frequency", fontdict=font2)
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

    def Vehicle_viewing_by_Make_bar2(self):
        sql_str = """ select a.Make,
                            sum(b.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Sale_Flag = 1
                         group by a.Make
                         order by Sale_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nSale frequency by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
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

    def Vehicle_viewing_by_Make_bar3(self):
        sql_str = """ select a.Make,
                            sum(b.Deposit_Flag) as Deposit_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Deposit_Flag = 1
                         group by a.Make
                         order by Deposit_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nDeposit frequency by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Deposit frequency", fontdict=font2)
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

    # Vehicle viewing by Make pie chart
    def Vehicle_viewing_by_Make_pie1(self):
        sql_str = """ select a.Make,
                    		count(b.V5C_id) as Viewing_frequency,
                            sum(b.Deposit_Flag) as Deposit_frequency,
                            sum(b.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make
                         order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Viewing_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Vehicle viewing\nstatistics by Make", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing frequencies\nby Make', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_Make_pie2(self):
        sql_str = """ select a.Make,
                            sum(b.Deposit_Flag) as Deposit_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Deposit_Flag =1
                         group by a.Make
                         order by Deposit_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Vehicle viewing\nstatistics by Make", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nDeposit frequencies by Make', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_Make_pie3(self):
        sql_str = """ select a.Make,
                            sum(b.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Sale_Flag =1
                         group by a.Make
                         order by Sale_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Sale_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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
            textprops={'fontsize': 8},
            startangle=45)

        # For each wedge, set the corresponding text label color to the wedge's
        # face color.
        for i, patch in enumerate(patches):
            texts[i].set_color(patch.get_facecolor())

        plt.legend(title="Vehicle viewing\nstatistics by Make", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nSale frequencies by Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_Make(self):
        sql_str = """ select a.Make,
                    		count(b.V5C_id) as Viewing_frequency,
                            sum(b.Deposit_Flag) as Deposit_frequency,
                            sum(b.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make
                         order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting Deposit_frequency into type int
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].astype(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].astype(int)

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
                ("Make", dp(40)),
                ("Viewing_frequency", dp(40)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),

            ],
            row_data=Ar_tup
        )

        Vehicle_viewing_by_Make = self.ids.Data_id
        Vehicle_viewing_by_Make.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the Graph
        self.Vehicle_viewing_by_Make_bar1()
        self.Vehicle_viewing_by_Make_bar2()
        self.Vehicle_viewing_by_Make_bar3()

        # Calling the pie chart
        self.Vehicle_viewing_by_Make_pie1()
        self.Vehicle_viewing_by_Make_pie2()
        self.Vehicle_viewing_by_Make_pie3()

    # **************** Vehicle viewing by Model ****************
    # Bar graph for Vehicle viewing by Model
    def Vehicle_viewing_by_Model_bar1(self):
        sql_str = """ select a.Make,
                            a.Model,
                    		count(b.V5C_id) as Viewing_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make, a.Model
                         order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Viewing_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Viewing frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nfrequencies by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Viewing frequency", fontdict=font2)
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

    def Vehicle_viewing_by_Model_bar2(self):
        sql_str = """ select a.Make,
                            a.Model,
                            sum(b.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Sale_Flag = 1
                         group by a.Make, a.Model
                         order by Sale_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nSale frequency by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
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

    def Vehicle_viewing_by_Model_bar3(self):
        sql_str = """ select a.Make,
                            a.Model,
                            sum(b.Deposit_Flag) as Deposit_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Deposit_Flag = 1
                         group by a.Make, a.Model
                         order by Deposit_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nDeposit frequency by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Deposit frequency", fontdict=font2)
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

    # Vehicle viewing by Make pie chart
    def Vehicle_viewing_by_Model_pie1(self):
        sql_str = """ select a.Make,
                            a.Model,
                    		count(b.V5C_id) as Viewing_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         group by a.Make, a.Model
                         order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Viewing_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing frequencies\nby Model', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_Model_pie2(self):
        sql_str = """ select a.Make,
                            a.Model,
                            sum(b.Deposit_Flag) as Deposit_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Deposit_Flag =1
                         group by a.Make, a.Model
                         order by Deposit_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nDeposit frequencies by Model', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_Model_pie3(self):
        sql_str = """ select a.Make,
                            a.Model,
                            sum(b.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as b left join
                    	 icp.V5C as a
                         on b.V5C_id = a.V5C_id
                         where b.Sale_Flag =1
                         group by a.Make, a.Model
                         order by Sale_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Sale_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics by Model", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nSale frequencies by Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_Model(self):
        sql_str = """ select  a.Make,
                            a.Model,
                    		count(b.V5C_id) as Viewing_frequency,
                            sum(b.Deposit_Flag) as Deposit_frequency,
                            sum(b.Sale_Flag) as Sale_frequency
                        from icp.Op_vehicle_viewing as b left join
                        	 icp.V5C as a
                             on b.V5C_id = a.V5C_id
                             group by a.Make, a.Model
                             order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing the data type for Sale_frequency and Deposit_frequency
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].apply(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].apply(int)

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
                ("Make", dp(40)),
                ("Model", dp(50)),
                ("Viewing_frequency", dp(40)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),

            ],
            row_data=Ar_tup
        )

        Vehicle_viewing_by_Model = self.ids.Data_id
        Vehicle_viewing_by_Model.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the Graph
        self.Vehicle_viewing_by_Model_bar1()
        self.Vehicle_viewing_by_Model_bar2()
        self.Vehicle_viewing_by_Model_bar3()

        # Calling the pie chart
        self.Vehicle_viewing_by_Model_pie1()
        self.Vehicle_viewing_by_Model_pie2()
        self.Vehicle_viewing_by_Model_pie3()

    # ***********************************************
    # ****** Vehicle viewing by City or village *****
    # ***********************************************

    # Bar graph for Vehicle viewing by City or village
    def Vehicle_viewing_by_City_or_village_bar1(self):
        sql_str = """ select City_or_village,
                        count(Vehicle_viewing_id) as Viewing_frequency
                    from icp.Op_vehicle_viewing
                    group by City_or_village
                    order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        v = mydata['Viewing_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Viewing frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nfrequencies by City or village", fontdict=font1)
        plt.xlabel("City or village", fontdict=font2)
        plt.ylabel("Viewing frequency", fontdict=font2)
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

    def Vehicle_viewing_by_City_or_village_bar2(self):
        sql_str = """ select City_or_village,
                        count(Vehicle_viewing_id) as Viewing_frequency,
                        sum(Deposit_Flag) as Deposit_frequency,
                        sum(Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing
                    group by City_or_village
                    order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nDeposit frequency by City or village", fontdict=font1)
        plt.xlabel("City or village", fontdict=font2)
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

    def Vehicle_viewing_by_City_or_village_bar3(self):
        sql_str = """ select City_or_village,
                        count(Vehicle_viewing_id) as Viewing_frequency,
                        sum(Deposit_Flag) as Deposit_frequency,
                        sum(Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing
                    group by City_or_village
                    order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Vehicle viewing\nSale frequency by City or village", fontdict=font1)
        plt.xlabel("City or village", fontdict=font2)
        plt.ylabel("Sale frequency", fontdict=font2)
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

    # Vehicle viewing by Make pie chart
    def Vehicle_viewing_by_City_or_village_pie1(self):
        sql_str = """ select City_or_village,
                        count(Vehicle_viewing_id) as Viewing_frequency,
                        sum(Deposit_Flag) as Deposit_frequency,
                        sum(Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing
                    group by City_or_village
                    order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        w = mydata['Viewing_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing frequencies\nby City or village', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_City_or_village_pie2(self):
        sql_str = """ select City_or_village,
                        count(Vehicle_viewing_id) as Viewing_frequency,
                        sum(Deposit_Flag) as Deposit_frequency,
                        sum(Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing
                    where Deposit_Flag = 1
                    group by City_or_village
                    order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        w = mydata['Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nDeposit frequencies by City or village', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_City_or_village_pie3(self):
        sql_str = """ select City_or_village,
                        count(Vehicle_viewing_id) as Viewing_frequency,
                        sum(Deposit_Flag) as Deposit_frequency,
                        sum(Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing
                    where Sale_Flag = 1
                    group by City_or_village
                    order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        w = mydata['Sale_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nSale frequencies by City or village', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_City_or_village(self):
        sql_str = """ select City_or_village,
                        count(Vehicle_viewing_id) as Viewing_frequency,
                        sum(Deposit_Flag) as Deposit_frequency,
                        sum(Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing
                    group by City_or_village
                    order by Viewing_frequency desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing data type for Deposit_frequency and Sale_frequency
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].astype(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].astype(int)

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
                ("City_or_village", dp(50)),
                ("Viewing_frequency", dp(40)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Vehicle_viewing_by_City_or_village = self.ids.Data_id
        Vehicle_viewing_by_City_or_village.add_widget(table)

        # Calling the graphs
        self.Vehicle_viewing_by_City_or_village_bar1()
        self.Vehicle_viewing_by_City_or_village_bar2()
        self.Vehicle_viewing_by_City_or_village_bar3()

        # Calling the charts
        self.Vehicle_viewing_by_City_or_village_pie1()
        self.Vehicle_viewing_by_City_or_village_pie2()
        self.Vehicle_viewing_by_City_or_village_pie3()

        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_City_or_village_Make(self):
        sql_str = """ select a.City_or_village,
                    		b.Make,
                    		count(a.Vehicle_viewing_id) as Viewing_frequency,
                            sum(a.Deposit_Flag) as Deposit_frequency,
                            sum(a.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as a left join
                    	 icp.V5C as b
                         on a.V5C_id = b.V5C_id
                    group by a.City_or_village, b.Make
                    order by Viewing_frequency desc, a.City_or_village; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing data type for Deposit_frequency and Sale_frequency
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].astype(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].astype(int)

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
                ("City_or_village", dp(50)),
                ("Make", dp(40)),
                ("Viewing_frequency", dp(40)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Vehicle_viewing_by_City_or_village_Make = self.ids.Data_id
        Vehicle_viewing_by_City_or_village_Make.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nVehicle viewing by City or village and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nVehicle viewing by City or village and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nVehicle viewing by City or village and Make",
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
                text="There is no Graph 1 for\nVehicle viewing by City or village and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nVehicle viewing by City or village and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nVehicle viewing by City or village and Make",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    def Vehicle_viewing_by_City_or_village_Model(self):
        sql_str = """ select a.City_or_village,
                    		b.Make,
                            b.Model,
                    		count(a.Vehicle_viewing_id) as Viewing_frequency,
                            sum(a.Deposit_Flag) as Deposit_frequency,
                            sum(a.Sale_Flag) as Sale_frequency
                    from icp.Op_vehicle_viewing as a left join
                    	 icp.V5C as b
                         on a.V5C_id = b.V5C_id
                    group by a.City_or_village, b.Make, b.Model
                    order by Viewing_frequency desc, a.City_or_village; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing data type for Deposit_frequency and Sale_frequency
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].astype(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].astype(int)

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
                ("City_or_village", dp(50)),
                ("Make", dp(40)),
                ("Model", dp(40)),
                ("Viewing_frequency", dp(40)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Vehicle_viewing_by_City_or_village_Model = self.ids.Data_id
        Vehicle_viewing_by_City_or_village_Model.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nVehicle viewing by City or village and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nVehicle viewing by City or village and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nVehicle viewing by City or village and Model",
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
                text="There is no Graph 1 for\nVehicle viewing by City or village and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nVehicle viewing by City or village and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nVehicle viewing by City or village and Model",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # **********************************************
    # *************** Fiscal viewing ***************
    # **********************************************

    def Fiscal_vehicle_viewing(self):
        sql_str = """ call Fiscal_Vehicle_viewing_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing the time format
        mydata['Viewing_time'] = pd.to_datetime(mydata['Viewing_time'])
        mydata['Viewing_time'] = mydata['Viewing_time'].dt.strftime('%H:%M:%S')

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
                ("Vehicle_viewing_id", dp(40)),
                ("Vehicle_of_interest", dp(50)),
                ("V5C_id", dp(30)),
                ("Make", dp(40)),

                ("Model", dp(50)),
                ("Reg_numb", dp(40)),
                ("Nbr_Vehicles_viewed", dp(40)),
                ("Customer_Age_Bracket", dp(40)),

                ("Customer_sex", dp(30)),
                ("City_or_village", dp(50)),
                ("Viewing_date", dp(30)),
                ("financial_year", dp(30)),

                ("Viewing_time", dp(40)),
                ("Deposit_Flag", dp(30)),
                ("Sale_Flag", dp(30)),
                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_vehicle_viewing_all_data = self.ids.Data_id
        Fiscal_vehicle_viewing_all_data.add_widget(table)

        # Adding text place-holder for Charts as no charts is drawn
        # from the data above
        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal vehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal vehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal vehicle viewing all data",
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
                text="There is no Graph 1 for\nFiscal vehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal vehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal vehicle viewing all data",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 0, 0, 1),
                font_style='H3',
            )
        )
        # Closing the database connection
        cnn.close()

    # Bar graph for Vehicle viewing by make
    def Fiscal_Vehicle_viewing_by_Make_bar1(self):
        sql_str = """ call Fiscall_Make_Viewing_frequency_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Fiscal_Viewing_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Fiscal viewing frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nfrequencies by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Viewing frequency", fontdict=font2)
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

    def Fiscal_Vehicle_viewing_by_Make_bar2(self):
        sql_str = """ call Fiscall_Make_Viewing_frequency_Deposit_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nDeposit frequency by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
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

    def Fiscal_Vehicle_viewing_by_Make_bar3(self):
        sql_str = """ call Fiscall_Make_Viewing_frequency_Sale_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nSale frequency by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Sale frequency", fontdict=font2)
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

    # Vehicle viewing by Make pie chart
    def Fiscal_Vehicle_viewing_by_Make_pie1(self):
        sql_str = """ call Fiscall_Make_Viewing_frequency_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Fiscal_Viewing_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Fiscal vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal vehicle viewing\nfrequencies by Make', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Vehicle_viewing_by_Make_pie2(self):
        sql_str = """ call Fiscall_Make_Viewing_frequency_Deposit_call();"""

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nDeposit frequencies by Make', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Vehicle_viewing_by_Make_pie3(self):
        sql_str = """ call Fiscall_Make_Viewing_frequency_Sale_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Sale_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nSale frequencies by Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_vehicle_viewing_Make(self):
        sql_str = """ call Fiscall_Make_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing the data type for Deposit and Sale frequencies
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].astype(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].astype(int)

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
                ("Make", dp(40)),
                ("Fiscall_Viewing_frequency", dp(50)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_vehicle_viewing_by_Make = self.ids.Data_id
        Fiscal_vehicle_viewing_by_Make.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Call the Graphs
        self.Fiscal_Vehicle_viewing_by_Make_bar1()
        self.Fiscal_Vehicle_viewing_by_Make_bar2()
        self.Fiscal_Vehicle_viewing_by_Make_bar3()

        # Call the charts
        self.Fiscal_Vehicle_viewing_by_Make_pie1()
        self.Fiscal_Vehicle_viewing_by_Make_pie2()
        self.Fiscal_Vehicle_viewing_by_Make_pie3()

    # ******************************************
    # ***** Fiscal Vehicle viewing by Model ****
    # ******************************************

    # Bar graph for Vehicle viewing by Model
    def Fiscal_Vehicle_viewing_by_Model_bar1(self):
        sql_str = """ call Fiscal_Model_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Fiscal_Viewing_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Fiscal viewing frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nfrequencies by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Viewing frequency", fontdict=font2)
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

    def Fiscal_Vehicle_viewing_by_Model_bar2(self):
        sql_str = """ call Fiscal_Model_Viewing_Deposit_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nDeposit frequency by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
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

    def Fiscal_Vehicle_viewing_by_Model_bar3(self):
        sql_str = """ call Fiscal_Model_Viewing_Sale_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nSale frequency by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Sale frequency", fontdict=font2)
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

    # Vehicle viewing by Make pie chart
    def Fiscal_Vehicle_viewing_by_Model_pie1(self):
        sql_str = """ call Fiscal_Model_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Fiscal_Viewing_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Fiscal vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal vehicle viewing\nfrequencies by Model', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Vehicle_viewing_by_Model_pie2(self):
        sql_str = """ call Fiscal_Model_Viewing_Deposit_frequency_call();"""

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Deposit_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nDeposit frequencies by Model', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Vehicle_viewing_by_Model_pie3(self):
        sql_str = """ call Fiscal_Model_Viewing_Sale_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Sale_frequency'].to_numpy()

        mylabels = x

        # programme flow for colors to be used: retrieved via an import
        mycolors = Chart_colors.Retrieve_chart_colors(self, x)

        # calculating the number of items for the exploded pie chart
        myexplode = []
        for a in range(len(x)):
            myexplode.append(0.1)

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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nSale frequencies by Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_vehicle_viewing_Model(self):
        sql_str = """ call Fiscal_Model_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing the data type for Deposit and Sale frequencies
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].astype(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].astype(int)

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
                ("Make", dp(40)),
                ("Model", dp(50)),
                ("Fiscal_Viewing_frequency", dp(40)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_vehicle_viewing_by_Model = self.ids.Data_id
        Fiscal_vehicle_viewing_by_Model.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the Graphs
        self.Fiscal_Vehicle_viewing_by_Model_bar1()
        self.Fiscal_Vehicle_viewing_by_Model_bar2()
        self.Fiscal_Vehicle_viewing_by_Model_bar3()

        # Calling the Charts
        self.Fiscal_Vehicle_viewing_by_Model_pie1()
        self.Fiscal_Vehicle_viewing_by_Model_pie2()
        self.Fiscal_Vehicle_viewing_by_Model_pie3()

    # ****************************************************
    # ***** Fiscal Vehicle viewing by City_or_village ****
    # ****************************************************

    # Bar graph for Vehicle viewing by City_or_village
    def Fiscal_Vehicle_viewing_by_City_or_village_bar1(self):
        sql_str = """ call Fiscall_City_or_village_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        v = mydata['Fiscal_Viewing_frequency'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Fiscal viewing frequency")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nfrequencies by City or village", fontdict=font1)
        plt.xlabel("City_or_village", fontdict=font2)
        plt.ylabel("Viewing frequency", fontdict=font2)
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

    def Fiscal_Vehicle_viewing_by_City_or_village_bar2(self):
        sql_str = """ call Fiscall_City_or_village_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nDeposit frequency by City or village", fontdict=font1)
        plt.xlabel("City_or_village", fontdict=font2)
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

    def Fiscal_Vehicle_viewing_by_City_or_village_bar3(self):
        sql_str = """ call Fiscall_City_or_village_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
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

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal vehicle viewing\nSale frequency by City or village", fontdict=font1)
        plt.xlabel("City_or_village", fontdict=font2)
        plt.ylabel("Sale frequency", fontdict=font2)
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

    # Vehicle viewing by City_or_village pie chart
    def Fiscal_Vehicle_viewing_by_City_or_village_pie1(self):
        sql_str = """ call Fiscall_City_or_village_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
        w = mydata['Fiscal_Viewing_frequency'].to_numpy()

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

        plt.legend(title="Fiscal vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal vehicle viewing\nfrequencies by City or village', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Vehicle_viewing_by_City_or_village_pie2(self):
        sql_str = """ call Fiscall_City_or_village_Viewing_frequency_call();"""

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nDeposit frequencies by City or village', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Vehicle_viewing_by_City_or_village_pie3(self):
        sql_str = """ call Fiscall_City_or_village_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['City_or_village'].to_numpy()
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

        plt.legend(title="Vehicle viewing\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Vehicle viewing\nSale frequencies by City or village', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_vehicle_viewing_City_or_village(self):
        sql_str = """ call Fiscall_City_or_village_Viewing_frequency_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing the data type for Deposit and Sale frequencies
        mydata['Deposit_frequency'] = mydata['Deposit_frequency'].astype(int)
        mydata['Sale_frequency'] = mydata['Sale_frequency'].astype(int)

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
                ("City_or_village", dp(40)),
                ("Fiscal_Viewing_frequency", dp(50)),
                ("Deposit_frequency", dp(40)),
                ("Sale_frequency", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_vehicle_viewing_by_Model = self.ids.Data_id
        Fiscal_vehicle_viewing_by_Model.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the Graphs
        self.Fiscal_Vehicle_viewing_by_City_or_village_bar1()
        self.Fiscal_Vehicle_viewing_by_City_or_village_bar2()
        self.Fiscal_Vehicle_viewing_by_City_or_village_bar3()

        # Calling the Charts
        self.Fiscal_Vehicle_viewing_by_City_or_village_pie1()
        self.Fiscal_Vehicle_viewing_by_City_or_village_pie2()
        self.Fiscal_Vehicle_viewing_by_City_or_village_pie3()

    # ************************************************************
    # **************** Revenue and Profit by Make ****************
    # ************************************************************

    def Revenue_and_Profit_by_Make_bar1(self):
        sql_str = """ select a.Make,
                        sum(distinct ifnull(c.Deposit_Amount,0)) as Deposit_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make
                        order by Deposit_Revenue desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Deposit_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Deposit revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Deposit revenue by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Revenue_and_Profit_by_Make_bar2(self):
        sql_str = """ select a.Make,
                		sum(distinct ifnull(b.Sale_Amount,0)) as Sale_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make
                        order by Sale_Revenue desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Sale_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Sale revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Sale revenue by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Revenue_and_Profit_by_Make_bar3(self):
        sql_str = """ select a.Make,
                		sum(distinct ifnull(b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) as Total_Revenue,
                		sum(distinct ifnull(e.Total,0)) as Vehicle_Purchase_Price,
                        sum(distinct ifnull( b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) - sum(distinct ifnull(d.Price,0)) - sum(distinct ifnull(e.Total,0)) as Profit

                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make
                        order by Total_Revenue desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Total_Revenue'].to_numpy()
        y = mydata['Vehicle_Purchase_Price'].to_numpy()
        z = mydata['Profit'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Revenue")
        plt.bar(bar2, y, w, color="#E65100", label="Vehicle Purchase Price")
        plt.bar(bar3, z, w, color="#C6FF00", label="Profit")

        # Aligning the spacing of the bars to the center between the the bars
        plt.xticks(bar1 + w, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Total revenue & Profit by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Revenues (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        # Adding value labels to go on top of the bars
        # for i in range(len(x)):
        #     plt.text(i, v[i], v[i], ha="center", va="bottom")
        #     plt.text(i + w, y[i], y[i], ha="center", va="bottom")
        #     plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Make_pie1(self):
        sql_str = """ select a.Make,
                        sum(distinct ifnull(c.Deposit_Amount,0)) as Deposit_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make
                        order by Deposit_Revenue desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Deposit_Revenue'].to_numpy()

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

        plt.legend(title="Deposit revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Deposit revenue\nby Make', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Make_pie2(self):
        sql_str = """ select a.Make,
                		sum(distinct ifnull(b.Sale_Amount,0)) as Sale_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make
                        order by Sale_Revenue desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Sale_Revenue'].to_numpy()

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

        plt.legend(title="Sale revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Sale revenue\nby Make', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Make_pie3(self):
        sql_str = """ select a.Make,
                		sum(distinct ifnull( b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) - sum(distinct ifnull(d.Price,0)) - sum(distinct ifnull(e.Total,0)) as Profit
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make
                        order by Profit desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Profit'].to_numpy()

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

        plt.legend(title="Profit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Profit\nby Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Make(self):
        # Note: not all vehicles have an entry in Auction invoice so the calculations may seem incorrect
        # This also demonstrates why auction invoice is a table that must be populated after V5C insert
        sql_str = """ select a.Make,
                		count(distinct a.V5C_id) as Make_frequency,
                        count(distinct d.Serv_Invoice_nbr) as Service_frequency,
                		sum(distinct ifnull(d.Price,0)) as Service_Cost,
                        sum(distinct ifnull(c.Deposit_Amount,0)) as Deposit_Revenue,
                		sum(distinct ifnull(b.Sale_Amount,0)) as Sale_Revenue,
                		sum(distinct ifnull(b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) as Total_Revenue,
                		sum(distinct ifnull(e.Total,0)) as Vehicle_Purchase_Price,
                        sum(distinct ifnull( b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) - sum(distinct ifnull(d.Price,0)) - sum(distinct ifnull(e.Total,0)) as Profit

                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id

                        group by a.Make
                        order by Total_Revenue desc; """

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
                ("Make", dp(40)),
                ("Make_frequency", dp(50)),
                ("Service_frequency", dp(40)),

                ("Service_Cost", dp(40)),
                ("Deposit_Revenue", dp(50)),
                ("Sale_Revenue", dp(40)),

                ("Total_Revenue", dp(40)),
                ("Vehicle_Purchase_Price", dp(50)),
                ("Profit", dp(40)),
            ],
            row_data=Ar_tup
        )
        Revenue_and_Profit_by_Make_id = self.ids.Data_id
        Revenue_and_Profit_by_Make_id.add_widget(table)
        # Closing the database connection
        cnn.close()

        # Calling the Graphs
        self.Revenue_and_Profit_by_Make_bar1()
        self.Revenue_and_Profit_by_Make_bar2()
        self.Revenue_and_Profit_by_Make_bar3()

        # Calling the Charts
        self.Revenue_and_Profit_by_Make_pie1()
        self.Revenue_and_Profit_by_Make_pie2()
        self.Revenue_and_Profit_by_Make_pie3()

    # *************************************************************
    # **************** Revenue and Profit by Model ****************
    # *************************************************************

    def Revenue_and_Profit_by_Model_bar1(self):
        sql_str = """ select a.Make,
                        a.Model,
                        sum(distinct ifnull(c.Deposit_Amount,0)) as Deposit_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make, a.Model
                        order by Deposit_Revenue desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Deposit_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Deposit revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Deposit revenue by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Revenue_and_Profit_by_Model_bar2(self):
        sql_str = """ select a.Make,
                        a.Model,
                		sum(distinct ifnull(b.Sale_Amount,0)) as Sale_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make, a.Model
                        order by Sale_Revenue desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Sale_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Sale revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Sale revenue by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Revenue_and_Profit_by_Model_bar3(self):
        sql_str = """ select a.Make,
                        a.Model,
                		sum(distinct ifnull(b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) as Total_Revenue,
                		sum(distinct ifnull(e.Total,0)) as Vehicle_Purchase_Price,
                        sum(distinct ifnull( b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) - sum(distinct ifnull(d.Price,0)) - sum(distinct ifnull(e.Total,0)) as Profit
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make, a.Model
                        order by Total_Revenue desc; """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Total_Revenue'].to_numpy()
        y = mydata['Vehicle_Purchase_Price'].to_numpy()
        z = mydata['Profit'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Revenue")
        plt.bar(bar2, y, w, color="#E65100", label="Vehicle Purchase Price")
        plt.bar(bar3, z, w, color="#C6FF00", label="Profit")

        # Aligning the spacing of the bars to the center between the the bars
        plt.xticks(bar1 + w, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Total revenue & Profit by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Revenues (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        # Adding value labels to go on top of the bars
        # for i in range(len(x)):
        #     plt.text(i, v[i], v[i], ha="center", va="bottom")
        #     plt.text(i + w, y[i], y[i], ha="center", va="bottom")
        #     plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Model_pie1(self):
        sql_str = """ select a.Make,
                        a.Model,
                        sum(distinct ifnull(c.Deposit_Amount,0)) as Deposit_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make, a.Model
                        order by Deposit_Revenue desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Deposit_Revenue'].to_numpy()

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

        plt.legend(title="Deposit revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Deposit revenue\nby Model', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Model_pie2(self):
        sql_str = """ select a.Make,
                        a.Model,
                		sum(distinct ifnull(b.Sale_Amount,0)) as Sale_Revenue
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make, a.Model
                        order by Sale_Revenue desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Sale_Revenue'].to_numpy()

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

        plt.legend(title="Sale revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Sale revenue\nby Model', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Model_pie3(self):
        sql_str = """ select a.Make,
                        a.Model,
                		sum(distinct ifnull( b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) - sum(distinct ifnull(d.Price,0)) - sum(distinct ifnull(e.Total,0)) as Profit
                        from icp.V5C as a left join
                        	 icp.Sale as b
                        		on a.V5C_id= b.V5C_id
                        		left join
                             icp.Deposit as c
                        		on a.V5C_id = c.V5C_id
                                left join
                        	icp.Op_service as d
                        		on a.V5C_id = d.V5C_id
                        	left join
                        	icp.Auction_invoice as e
                        	on a.V5C_id = e.V5C_id
                        group by a.Make, a.Model
                        order by Profit desc; """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Profit'].to_numpy()

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

        plt.legend(title="Profit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Profit\nby Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Revenue_and_Profit_by_Model(self):
        sql_str = """ select a.Make,
                		a.Model,
                		count(distinct a.V5C_id) as Model_frequency,
                        count(distinct d.Serv_Invoice_nbr) as Service_frequency,
                		sum(distinct ifnull(d.Price,0)) as Service_Cost,
                        sum(distinct ifnull(c.Deposit_Amount,0)) as Deposit_Revenue,
                		sum(distinct ifnull(b.Sale_Amount,0)) as Sale_Revenue,
                		sum(distinct ifnull(b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) as Total_Revenue,
                		sum(distinct ifnull(e.Total,0)) as Vehicle_Purchase_Price,
                        sum(distinct ifnull( b.Sale_Amount,0))+ sum(distinct ifnull(c.Deposit_Amount,0)) - sum(distinct ifnull(d.Price,0)) - sum(distinct ifnull(e.Total,0)) as Profit

                    from icp.V5C as a left join
                    	 icp.Sale as b
                    		on a.V5C_id= b.V5C_id
                    		left join
                         icp.Deposit as c
                    		on a.V5C_id = c.V5C_id
                            left join
                    	icp.Op_service as d
                    		on a.V5C_id = d.V5C_id
                    	left join
                    	icp.Auction_invoice as e
                    	on a.V5C_id = e.V5C_id

                    group by a.Make, a.Model
                    order by Total_Revenue desc; """

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
                ("Make", dp(40)),
                ("Model", dp(50)),
                ("Model_frequency", dp(40)),
                ("Service_frequency", dp(40)),

                ("Service_Cost", dp(40)),
                ("Deposit_Revenue", dp(40)),
                ("Sale_Revenue", dp(40)),

                ("Total_Revenue", dp(40)),
                ("Vehicle_Purchase_Price", dp(50)),
                ("Profit", dp(30)),
            ],
            row_data=Ar_tup
        )

        Revenue_and_Profit_by_Model_id = self.ids.Data_id
        Revenue_and_Profit_by_Model_id.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the Graphs
        self.Revenue_and_Profit_by_Model_bar1()
        self.Revenue_and_Profit_by_Model_bar2()
        self.Revenue_and_Profit_by_Model_bar3()

        # Calling the Charts
        self.Revenue_and_Profit_by_Model_pie1()
        self.Revenue_and_Profit_by_Model_pie2()
        self.Revenue_and_Profit_by_Model_pie3()

    # *******************************************************************
    # **************** Fiscal Revenue and Profit by Make ****************
    # *******************************************************************

    def Fiscal_Revenue_and_Profit_by_Make_bar1(self):
        sql_str = """ call Fiscal_Deposit_Revenue_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Deposit_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Deposit revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Deposit revenue by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Fiscal_Revenue_and_Profit_by_Make_bar2(self):
        sql_str = """ call Fiscal_Sale_Revenue_by_Make_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Sale_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Sale revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Sale revenue by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Fiscal_Revenue_and_Profit_by_Make_bar3(self):
        sql_str = """ call Fiscall_Total_Revenue_and_Profit_by_Make_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        v = mydata['Total_Revenue'].to_numpy()
        y = mydata['Vehicle_Purchase_Price'].to_numpy()
        z = mydata['Profit'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Revenue")
        plt.bar(bar2, y, w, color="#E65100", label="Vehicle Purchase Price")
        plt.bar(bar3, z, w, color="#C6FF00", label="Profit")

        # Aligning the spacing of the bars to the center between the the bars
        plt.xticks(bar1 + w, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Total revenue & Profit by Make", fontdict=font1)
        plt.xlabel("Make", fontdict=font2)
        plt.ylabel("Revenues (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        # Adding value labels to go on top of the bars
        # for i in range(len(x)):
        #     plt.text(i, v[i], v[i], ha="center", va="bottom")
        #     plt.text(i + w, y[i], y[i], ha="center", va="bottom")
        #     plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Make_pie1(self):
        sql_str = """ call Fiscal_Deposit_Revenue_by_Make_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Deposit_Revenue'].to_numpy()

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

        plt.legend(title="Fiscal Deposit revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Deposit revenue\nby Make', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Make_pie2(self):
        sql_str = """ call Fiscal_Sale_Revenue_by_Make_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Sale_Revenue'].to_numpy()

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

        plt.legend(title="Fiscal Sale revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Sale revenue\nby Make', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Make_pie3(self):
        sql_str = """call Fiscall_Total_Revenue_and_Profit_by_Make_call();"""

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Make'].to_numpy()
        w = mydata['Profit'].to_numpy()

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

        plt.legend(title="Fiscal Profit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Profit\nby Make', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Make(self):
        sql_str = """ call Fiscall_Revenue_and_Profit_by_Make_call(); """

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
                ("Make", dp(40)),
                ("Make_frequency", dp(50)),
                ("Service_frequency", dp(40)),
                ("Service_Cost", dp(40)),
                ("Deposit_Revenue", dp(50)),
                ("Sale_Revenue", dp(40)),
                ("Total_Revenue", dp(40)),
                ("Vehicle_Purchase_Price", dp(50)),
                ("Profit", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Revenue_and_Profit_by_Make = self.ids.Data_id
        Fiscal_Revenue_and_Profit_by_Make.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the Graphs
        self.Fiscal_Revenue_and_Profit_by_Make_bar1()
        self.Fiscal_Revenue_and_Profit_by_Make_bar2()
        self.Fiscal_Revenue_and_Profit_by_Make_bar3()

        # Calling the Charts
        self.Fiscal_Revenue_and_Profit_by_Make_pie1()
        self.Fiscal_Revenue_and_Profit_by_Make_pie2()
        self.Fiscal_Revenue_and_Profit_by_Make_pie3()

    # ********************************************************************
    # **************** Fiscal Revenue and Profit by Model ****************
    # ********************************************************************

    def Fiscal_Revenue_and_Profit_by_Model_bar1(self):
        sql_str = """ call Fiscal_Deposit_Revenue_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Deposit_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Deposit revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Deposit revenue by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Fiscal_Revenue_and_Profit_by_Model_bar2(self):
        sql_str = """ call Fiscal_Sale_Revenue_by_Model_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Sale_Revenue'].to_numpy()

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
        plt.bar(bar1, v, w, color="#D50000", label="Sale revenue")

        # Aligning the spacing of the bars to the center between the two bars
        plt.xticks(bar1, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Sale revenue by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Revenue (£)", fontdict=font2)
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

    def Fiscal_Revenue_and_Profit_by_Model_bar3(self):
        sql_str = """ call Fiscall_Total_Revenue_and_Profit_by_Model_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        v = mydata['Total_Revenue'].to_numpy()
        y = mydata['Vehicle_Purchase_Price'].to_numpy()
        z = mydata['Profit'].to_numpy()

        mylabels = x

        # Setting the width of the bars
        w = 0.1

        # setting the positions of the bars
        bar1 = np.arange(len(x))
        bar2 = [i+w for i in bar1]
        bar3 = [i+w for i in bar2]

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
        plt.bar(bar1, v, w, color="#D50000", label="Total Revenue")
        plt.bar(bar2, y, w, color="#E65100", label="Vehicle Purchase Price")
        plt.bar(bar3, z, w, color="#C6FF00", label="Profit")

        # Aligning the spacing of the bars to the center between the the bars
        plt.xticks(bar1 + w, x)

        # Add comma to the y axis values in thousands
        ax.set_yticklabels(['{:,}'.format(int(x)) for x in ax.get_yticks().tolist()])

        font1 = {'family': 'serif', 'color': 'lime', 'size': 20}
        font2 = {'family': 'serif', 'color': 'lime', 'size': 15}

        plt.title("Fiscal Total revenue & Profit by Model", fontdict=font1)
        plt.xlabel("Model", fontdict=font2)
        plt.ylabel("Revenues (£)", fontdict=font2)
        plt.grid(color='lime', linestyle='dashed', linewidth=0.5)
        plt.legend()

        # Adding value labels to go on top of the bars
        # for i in range(len(x)):
        #     plt.text(i, v[i], v[i], ha="center", va="bottom")
        #     plt.text(i + w, y[i], y[i], ha="center", va="bottom")
        #     plt.text(i + (2*w), z[i], z[i], ha="center", va="bottom")

        # rotating the x labels to fit the page
        plt.setp(ax.get_xticklabels(), rotation=10, ha="right", rotation_mode="anchor")

        Graph3 = self.ids.Graph3
        Graph3.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Model_pie1(self):
        sql_str = """ call Fiscal_Deposit_Revenue_by_Model_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Deposit_Revenue'].to_numpy()

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

        plt.legend(title="Fiscal Deposit revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Deposit revenue\nby Model', fontdict=font1)

        chart1 = self.ids.chart1
        chart1.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Model_pie2(self):
        sql_str = """ call Fiscal_Sale_Revenue_by_Model_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Sale_Revenue'].to_numpy()

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

        plt.legend(title="Fiscal Sale revenue\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Sale revenue\nby Model', fontdict=font1)

        chart2 = self.ids.chart2
        chart2.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Model_pie3(self):
        sql_str = """ call Fiscall_Total_Revenue_and_Profit_by_Model_call(); """

        # Changing mysql connection method
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Converting single columns from pandas dataframe to numpy array
        x = mydata['Model'].to_numpy()
        w = mydata['Profit'].to_numpy()

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

        plt.legend(title="Fiscal Profit\nstatistics", bbox_to_anchor=(1.60, 1))
        plt.title('Fiscal Profit\nby Model', fontdict=font1)

        chart3 = self.ids.chart3
        chart3.add_widget(FigureCanvasKivyAgg(plt.gcf()))

        # Closing the database connection
        cnn.close()

    def Fiscal_Revenue_and_Profit_by_Model(self):
        sql_str = """ call Fiscall_Revenue_and_Profit_by_Model_call(); """

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
                ("Make", dp(40)),
                ("Model", dp(40)),
                ("Model_frequency", dp(50)),
                ("Service_frequency", dp(40)),
                ("Service_Cost", dp(40)),
                ("Deposit_Revenue", dp(50)),
                ("Sale_Revenue", dp(40)),
                ("Total_Revenue", dp(40)),
                ("Vehicle_Purchase_Price", dp(50)),
                ("Profit", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Revenue_and_Profit_by_Model = self.ids.Data_id
        Fiscal_Revenue_and_Profit_by_Model.add_widget(table)

        # Closing the database connection
        cnn.close()

        # Calling the Graphs
        self.Fiscal_Revenue_and_Profit_by_Model_bar1()
        self.Fiscal_Revenue_and_Profit_by_Model_bar2()
        self.Fiscal_Revenue_and_Profit_by_Model_bar3()

        # Calling the Charts
        self.Fiscal_Revenue_and_Profit_by_Model_pie1()
        self.Fiscal_Revenue_and_Profit_by_Model_pie2()
        self.Fiscal_Revenue_and_Profit_by_Model_pie3()
