# Author: Abdul-Kudus Alhassan
# Date: 02/22/2023
# Purpose: visualizing the cities on a map

from cs1lib import *
from read_cities import list_of_cities
from quick_sort import sort
from sort_cities import compare_population

FRAME_RATE = 5  # slowing down the rate at which the draw function is called
HEIGHT = 360  # the height of the display window
WIDTH = 720  # the width of the display window
NUMBER_OF_CITIES = 50  # number of cities to be displayed on map
CX = 0  # latitude 0
CY = 0  # longitude 0

# DRAWING MAP
img = load_image("map.png")  # this loads the map image

new_list = []  # stores the list of cities to be displayed on the map
counter = 0  # keeps track of the number of cities drawn

# Sorting the list of city objects based on population
sort(list_of_cities, compare_population)


def draw():
    global counter  # keeps track of the number of cities drawn
    clear()
    draw_image(img, CX, CY)  # drawing the map image

    for city in new_list:  # draws all city objects in the list
        city.draw(CX, CY)

    if counter < NUMBER_OF_CITIES:  # checks if 50 cities have already been displayed
        new_list.append(list_of_cities[counter])  # adds a new city to the list each time the function is called

        counter += 1  # incrementing counter


start_graphics(draw, width=WIDTH, height=HEIGHT, framerate=FRAME_RATE)
