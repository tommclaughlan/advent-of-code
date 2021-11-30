package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.stream.Collectors;

public class Day9 extends Solution {
    public Day9() {
        super("day9/input");
    }

    @Override
    protected Object part1() {
        var last25 = new ArrayList<Long>();

        return inputReader.streamLines()
            .map(s -> Long.parseLong(s))
            .reduce(0L, (a, i) -> {
                if (last25.size() < 25) {
                    last25.add(i);
                } else {
                    var found = last25.stream().filter(j -> last25.contains(i - j)).collect(Collectors.toList());
                    if (found.isEmpty() && a == 0) {
                        return i;
                    }
                    last25.remove(0);
                    last25.add(i);
                }
                return a;
            });
    }

    @Override
    protected Object part2() {
        var first = (Long)part1();

        var list = inputReader.streamLines()
            .map(s -> Long.parseLong(s)).collect(Collectors.toList());

        var i = 0;
        var j = 2;
        var sublist = list.subList(i, j);
        var sum = sublist.stream().reduce(0L, (a, b) -> a + b).longValue();
        while (sum != first) {
            if (sum < first) {
                j++;
            } else if (sum > first) {
                i++;
            }
            sublist = list.subList(i, j);
            sum = sublist.stream().reduce(0L, (a, b) -> a + b).longValue();
        }

        return sublist.stream().max(Comparator.naturalOrder()).get() + sublist.stream().min(Comparator.naturalOrder()).get();
    }
}
