package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;

import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicLong;

public class Day10 extends Solution {
    public Day10() {
        super("day10/input");
    }

    private static int[] trib = new int[] { 1, 1, 2, 4, 7, 13, 24 };

    @Override
    protected Object part1() {
        var onegaps = new AtomicInteger(0);
        var threegaps = new AtomicInteger(1);
        var prev = new AtomicInteger(0);
        inputReader.streamLines()
            .map(Integer::parseInt)
            .sorted()
            .forEach(j -> {
                var gap = j - prev.getAndSet(j);
                if (gap == 1) {
                    onegaps.incrementAndGet();
                } else if (gap == 3) {
                    threegaps.incrementAndGet();
                }
            });

        return onegaps.get() * threegaps.get();
    }

    @Override
    protected Object part2() {
        var prev = new AtomicInteger(0);
        var combos = new AtomicLong(1);
        var onestring = new AtomicInteger(0);

        inputReader.streamLines()
            .map(Integer::parseInt)
            .sorted()
            .forEach(j -> {
                var gap = j - prev.getAndSet(j);
                if (gap == 1) {
                    onestring.incrementAndGet();
                } else {
                    combos.getAndUpdate(x -> x * trib[onestring.get()]);
                    onestring.set(0);
                }
            });

        combos.getAndUpdate(x -> x * trib[onestring.get()]);

        return combos.get();
    }
}
