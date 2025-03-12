import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def makeChart(xlabel,ylabel,title,width=6.4,height=4.8):
    plt.figure(figsize=(width,height))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def makeChartManual(xlabel,ylabel,title):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)