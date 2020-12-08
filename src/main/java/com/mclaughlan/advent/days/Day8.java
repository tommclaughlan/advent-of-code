package com.mclaughlan.advent.days;

import com.mclaughlan.advent.days.day8.Program;
import com.mclaughlan.advent.solution.Solution;

import java.util.stream.Collectors;

public class Day8 extends Solution {
    public Day8() {
        super("day8/input");
    }

    @Override
    protected Object part1() {
        var program = new Program(inputReader.streamLines().collect(Collectors.toList()));
        return program.run(null).acc;
    }

    @Override
    protected Object part2() {
        var program = new Program(inputReader.streamLines().collect(Collectors.toList()));
        var result = program.run(null);
        var stack = result.stack;
        var toMod = stack.size() - 1;
        var loop = true;
        while (loop && toMod >= 0) {
            program.reset();
            result = program.run(stack.get(toMod--).getSecond());
            loop = result.loop;
        }

        if (loop) {
            throw new RuntimeException("Didn't complete");
        }

        return result.acc;
    }
}
