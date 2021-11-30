package com.mclaughlan.advent.days;

import com.mclaughlan.advent.days.day7.Bag;
import com.mclaughlan.advent.days.day7.BagParser;
import com.mclaughlan.advent.solution.Solution;

import java.util.Map;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class Day7 extends Solution {

    private final Map<String, Bag> bags;

    public Day7() {
        super("day7/input");

        bags = inputReader.streamLines().map(b -> BagParser.parseBag(b)).collect(Collectors.toMap(b -> b.getColour(), b -> b));
        bags.forEach((c, b) -> b.evaluateRule(bags));
    }

    @Override
    protected Object part1() {
        AtomicInteger count = new AtomicInteger();
        bags.values().forEach(b -> {
            if (b.couldContain(bags.get("shiny gold"))) {
                count.getAndIncrement();
            }
        });
        return count.get();
    }

    @Override
    protected Object part2() {
        return bags.get("shiny gold").mustContain() - 1;
    }
}
