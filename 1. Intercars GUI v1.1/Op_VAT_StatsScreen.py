from kivy.uix.screenmanager import Screen, ScreenManager

import mysql.connector
import numpy as np
import pandas as pd
from pandas.plotting import table

# Importing FPDF to create the PDF
from fpdf import FPDF

# Importing datetime
import datetime

# Importing matplotlib.pyplot for creating the PDF
import matplotlib.pyplot as plt

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


class Op_VAT_StatsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def chng_Screen(self, Scrn_name):
        self.manager.current = Scrn_name

    def Op_VAT_all_in_house_data(self):
        sql_str = """ call Op_VAT_stats_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing datatypes
        mydata['Auct_Invoice_id'] = mydata['Auct_Invoice_id'].fillna(0).astype(int)
        mydata['Op_service_id'] = mydata['Op_service_id'].fillna(0).astype(int)
        mydata['Op_misc_Receipt_id'] = mydata['Op_misc_Receipt_id'].fillna(0).astype(int)
        mydata['VAT_rate'] = mydata['VAT_rate'].fillna(0)
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
                ("Op_VAT_id", dp(30)),
                ("Auct_Invoice_id", dp(40)),
                ("Op_service_id", dp(40)),
                ("Op_misc_Receipt_id", dp(30)),
                ("Venue", dp(60)),
                ("Product_or_service", dp(60)),
                ("Gross_Price", dp(30)),
                ("VAT_rate", dp(30)),
                ("VAT", dp(30)),
                ("Net", dp(30)),
                ("Transaction_Date", dp(30)),
                ("Transaction_Time", dp(30)),
                ("financial_year", dp(30)),

                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Op_VAT_all_in_house_data = self.ids.Data_id
        Op_VAT_all_in_house_data.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nOp VAT all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nOp VAT all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nOp VAT all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nOp VAT all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nOp VAT all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nOp VAT all inhouse data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

    def Fiscal_Op_VAT_in_house_data(self):
        sql_str = """ call Fiscal_Op_VAT_stats_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Changing datatypes
        mydata['Auct_Invoice_id'] = mydata['Auct_Invoice_id'].fillna(0).astype(int)
        mydata['Op_service_id'] = mydata['Op_service_id'].fillna(0).astype(int)
        mydata['Op_misc_Receipt_id'] = mydata['Op_misc_Receipt_id'].fillna(0).astype(int)
        mydata['VAT_rate'] = mydata['VAT_rate'].fillna(0)
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
                ("Op_VAT_id", dp(30)),
                ("Auct_Invoice_id", dp(40)),
                ("Op_service_id", dp(40)),
                ("Op_misc_Receipt_id", dp(30)),
                ("Venue", dp(60)),
                ("Product_or_service", dp(60)),
                ("Gross_Price", dp(30)),
                ("VAT_rate", dp(30)),
                ("VAT", dp(30)),
                ("Net", dp(30)),
                ("Transaction_Date", dp(30)),
                ("Transaction_Time", dp(30)),
                ("financial_year", dp(30)),
                ("Date_added", dp(40)),
            ],
            row_data=Ar_tup
        )

        Fiscal_Op_VAT_in_house_data = self.ids.Data_id
        Fiscal_Op_VAT_in_house_data.add_widget(table)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Op VAT data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Op VAT data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Op VAT data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal Op VAT data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Op VAT data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Op VAT data",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

    def Fiscal_Op_VAT_stats_total(self):
        sql_str = """ call Fiscal_Op_VAT_stats_total_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        Total_Net = Ar_tup[0][0]
        Total_VAT = Ar_tup[0][1]
        Total_Gross = Ar_tup[0][2]

        Fiscal_Op_VAT_stats_total = self.ids.Data_id

        Fiscal_Op_VAT_stats_total.add_widget(
            MDLabel(
                text="[color=#FFCA28][b]Total Net:[/b][/color]      £{0:,}\n[color=#FFCA28][b]   Total VAT:[/b][/color]        £{1:,}\n[color=#FFCA28][b]  Total Gross:[/b][/color]      £{2:,}".format(
                    Total_Net, Total_VAT, Total_Gross),
                markup=True,
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Op VAT totals",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Op VAT totals",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Op VAT totals",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal Op VAT totals",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Op VAT totals",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Op VAT totals",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

    def Fiscal_Op_VAT_stats_PDF(self):
        sql_str = """ call Fiscal_Op_VAT_stats_call1(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Applying the thousands separator for Net, VAT and Gross price
        mydata['Gross_Price'] = mydata['Gross_Price'].fillna(0).apply('{:,}'.format)
        mydata['VAT'] = mydata['VAT'].fillna(0).apply('{:,}'.format)
        mydata['Net'] = mydata['Net'].fillna(0).apply('{:,}'.format)

        mydata['Gross_Price'] = mydata['Gross_Price'].astype(str)
        mydata['VAT'] = mydata['VAT'].astype(str)
        mydata['Net'] = mydata['Net'].astype(str)
        mydata['financial_year'] = mydata['financial_year'].fillna(0).astype(str)
        mydata['Transaction_Date'] = mydata['Transaction_Date'].astype(str)
        mydata['Transaction_Time'] = mydata['Transaction_Time'].astype(str)
        mydata['Date_added'] = mydata['Date_added'].astype(str)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        headers = mydata.columns.values
        length_headers = len(headers)

        title = "Intercars Leicester Fiscal VAT data"
        time = datetime.datetime.now()
        pdf = ".pdf"
        addr = "/home/kapanga/Documents/PDF_Folder/Fiscal VAT {0}{1}".format(time.date(), pdf)

        # Instantiating FPDF and setting the orientation to Landscape
        pdf = FPDF(orientation="L")

        # Creating a function to add the column headers to the table

        def render_table_header():
            pdf.set_font(style="B")  # enabling bold text
            for col_name in headers:
                pdf.cell(col_width, line_height, col_name, border=1)
            pdf.ln(line_height)
            pdf.set_font(style="")  # disabling bold text

        pdf.add_page()
        pdf.set_font("Times", size=8)
        line_height = pdf.font_size * 2.5
        col_width = pdf.epw / length_headers  # distribute content evenly
        pdf.set_title(title=title)

        render_table_header()
        for row in Ar_tup:
            if pdf.will_page_break(line_height):
                render_table_header()
            for datum in row:
                pdf.cell(col_width, line_height, datum, border=1)
            pdf.ln(line_height)

        pdf.output(addr)

        # Closing the database connection
        cnn.close()

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nFiscal Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nFiscal Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nFiscal Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nFiscal Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nFiscal Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nFiscal Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

    # ********************************************************
    # ************** Previous fiscal year ********************
    # ********************************************************
    # def Previous_Fiscal_Op_VAT_in_house_data(self):
    #     sql_str = """ call Fiscal_Op_VAT_stats_Previous_year_call1(); """
    #
    #     # database connection
    #     cnn = sql_import.db_connection(self)
    #     mydata = pd.read_sql_query(sql_str, cnn)
    #
    #     # Changing datatypes
    #     mydata['VAT_rate'] = mydata['VAT_rate'].fillna(0)
    #     # converting the pandas dataframe into a numpy array
    #     num_data = mydata.to_numpy()
    #
    #     # Reshaping the data ready for MDDataTable
    #     Ar_shape = num_data.reshape(num_data.shape)
    #
    #     Ar_tup = list(map(tuple, Ar_shape))
    #
    #     # Define Table
    #     table = MDDataTable(
    #         pos_hint={'center_x': 0.5, 'center_y': 0.5},
    #         size_hint=(1, 1),
    #
    #         check=True,
    #         use_pagination=True,
    #         rows_num=15,
    #         column_data=[
    #             ("Venue", dp(60)),
    #             ("Product_or_service", dp(60)),
    #             ("Gross_Price", dp(30)),
    #             ("VAT_rate", dp(30)),
    #             ("VAT", dp(30)),
    #             ("Net", dp(30)),
    #             ("Transaction_Date", dp(30)),
    #             ("Transaction_Time", dp(30)),
    #             ("financial_year", dp(30)),
    #             ("Date_added", dp(40)),
    #         ],
    #         row_data=Ar_tup
    #     )
    #
    #     Previous_Fiscal_Op_VAT_in_house_data = self.ids.Data_id
    #     Previous_Fiscal_Op_VAT_in_house_data.add_widget(table)
    #
    #     # Closing the database connection
    #     cnn.close()
    #
    #     Chart1 = self.ids.chart1
    #     Chart1.add_widget(
    #         MDLabel(
    #             text="There is no Chart 1 for\nPrevious fiscal Op VAT data",
    #             halign="center",
    #             theme_text_color="Custom",
    #             text_color=(118/255, 255/255, 3/255),
    #             font_style='H3',
    #         )
    #     )
    #
    #     Chart2 = self.ids.chart2
    #     Chart2.add_widget(
    #         MDLabel(
    #             text="There is no Chart 2 for\nPrevious fiscal Op VAT data",
    #             halign="center",
    #             theme_text_color="Custom",
    #             text_color=(118/255, 255/255, 3/255),
    #             font_style='H3',
    #         )
    #     )
    #
    #     Chart3 = self.ids.chart3
    #     Chart3.add_widget(
    #         MDLabel(
    #             text="There is no Chart 3 for\nPrevious fiscal Op VAT data",
    #             halign="center",
    #             theme_text_color="Custom",
    #             text_color=(118/255, 255/255, 3/255),
    #             font_style='H3',
    #         )
    #     )
    #
    #     # Adding text place-holders for Graphs
    #     Graph1 = self.ids.Graph1
    #     Graph1.add_widget(
    #         MDLabel(
    #             text="There is no Graph 1 for\nPrevious fiscal Op VAT data",
    #             halign="center",
    #             theme_text_color="Custom",
    #             text_color=(118/255, 255/255, 3/255),
    #             font_style='H3',
    #         )
    #     )
    #
    #     Graph2 = self.ids.Graph2
    #     Graph2.add_widget(
    #         MDLabel(
    #             text="There is no Graph 2 for\nPrevious fiscal Op VAT data",
    #             halign="center",
    #             theme_text_color="Custom",
    #             text_color=(118/255, 255/255, 3/255),
    #             font_style='H3',
    #         )
    #     )
    #
    #     Graph3 = self.ids.Graph3
    #     Graph3.add_widget(
    #         MDLabel(
    #             text="There is no Graph 3 for\nPrevious fiscal Op VAT data",
    #             halign="center",
    #             theme_text_color="Custom",
    #             text_color=(118/255, 255/255, 3/255),
    #             font_style='H3',
    #         )
    #     )

    def Previous_Fiscal_Op_VAT_stats_PDF(self):
        sql_str = """ call Fiscal_Op_VAT_stats_Previous_year_call(); """

        # database connection
        cnn = sql_import.db_connection(self)
        mydata = pd.read_sql_query(sql_str, cnn)

        # Applying the thousands separator for Net, VAT and Gross price
        mydata['Gross_Price'] = mydata['Gross_Price'].fillna(0).apply('{:,}'.format)
        mydata['VAT'] = mydata['VAT'].fillna(0).apply('{:,}'.format)
        mydata['Net'] = mydata['Net'].fillna(0).apply('{:,}'.format)

        mydata['Gross_Price'] = mydata['Gross_Price'].astype(str)
        mydata['VAT'] = mydata['VAT'].astype(str)
        mydata['Net'] = mydata['Net'].astype(str)
        mydata['financial_year'] = mydata['financial_year'].fillna(0).astype(str)
        mydata['Transaction_Date'] = mydata['Transaction_Date'].astype(str)
        mydata['Transaction_Time'] = mydata['Transaction_Time'].astype(str)
        mydata['Date_added'] = mydata['Date_added'].astype(str)

        # converting the pandas dataframe into a numpy array
        num_data = mydata.to_numpy()

        # Reshaping the data ready for MDDataTable
        Ar_shape = num_data.reshape(num_data.shape)

        Ar_tup = list(map(tuple, Ar_shape))

        headers = mydata.columns.values
        length_headers = len(headers)

        title = "Intercars Leicester previous fiscal year VAT data"
        time = datetime.datetime.now()
        pdf = ".pdf"
        addr = "/home/kapanga/Documents/PDF_Folder/Previous Fiscal year VAT {0}{1}".format(
            time.date(), pdf)

        # Instantiating FPDF and setting the orientation to Landscape
        pdf = FPDF(orientation="L")

        # Creating a function to add the column headers to the table

        def render_table_header():
            pdf.set_font(style="B")  # enabling bold text
            for col_name in headers:
                pdf.cell(col_width, line_height, col_name, border=1)
            pdf.ln(line_height)
            pdf.set_font(style="")  # disabling bold text

        pdf.add_page()
        pdf.set_font("Helvetica", size=8)
        line_height = pdf.font_size * 2.5
        col_width = pdf.epw / length_headers  # distribute content evenly
        pdf.set_title(title=title)

        render_table_header()
        for row in Ar_tup:
            if pdf.will_page_break(line_height):
                render_table_header()
            for datum in row:
                pdf.cell(col_width, line_height, datum, border=1)
            pdf.ln(line_height)

        pdf.output(addr)

        Chart1 = self.ids.chart1
        Chart1.add_widget(
            MDLabel(
                text="There is no Chart 1 for\nPrevious fiscal year Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart2 = self.ids.chart2
        Chart2.add_widget(
            MDLabel(
                text="There is no Chart 2 for\nPrevious fiscal year Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Chart3 = self.ids.chart3
        Chart3.add_widget(
            MDLabel(
                text="There is no Chart 3 for\nPrevious fiscal year Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        # Adding text place-holders for Graphs
        Graph1 = self.ids.Graph1
        Graph1.add_widget(
            MDLabel(
                text="There is no Graph 1 for\nPrevious fiscal year Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph2 = self.ids.Graph2
        Graph2.add_widget(
            MDLabel(
                text="There is no Graph 2 for\nPrevious fiscal year Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )

        Graph3 = self.ids.Graph3
        Graph3.add_widget(
            MDLabel(
                text="There is no Graph 3 for\nPrevious fiscal year Op VAT PDF",
                halign="center",
                theme_text_color="Custom",
                text_color=(118/255, 255/255, 3/255),
                font_style='H3',
            )
        )
