package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;
import com.mclaughlan.advent.utility.Pair;

import java.util.List;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;

public class Day1 extends Solution {

    public Day1() {
        super("day1/input");
    }

    @Override
    public Object part1() {
        var stream = inputReader.streamLines();
        var list = stream.map(s -> Integer.parseInt(s)).sorted().collect(Collectors.toList());

        var result = findPair(list, 2020).get();
        return result.getFirst() * result.getSecond();
    }

    public Object part2() {
        var stream = inputReader.streamLines();
        var list = stream.map(s -> Integer.parseInt(s)).sorted().collect(Collectors.toList());

        var result = list.stream().reduce((a, i) -> {
            var pair = findPair(list, 2020 - i);
            if (pair.isPresent()) {
                return i * pair.get().getFirst() * pair.get().getSecond();
            }
            return a;
        }).get();

        return result;
    }

    private Optional<Pair<Integer, Integer>> findPair(List<Integer> input, Integer target) {
        AtomicReference<Optional<Pair<Integer, Integer>>> result = new AtomicReference<>(Optional.empty());
        input.stream().filter(i -> {
            var found = input.stream().filter(j -> j == target - i).findFirst();
            if (found.isPresent()) {
                result.set(Optional.of(new Pair<Integer, Integer>(i, found.get())));
                return true;
            }
            return false;
        }).findFirst();

        return result.get();
    }
}
