package com.mclaughlan.advent.days;

import com.mclaughlan.advent.days.day11.Floorplan;
import com.mclaughlan.advent.solution.Solution;

import java.util.stream.Collectors;

public class Day11 extends Solution {
    public Day11() {
        super("day11/input");
    }

    @Override
    protected Object part1() {
        var floorplan = new Floorplan(inputReader.streamLines()
            .map(l -> l.chars().mapToObj(c -> (char) c).collect(Collectors.toList()))
            .collect(Collectors.toList()));

        while (floorplan.tick(false, 4)) { }

        return floorplan.getOccupied();
    }

    @Override
    protected Object part2() {
        var floorplan = new Floorplan(inputReader.streamLines()
        .map(l -> l.chars().mapToObj(c -> (char) c).collect(Collectors.toList()))
        .collect(Collectors.toList()));

        while (floorplan.tick(true, 5)) { }

        return floorplan.getOccupied();
    }
}
