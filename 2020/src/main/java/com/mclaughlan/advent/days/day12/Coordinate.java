package com.mclaughlan.advent.days.day12;

public class Coordinate {
    public int x;
    public int y;

    public Coordinate() {
        this.x = 0;
        this.y = 0;
    }

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void move(int x, int y) {
        this.x += x;
        this.y += y;
    }

    public void rotate(int degrees) {
        var radians = -Math.toRadians(degrees);
        var xp = (int) (x * Math.cos(radians)) - (int) (y * Math.sin(radians));
        var yp = (int) (x * Math.sin(radians)) + (int) (y * Math.cos(radians));
        x = xp;
        y = yp;
    }

    public int getDistance(int x0, int y0) {
        return Math.abs(x - x0) + Math.abs(y - y0);
    }
}
