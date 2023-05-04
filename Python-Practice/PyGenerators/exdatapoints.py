from typing import NamedTuple

class MyDataPoint(NamedTuple):
    x: float
    y: float
    z: float

def mydata_reader(file):
    for row in file:
        cols = row.rstrip().split(",")
        cols = [float(c) for c in cols]
        yield MyDataPoint._make(cols)

def example_reader():
    with open('mydata.txt') as file:
        for row in mydata_reader(file):
            print(row)

example_reader()
