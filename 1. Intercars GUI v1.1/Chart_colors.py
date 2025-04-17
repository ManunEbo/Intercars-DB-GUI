def Retrieve_chart_colors(self, x):
    # programme flow for colors to be used
    if len(x) == 1:
        mycolors = ["#D50000"]
    elif len(x) == 2:
        mycolors = ["#D50000", "#76FF03"]
    elif len(x) == 3:
        mycolors = ["#D50000", "#76FF03", "#FFFF00"]
    elif len(x) == 4:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE"]
    elif len(x) == 5:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00"]
    elif len(x) == 6:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00", "#D500F9"]
    elif len(x) == 7:
        mycolors = ["#D50000", "#76FF03", "#FFFF00",
                    "#304FFE", "#AEEA00", "#D500F9", "#6A1B9A"]
    elif len(x) == 8:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE",
                    "#AEEA00", "#D500F9", "#6A1B9A", "#E65100"]
    elif len(x) == 9:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE",
                    "#AEEA00", "#D500F9", "#6A1B9A", "#E65100", "#BDBDBD"]
    elif len(x) == 10:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00",
                    "#D500F9", "#6A1B9A", "#E65100", "#BDBDBD", "#43A047"]
    elif len(x) == 11:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00",
                    "#D500F9", "#6A1B9A", "#E65100", "#BDBDBD", "#43A047", "#FFA726"]
    elif len(x) == 12:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00", "#D500F9",
                    "#6A1B9A", "#E65100", "#BDBDBD", "#43A047", "#FFA726", "#827717"]
    elif len(x) == 13:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00", "#D500F9",
                    "#6A1B9A", "#E65100", "#BDBDBD", "#43A047", "#FFA726", "#827717", "#18FFFF"]
    elif len(x) == 14:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00", "#D500F9", "#6A1B9A",
                    "#E65100", "#BDBDBD", "#43A047", "#FFA726", "#827717", "#18FFFF", "#E64A19"]
    elif len(x) == 15:
        mycolors = ["#D50000", "#76FF03", "#FFFF00", "#304FFE", "#AEEA00", "#D500F9", "#6A1B9A",
                    "#E65100", "#BDBDBD", "#43A047", "#FFA726", "#827717", "#18FFFF", "#E64A19", "#F57C00"]
    return mycolors
