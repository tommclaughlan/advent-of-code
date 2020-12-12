package com.mclaughlan.advent.days.day12;

public class Point {

    // north is positive, south is negative
    // east is positive, west is negative
    protected Coordinate coord;

    public Point() {
        coord = new Coordinate();
    }

    public void moveNorth(int amount) {
        coord.move(0, amount);
    }

    public void moveSouth(int amount) {
        coord.move(0, -amount);
    }

    public void moveEast(int amount) {
        coord.move(amount, 0);
    }

    public void moveWest(int amount) {
        coord.move(-amount, 0);
    }
}
