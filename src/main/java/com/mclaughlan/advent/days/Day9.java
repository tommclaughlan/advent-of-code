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

        long top = -1;
        long bottom = -1;
        for (var i = 0; i < list.size() - 1 && top == -1 && bottom == -1; i++) {
            for (var j = i + 1; j < list.size(); j++) {
                var sublist = list.subList(i, j + 1);
                var sum = sublist.stream().reduce(0L, (a,b) -> a + b).longValue();
                if (sum == first) {
                    top = sublist.stream().max(Comparator.naturalOrder()).get();
                    bottom = sublist.stream().min(Comparator.naturalOrder()).get();
                    break;
                }
                if (sum > first) {
                    break;
                }
            }
        }

        return top + bottom;
    }
}
