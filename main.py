import csv
from matplotlib import pyplot as plt
import math
def findMinimum(table, column):
    min = float(table[0][column])
    for x in kwiatki:
        if float(x[column]) < min:
            min = float(x[column])
    return min


def findMaximum(table, column):
    max = float(table[0][column])
    for x in kwiatki:
        if float(x[column]) > max:
            max = float(x[column])
    return max


def findQuantity(table, column, searched_value):
    quantity_searched_value = 0
    for x in table:
        if int(x[column]) == searched_value:
            quantity_searched_value = quantity_searched_value + 1
    return quantity_searched_value


def findAverage(table, column):
    sum = 0.0
    for x in table:
        sum += float(x[column])
    return sum / len(table)


def findMedian(table, column):
    table_to_sort = []
    for x in table:
        table_to_sort.append(float(x[column]))
    table_to_sort.sort()
    middle_value = int(len(table_to_sort) / 2)
    if len(table_to_sort) % 2 == 0:
        return (table_to_sort[middle_value - 1] + table_to_sort[middle_value]) / 2
    if len(table_to_sort) % 2 == 1:
        return middle_value


def findQ1(table, column):
    Q1 = []
    for x in table:
        Q1.append(float(x[column]))
    Q1.sort()
    if len(Q1) % 4 == 0:
        return Q1[int(len(Q1) / 4)] - (Q1[int(len(Q1) / 4)] - Q1[int(len(Q1) / 4) - 1]) / 4
    if len(Q1) % 4 == 1:
        return Q1[int(len(Q1) / 4)]
    if len(Q1) % 4 == 2:
        return Q1[int(len(Q1) / 4)] + (Q1[int(len(Q1) / 4) + 1] - Q1[int(len(Q1) / 4)]) / 4
    if len(Q1) % 4 == 3:
        return (Q1[int(len(Q1) / 4)] + Q1[int(len(Q1) / 4) + 1]) / 2


def findQ3(table, column):
    Q3 = []
    for x in table:
        Q3.append(float(x[column]))
    Q3.sort()
    if len(Q3) % 4 == 0:
        return Q3[int(len(Q3) / 4 * 3)] - (Q3[int(len(Q3) / 4 * 3)] - Q3[int(len(Q3) / 4 * 3) - 1]) / 4 * 3
    if len(Q3) % 4 == 1:
        return Q3[int(len(Q3) / 4 * 3)]
    if len(Q3) % 4 == 2:
        return Q3[int(len(Q3) / 4 * 3)] - (Q3[int(len(Q3) / 4 * 3)] - Q3[int(len(Q3) / 4 * 3) - 1]) / 4
    if len(Q3) % 4 == 3:
        return (Q3[int(len(Q3) / 4 * 3)] + Q3[int(len(Q3) / 4 * 3) - 1]) / 2


def findStdDeviation(table, column):
    avg = float(findAverage(table, column))
    sum = 0
    for x in table:
        sum += (float(float(x[column]) - avg) ** 2)
    sum /= len(table)
    sum = sum ** 0.5
    return sum


def drawHistogram(table, column, title, xlable):
    table_values = []
    for x in table:
        table_values.append(float(x[column]))
    min = round(findMinimum(table, column), 0)
    max = round(findMaximum(table, column), 0)
    bins = int(round(math.sqrt(len(table_values)), 0))
    plt.hist(table_values, bins=bins, range=(min, max), edgecolor='black')
    plt.title(title)
    plt.ylabel("Liczebność")
    plt.xlabel(xlable)
    plt.show()

def SortTableForTables(table, column):
    a_category = []
    b_category = []
    c_category = []
    for x in table:
        if int(x[4]) == 0:
            a_category.append(float(x[column]))
        if int(x[4]) == 1:
            b_category.append(float(x[column]))
        if int(x[4]) == 2:
            c_category.append(float(x[column]))
    return [a_category, b_category, c_category]

def drawHistogramFor3Species(table, column, title, xlabel, names_species):
    table_for_all_categories = SortTableForTables(table, column)
    min = round(findMinimum(table, column), 0)
    max = round(findMaximum(table, column), 0)
    bins = int(round(math.sqrt(len(table)), 0))
    plt.hist(table_for_all_categories, bins=bins, range=(min, max), edgecolor='black', stacked=True,
             label=names_species)
    plt.legend(loc="upper left")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Liczebność")
    plt.show()

