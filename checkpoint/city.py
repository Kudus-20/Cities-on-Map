# Author: Abdul-Kudus Alhassan
# Date: 02/22/2023
# Purpose: creating a class for a city

from cs1lib import *
from random import uniform


class City:
    # the constructor method
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = country_code
        self.name = str(name)
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):  # method to return a concatenated string
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    # this method draws a city on the map as a coloured circle
    def draw(self, cx, cy):
        # Generates a random value for the r,g,b colour components
        r = uniform(0, 1)
        g = uniform(0, 1)
        b = uniform(0, 1)

        # setting the stroke and colour of circles randomly
        set_fill_color(r, g, b)
        set_stroke_color(r, g, b)

        px = cx + (720 / 2 + (float(self.longitude) * 2))  # scales the x position of the city
        py = cy + (360 / 2 - (float(self.latitude) * 2))  # scales the y position of the city
        RADIUS = 5  # radius of circle representing a country
        draw_circle(px, py, RADIUS)  # draws the city as a circle on the map
