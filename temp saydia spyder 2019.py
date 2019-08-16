# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:25:45 2019

@author: Saydia
"""

print("hi there") #welcome
print ("2001")
print(56)


#print 78




print(5*2)
print(5/2)
print(5-2)
print(5**2)
print(12+98)


def add(a,b):
  add = a+b
  print(add)

add(2,3)

add(10985.345,9802.472)

add(9067.987,6752.891)


add(678.89,908.34,765.23)


def adds(a,b,c):
     adds = a+b+c
     print(adds)
     
adds(9,7,4)

adds(78,65,38)



#saydia's code
def add(a,b):
    add=a+b
    print("the sum is", add)

add(908,675)



def add(a,c):

import math
dir(math)


math.sq





import math
dir (math)


math.factorial.


#dict data structure
chocolate1 = {"milk":5}
chocolate2 = {"dark" :6}
chocolate3 = {"white" :8}



milk=8
milk= milk+46





chocolatebox  = {"milk":5,"dark": 6,"white":8}
chocolatebox


#list
student1 = ["Steve", 32, "M"]
student2 = ["Lia", 28, "F"]
student3 = ["Vin", 45, "M"]
student4 = ["Katie", 38, "F"]


student1[0]
student1[1]
student1[3]
print(student1, student2, student3, student4)


print[student1, student2, student3, student4]
students
studentinfo = [["Steve",32,"M"],["Lia",28,"F"],["Vin",45,"F"],["Katie",38,"F"]]



#pandas

import pandas
dir(pandas)

studentdf = pandas.DataFrame(studentinfo,columns=("Name","Age","Gender"))
studentdf

#reference columns names


#read data file
af = pandas.read_excel("GISdata.xlsx", sheet_name = women occupation)



#chocolate milk dark white

chocolate1 = ["Milk", 5]
chocolate2 = ["Dark", 6]
chocolate3 = ["White", 8]

chocolate1 = [1]
chocolate2[1]


sugar=[chocolate1, chocolate2, chocolate3]
sugar
sugardf=pandas.DataFrame(sugar,columns=("type","quantity"))
sugardf
print [chocolate1, chocolate2, chocolate3]



suagr=[chocolate1,chocolate2,chocolate3]
sugar
sugardf



import plotly
dir (plotly)
from plotly. offline import plot
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf["Name"], y = studentdf["Age"])
plot([studentbar])


#DAY 4 
import pandas
studentlist = [["Seve", 32, "male"], ["Lia", 28, "female"], ["Vin", 45, "male"], ["Katie", 38, "female"]]
print(studentlist)

studentlistdf1 = pandas.Dataframe(studentlist, columns = ["name", "age", "gender"])



agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])



import pandas
dir (pandas)
import plotly
from plotly. offline import plot
import plotly.graph_objs as go


wodf = pandas.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
wodf



woplot = go.Bar(x=wodf["occupation"], y=wodf["women"],
                marker = {"color": wodf["women"],
                            "colorscale" : "Jet"})
plot([woplot])