def drawBoxPlotFor3Species(table, column, names_species, ylabel):
    table_for_all_categories = SortTableForTables(table, column)
    plt.boxplot(table_for_all_categories)
    plt.xlabel("Gatunek")
    plt.ylabel(ylabel)
    plt.xticks([1, 2, 3], names_species)
    plt.show()


f = open(r"data.csv")
csv = csv.reader(f)
kwiatki = []
for row in csv:
    kwiatki.append(row)
f.close()

nazwy = ["setosa", "versicolor", "virginica"]

print("Liczebność gatunku setosa = ", findQuantity(kwiatki, 4, 0))
print("Liczebność gatunku versicolor = ", findQuantity(kwiatki, 4, 1))
print("Liczebność gatunku virginica = ", findQuantity(kwiatki, 4, 2))

print("\t")
print("Minimum dlugosci dzialki kielicha: ", '%.2f' %findMinimum(kwiatki, 0))
print("Maksimum dlugosci dzialki kielicha: ", '%.2f' % findMaximum(kwiatki, 0))
print("Srednia arytmetyczna dlugosci dzialki kielicha: ", '%.2f' % findAverage(kwiatki, 0))
print("Mediana dlugosci dzialki kielicha: ", '%.2f' % findMedian(kwiatki, 0))
print("Kwartl 1: ", '%.2f' % findQ1(kwiatki, 0))
print("Kwartl 3: ", '%.2f' % findQ3(kwiatki, 0))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 0))
print("\t")

print("Minimum szerokosci dzialki kielicha: ", '%.2f' % findMinimum(kwiatki, 1))
print("Maksimum szerokosci dzialki kielicha: ", '%.2f' % findMaximum(kwiatki, 1))
print("Srednia arytmetyczna szerokosci dzialki kielicha: ", '%.2f' % findAverage(kwiatki, 1))
print("Mediana szerokosci dzialki kielicha: ", '%.2f' % findMedian(kwiatki, 1))
print("Kwartl 1: ", '%.2f' % findQ1(kwiatki, 1))
print("Kwartl 3: ", '%.2f' % findQ3(kwiatki, 1))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 1))
print("\t")

print("Minimum dlugosci platka: ", '%.2f' % findMinimum(kwiatki, 2))
print("Maksimum dlugosci platka: ", '%.2f' % findMaximum(kwiatki, 2))
print("Srednia arytmetyczna dlugosci platka: ", '%.2f' % findAverage(kwiatki, 2))
print("Mediana dlugosci platka: ", '%.2f' % findMedian(kwiatki, 2))
print("Kwartyl 1: ", '%.2f' % findQ1(kwiatki, 2))
print("Kwartyl 3: ", '%.2f' % findQ3(kwiatki, 2))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 2))
print("\t")

print("Minimum szerokosci platka: ", '%.2f' % findMinimum(kwiatki, 3))
print("Maksimum szerokosci platka: ", '%.2f' % findMaximum(kwiatki, 3))
print("Srednia arytmetyczna szerokosci platka: ", '%.2f' % findAverage(kwiatki, 3))
print("Mediana szerokosci dzialki kielicha: ", '%.2f' % findMedian(kwiatki, 3))
print("Kwartyl 1: ", '%.2f' % findQ1(kwiatki, 3))
print("Kwartyl 3: ", '%.2f' % findQ3(kwiatki, 3))
print("Odchylenie standardowe: ", '%.2f' % findStdDeviation(kwiatki, 3))

drawHistogram(kwiatki, 0, "Długość działki kielicha", "Długość[cm]")
drawHistogram(kwiatki, 1, "Szerokość działki kielicha", "Szerokość[cm]")
drawHistogram(kwiatki, 2, "Długość płatka", "Długość[cm]")
drawHistogram(kwiatki, 3, "Szerokość płatka", "Szerokość[cm]")

drawBoxPlotFor3Species(kwiatki, 0, nazwy, "Długośc[cm]")
drawBoxPlotFor3Species(kwiatki, 1, nazwy, "Szerokość[cm]")
drawBoxPlotFor3Species(kwiatki, 2, nazwy, "Długość[cm]")
drawBoxPlotFor3Species(kwiatki, 3, nazwy, "Szerokośc[cm]")

drawHistogramFor3Species(kwiatki, 0, "Długość działki kielicha", "Długość[cm]", nazwy)
drawHistogramFor3Species(kwiatki, 1, "Szerokość działki kielicha", "Szerokość[cm]", nazwy)
drawHistogramFor3Species(kwiatki, 2, "Długość płatka", "Długość[cm]", nazwy)
drawHistogramFor3Species(kwiatki, 3, "Szerokość płatka", "Szerokość[cm]", nazwy)
