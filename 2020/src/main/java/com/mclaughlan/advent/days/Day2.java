package com.mclaughlan.advent.days;

import com.mclaughlan.advent.days.day2.Rule;
import com.mclaughlan.advent.days.day2.RulePositions;
import com.mclaughlan.advent.solution.Solution;

import java.util.stream.Collectors;

public class Day2 extends Solution {
    public Day2() {
        super("day2/input");
    }

    @Override
    public Object part1() {
        var lines = inputReader.streamLines();
        return lines.filter(this::checkPassword).collect(Collectors.toList()).size();
    }

    public Object part2() {
        var lines = inputReader.streamLines();
        return lines.filter(this::checkPassword2).collect(Collectors.toList()).size();
    }

    private boolean checkPassword(String line) {
        var parts = line.split(":");
        var rule = new Rule(parts[0]);
        return rule.isValid(parts[1]);
    }

    private boolean checkPassword2(String line) {
        var parts = line.split(":");
        var rule = new RulePositions(parts[0]);
        return rule.isValid(parts[1]);
    }
}
