package com.mclaughlan.advent.days.day12;

public class Waypoint extends Point {
    public Waypoint() {
        coord = new Coordinate(10, 1);
    }

    public void rotate(int degrees) {
        coord.rotate(degrees);
    }
}
