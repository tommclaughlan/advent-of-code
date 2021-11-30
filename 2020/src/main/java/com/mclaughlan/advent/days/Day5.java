package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;
import com.mclaughlan.advent.utility.Pair;

import java.util.Comparator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day5 extends Solution {
    public Day5()
    {
        super("day5/input");
    }
    @Override
    protected Object part1() {
        return getSeatIds().max(Comparator.naturalOrder()).get();
    }

    @Override
    protected Object part2() {
        var set = getSeatIds().collect(Collectors.toSet());
        var max = (int) part1();
        for (var i = 0; i < max; i++) {
            if (set.contains(i + 1) && set.contains(i - 1) && !set.contains(i)) {
                return i;
            }
        }

        return "FAIL";
    }

    private Stream<Integer> getSeatIds() {
        return inputReader.streamLines().mapToInt(s -> {
            var seat = getSeat(s);
            return (seat.getFirst() * 8) + seat.getSecond();
        }).boxed();
    }

    private Pair<Integer, Integer> getSeat(String input) {
        return new Pair<>(getRow(input.substring(0, 7)), getColumn(input.substring(7)));
    }

    private int getRow(String input) {
        return Integer.parseInt(input.replace("F", "0").replace("B", "1"), 2);
    }

    private int getColumn(String input) {
        return Integer.parseInt(input.replace("L", "0").replace("R", "1"), 2);
    }
}
