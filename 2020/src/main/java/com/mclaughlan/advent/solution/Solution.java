package com.mclaughlan.advent.solution;

import com.mclaughlan.advent.utility.InputReader;

import java.time.Duration;
import java.time.Instant;
import java.util.function.Function;

public abstract class Solution {
    protected InputReader inputReader;
    public Solution(String input) {
        inputReader = new InputReader(input);
    }

    protected abstract Object part1();
    protected abstract Object part2();

    public void run() {
        timedRun((a) -> "part 1: " + part1());
        timedRun((a) -> "part 2: " + part2());
    }

    private void timedRun(Function<?, String> toRun) {
        Instant start = Instant.now();
        var result = toRun.apply(null);
        Instant end = Instant.now();
        System.out.println(result + ". Time taken: " + Duration.between(start, end).toMillis() + " ms");
    }
}
