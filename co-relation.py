from io import IncrementalNewlineDecoder
from numpy.core.numeric import correlate
import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    ice_cream_sales=[]
    cool_drink_sales=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
            cool_drink_sales.append(float(row["Cold drink sales"]))

    return {"x":ice_cream_sales,"y":cool_drink_sales}

def find_co_relation(datasource):
     correlation=np.corrcoef(datasource["x"],datasource["y"])
     print("correleation between ice cream and cool drinks is",correlation[0,1])

def setup():
     data_path="IceCream.csv"
     datasource=getDataSource(data_path)
     find_co_relation(datasource)

setup()
        






























