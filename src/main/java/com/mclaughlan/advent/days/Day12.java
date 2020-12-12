package com.mclaughlan.advent.days;

import com.mclaughlan.advent.days.day12.Ship;
import com.mclaughlan.advent.days.day12.Waypoint;
import com.mclaughlan.advent.solution.Solution;

public class Day12 extends Solution {
    public Day12() {
        super("day12/input");
    }

    @Override
    protected Object part1() {
        var ship = new Ship();
        inputReader.streamLines()
            .forEach(l -> {
                var instruction = l.charAt(0);
                var argument = Integer.parseInt(l.substring(1));
                switch (instruction) {
                    case 'F':
                        ship.moveForward(argument);
                        break;
                    case 'N':
                        ship.moveNorth(argument);
                        break;
                    case 'S':
                        ship.moveSouth(argument);
                        break;
                    case 'E':
                        ship.moveEast(argument);
                        break;
                    case 'W':
                        ship.moveWest(argument);
                        break;
                    case 'L':
                        ship.turn(-argument);
                        break;
                    case 'R':
                        ship.turn(argument);
                        break;
                }
            });
        return ship.distance();
    }

    @Override
    protected Object part2() {
        var ship = new Ship();
        var waypoint = new Waypoint();
        inputReader.streamLines()
            .forEach(l -> {
                var instruction = l.charAt(0);
                var argument = Integer.parseInt(l.substring(1));
                switch (instruction) {
                    case 'F':
                        ship.moveTo(waypoint, argument);
                        break;
                    case 'N':
                        waypoint.moveNorth(argument);
                        break;
                    case 'S':
                        waypoint.moveSouth(argument);
                        break;
                    case 'E':
                        waypoint.moveEast(argument);
                        break;
                    case 'W':
                        waypoint.moveWest(argument);
                        break;
                    case 'L':
                        waypoint.rotate(-argument);
                        break;
                    case 'R':
                        waypoint.rotate(argument);
                        break;
                }
            });
        return ship.distance();
    }
}
