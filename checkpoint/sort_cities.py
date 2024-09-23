# Author: Abdul-Kudus Alhassan
# Date: 02/22/2023
# Purpose: sorting a list of cities

from quick_sort import *
from read_cities import list_of_cities  # imports the list of city objects


# COMPARE FUNCTIONS
# compares the city objects based on their population instance variables
def compare_population(city1, city2):
    return city1.population >= city2.population


# compares the city objects based on their latitude instance variables
def compare_latitude(city1, city2):
    return city1.latitude <= city2.latitude


# compares the city objects based on their name instance variables
def compare_names(city1, city2):
    return city1.name.lower() <= city2.name.lower()


sort_name_file = open("cities_alpha.txt", "w")  # opens the cities_alpha file for writing mode
sort(list_of_cities, compare_names)  # sorts the city objects based on the compare_names function
for city in list_of_cities:  # writes the sorted cities into the file
    sort_name_file.write(str(city) + "\n")

sort_name_file.close()  # close file

sort_population_file = open("cities_population.txt", "w")  # opens the cities_population file for writing mode
sort(list_of_cities, compare_population)  # sorts the city objects based on the compare_population function
for city in list_of_cities:  # writes the sorted cities into the file
    sort_population_file.write(str(city) + "\n")

sort_population_file.close()  # close file

sort_latitude_file = open("cities_latitude.txt", "w")
sort(list_of_cities, compare_latitude)  # sorts the city objects based on the compare_latitude function
for city in list_of_cities:
    sort_latitude_file.write(str(city) + "\n")

sort_latitude_file.close()  # close file
