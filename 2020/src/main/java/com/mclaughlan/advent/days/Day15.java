package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;

import java.util.ArrayList;
import java.util.HashMap;

public class Day15 extends Solution {
    public Day15() {
        super("day15/input");
    }

    @Override
    protected Object part1() {
        int[] input = { 2, 0, 6, 12, 1, 3 };
        return getNumberSpokenAtIndex(input, 2020);
    }

    @Override
    protected Object part2() {
        int[] input = { 2, 0, 6, 12, 1, 3 };
        return getNumberSpokenAtIndex(input, 30000000);
    }

    public int getNumberSpokenAtIndex(int[] input, int nToSpeak) {
        var spoken = new HashMap<Integer, Integer>();
        var lastNumber = -1;

        for (var i = 0; i < nToSpeak; i++) {
            if (i < input.length) {
                spoken.put(input[i], i);
                lastNumber = input[i];
            } else {
                var lastSpokenIndex = spoken.get(lastNumber);

                if (lastSpokenIndex == null || lastSpokenIndex == i - 1) {
                    spoken.put(lastNumber, i - 1);
                    lastNumber = 0;
                } else {
                    spoken.put(lastNumber, i - 1);
                    lastNumber = (i - 1) - lastSpokenIndex;
                }
            }
        }
        return lastNumber;
    }
}
