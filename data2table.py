#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# data2table.py
def data2table_gh(data):
    data = data.split("\n")
    spaltenbreiten = {}
    datentypen = {}

    # spaltenbreite bestimmen
    for i, item in enumerate(data):
        zeile = item.split(";")
        if i == 1:
            for i, item in enumerate(zeile):
                if item == "":
                    datentypen[i] = "str"
                elif item[0] in ["-", "+", "0",
                                 '1', '2', '3',
                                 '4', '5', '6',
                                 '7', '8', '9']:
                    datentypen[i] = "int"
                else:
                    datentypen[i] = "str"
        for j, item in enumerate(zeile):
            if j in spaltenbreiten.keys():
                if spaltenbreiten[j] < len(item):
                    spaltenbreiten[j] = len(item)
            else:
                spaltenbreiten[j] = len(item)#
    
    """
    # print string left aligned
    print("{0:<50}".format(string))

    # print string right aligned
    print("{0:>50}".format(string))
    """
    for i, item in enumerate(data):
        zeile = item.split(";")
        if i == 1:
            print("|", end="")
            for i, spalte in enumerate(spaltenbreiten):
                if datentypen[i] == "int":
                    print((spaltenbreiten[i] + 1) * "-" + ":", end="")
                elif datentypen[i] == "str":
                    print(":" + (spaltenbreiten[i] + 1) * "-", end="")
                print("|", end="")
            print()
        print("| ", end="")
        for i, spalte in enumerate(zeile):
            spaltenbreite = str(spaltenbreiten[i])
            if datentypen[i] == "int":
                # rechtsbündig
                formatstring = "{0:>"+ spaltenbreite +"}"
            else:
                # linksbündig
                formatstring = "{0:<"+ spaltenbreite +"}"
            print(formatstring.format(spalte), end=" | ")
        print()


def data2table_html(data):
    # bringt einen Datenbestand
    # in Form und printed es in
    # die Konsole
    data = data.split("\n")
    for i, line in enumerate(data):
        zeile = line.split(";")
        if i == 0:
            print('<table border="1px solid grey">')
            print('<thead><tr>')
            for item in zeile:
                print("  <th>{}</th>".format(item))
            print('</tr></thead>')
        else:
            print('<tr style="vertical-align:top">')
            for item in zeile:
                if item == "":
                    print('  <td></td>')
                elif item[0] in ['-', '+', '0',
                               '1', '2', '3',
                               '4', '5', '6',
                               '7', '8', '9']:
                    print('  <td style="text-align: right;">{}</td>'.format(item))
                else:
                    print('  <td>{}</td>'.format(item))
            print('</tr>')
    print("</table>")


def data2table_wiki(data):
    # bringt einen Datenbestand
    # in Form und printed es in
    # die Konsole
    data = data.split("\n")

    for i, line in enumerate(data):

        zeile = line.split(";")

        if i == 0:
            print('{| class="wikitable sortable"')
            for item in zeile:
                print("!", item)
        else:
            print('|- style="vertical-align:top"')
            for item in zeile:
                if item == "":
                    print('|')
                elif item[0] in ['-', '+', '0',
                               '1', '2', '3',
                               '4', '5', '6',
                               '7', '8', '9']:
                    print('| style="text-align: right;" |', item)
                else:
                    print('|', item)
    print("|}")
