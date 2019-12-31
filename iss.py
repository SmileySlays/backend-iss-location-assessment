#!/usr/bin/env python

__author__ = 'SmileySlays'

import requests
import turtle
import time


def main():
    # List of astronauts
    astros = requests.get("http://api.open-notify.org/astros.json")
    print(astros.json())
    # Location of ISS and timestamp
    location = requests.get("http://api.open-notify.org/iss-now.json")
    location_json = location.json()
    # Latitude and longitude of ISS and
    # Rounded since goto() doesn't except strings or floats
    latitude = round(float(location_json["iss_position"]["latitude"]))
    longitude = round(float(location_json["iss_position"]["longitude"]))
    # Timestamp of when ISS passes over Indy next
    payload = {'lat': str(round(39.7684)),
               "lon": str(round(86.1581))}
    timestamp = requests.get("http://api.open-notify.org/iss-pass.json",
                             params=payload)
    formatted_timestamp = time.ctime(timestamp.json()["request"]["datetime"])
    # Setting up turtle screen
    world_map = turtle.Screen()
    world_map.setup(width=0.75, height=0.5, startx=None, starty=None)
    world_map.setworldcoordinates(110, -180, -110, 180)
    # Background pic of map
    world_map.bgpic("map.gif")
    # Registered ISS and as shape
    world_map.register_shape("iss.gif")
    # Made ISS a turtle and told it to go to coordinates exiting on click
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.up()
    iss.setheading(51.6)
    iss.speed(1)
    iss.goto(latitude, longitude)
    # Creating Indy dot and timestamp for when ISS passes over next
    indy = turtle.Turtle()
    indy.up()
    indy.shape("circle")
    indy.color("yellow")
    indy.setpos(39.7684, 86.1581)
    indy.write(formatted_timestamp, align="left")
    indy.forward(5)
    world_map.exitonclick()
    print(time.ctime(timestamp.json()["request"]["datetime"]))


if __name__ == '__main__':
    main()
