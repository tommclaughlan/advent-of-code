package com.mclaughlan.advent.days.day12;

public class Ship extends Point {
    private int facing = 0; // 0 == due east
    public void turn(int degrees) {
        facing += degrees;
    }

    public void moveForward(int amount) {
        int xd = (int) (amount * Math.cos(Math.toRadians(facing)));
        int yd = (int) (amount * -Math.sin(Math.toRadians(facing)));

        coord.move(xd, yd);
    }

    public void moveTo(Waypoint point, int times) {
        coord.move(point.coord.x * times, point.coord.y * times);
    }

    public int distance() {
        return coord.getDistance(0, 0);
    }

    public void printCoord() {
        System.out.println("E: " + coord.x + ", N: " + coord.y);
    }
}
