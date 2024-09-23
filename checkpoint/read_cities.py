# Author: Abdul-Kudus Alhassan
# Date: 02/22/2023
# Purpose: reading from a file and writing to a different file

from city import City

# a list to store all the city objects
list_of_cities = []

# READING FROM THE FILE
file_r = open("world_cities.txt", "r")  # open file for read mode
for line in file_r:  # going through every line of the file
    city = line.strip().split(",")  # removing white space and converting the line into a list
    city_obj = City(city[0], city[1], city[2], city[3], city[4], city[5])  # creating a city object
    list_of_cities.append(city_obj)  # adding the city object to the list of cities

file_r.close()  # close file

# Writing to cities_out
output_file = open("cities_out.txt", "w")  # Open file for write mode

for city in list_of_cities:
    output_file.write(str(city) + "\n")  # writes every city object in the list into the new file

output_file.close() # close file
