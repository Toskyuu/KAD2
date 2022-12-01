import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def draw_scatter_plot(table, first_column, second_column):
    pearson_corr = np.corrcoef(table[first_column], table[second_column])[0][1]
    a, b = np.polyfit(table[first_column], table[second_column], 1)
    plt.figure(figsize=(4.5, 4.5))
    plt.title('r = ' + str(round(pearson_corr, 2)) + ', y = ' + str(round(a, 1)) + 'x + ' + str(round(b, 1)))
    plt.scatter(table[first_column], table[second_column], c='darkcyan', s=80)
    plt.plot(table[first_column], a * table[first_column] + b, color='red')
    plt.xlabel(first_column)
    plt.ylabel(second_column)
    plt.show()


nazwy_kolumn = ['Długość Działki Kielicha(cm)', 'Szerokość Działki Kielicha(cm)', 'Długość Płatka(cm)',
                'Szerokość Płatka(cm)', 'Gatunek']
kwiatki = pd.read_csv('data.csv', names=nazwy_kolumn)

draw_scatter_plot(kwiatki, nazwy_kolumn[0], nazwy_kolumn[1])
draw_scatter_plot(kwiatki, nazwy_kolumn[0], nazwy_kolumn[2])
draw_scatter_plot(kwiatki, nazwy_kolumn[0], nazwy_kolumn[3])
draw_scatter_plot(kwiatki, nazwy_kolumn[1], nazwy_kolumn[2])
draw_scatter_plot(kwiatki, nazwy_kolumn[1], nazwy_kolumn[3])
draw_scatter_plot(kwiatki, nazwy_kolumn[2], nazwy_kolumn[3])
