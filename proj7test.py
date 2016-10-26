# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 16:29:32 2016

@author: MichaelMroue
"""

import pylab
import matplotlib.patches as patches
import csv

def open_file():
    decades = ["1980","1990","2000","2010"]
    make = []
    year = []
    city = []
    hwy = []
    company = ["ford","mercury","lincoln","gm","chevrolet","gmc","cadillac",\
        "pontiac","buick","oldsmobile","saturn","honda","acura","toyota","lexus",\
         "scion","make"]
    while True:
        files = input("enter decades (1980,1990,2000,2010): ").strip( )
        files_list = files.split(",")
        for item in files_list:
            if item in decades:
               file_csv = csv.reader(open(item+"s.csv"))
               for line in file_csv:
                   if line[46].lower() in company:
                      if line[63] != "2017":
                         make.append(line[46])
                         year.append(line[63])
                         city.append(line[4])
                         hwy.append(line[34])
                         
            else:
                print("error not in decades")
        city_hwy = list(zip(city,hwy))
        
        return make , year , city_hwy

             




def plot_mileage(years,city,highway):
    '''Plot the city and highway mileage data.
       Input: years, a list of years;
              city, a dictionary with manufacturer as key and list of annual mileage as value;
              highway, a similar dictionary with a list of highway mileage as values.
       Requirement: all lists must be the same length.'''
    pylab.figure(1)
    pylab.plot(years, city['Ford'], 'r-', years, city['GM'], 'b-', years,
             city['Honda'], 'g-', years, city['Toyota'], 'y-')
    red_patch = patches.Patch(color='red', label='Ford')
    blue_patch = patches.Patch(color='blue', label='GM')
    green_patch = patches.Patch(color='green', label='Honda')
    yellow_patch = patches.Patch(color='yellow', label='Toyota')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('City Fuel Economy (MPG)')
    pylab.show()
    
    # Plot the highway mileage data.
    pylab.figure(2)
    pylab.plot(years, highway['Ford'], 'r-', years, highway['GM'], 'b-', years,
             highway['Honda'], 'g-', years, highway['Toyota'], 'y-')
    pylab.legend(handles=[red_patch, blue_patch, green_patch, yellow_patch])
    pylab.xlabel('Years')
    pylab.ylabel('Highway Fuel Economy (MPG)')
    pylab.show()
    
make,year,city_hwy= open_file()
main_map = dictionary_func(make,year,city_hwy)
