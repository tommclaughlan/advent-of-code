package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;
import com.mclaughlan.advent.utility.Pair;

import java.util.ArrayList;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Stream;

public class Day3 extends Solution {

    public Day3() {
        super("day3/input");
    }

    @Override
    public Object part1() {
        return countTrees(inputReader.streamLines(), 1, 3);
    }

    @Override
    public Object part2() {
        var list = new ArrayList<Pair<Integer, Integer>>();
        list.add(new Pair(1, 1));
        list.add(new Pair(1, 3));
        list.add(new Pair(1, 5));
        list.add(new Pair(1, 7));
        list.add(new Pair(2, 1));

        return list.stream().reduce(1, (a, p) -> a * countTrees(inputReader.streamLines(), p.getFirst(), p.getSecond()), Integer::sum);
    }

    private int countTrees(Stream<String> lines, int down, int across) {
        AtomicInteger row = new AtomicInteger();
        AtomicInteger column = new AtomicInteger();
        var result = lines.reduce(0, (a, i) -> {
            if (row.getAndIncrement() % down != 0) {
                return a;
            }

            var test = i.charAt(column.getAndAdd(across) % (i.length()));
            if (test == '#') {
                return a + 1;
            }

            return a;
        }, Integer::sum);

        return result;
    }
}
