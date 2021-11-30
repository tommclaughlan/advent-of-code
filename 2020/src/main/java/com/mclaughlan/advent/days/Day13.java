package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;

import java.util.Arrays;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class Day13 extends Solution {
    public Day13() {
        super("day13/input");
    }

    @Override
    protected Object part1() {
        var currentTime = new AtomicInteger(-1);
        var busToTake = new AtomicInteger(-1);
        AtomicInteger shortestTime = new AtomicInteger(99999);
        inputReader.streamLines().forEach(l -> {
            if (currentTime.get() < 0) {
                currentTime.set(Integer.parseInt(l));
            } else {
                Arrays.asList(l.split(",")).forEach(b -> {
                    if (!b.equals("x")) {
                        var busId = Integer.parseInt(b);
                        var nextBus = busId - (currentTime.get() % busId);
                        if (nextBus < shortestTime.get()) {
                            shortestTime.set(nextBus);
                            busToTake.set(busId);
                        }
                    }
                });
            }
        });

        return busToTake.get() * shortestTime.get();
    }

    @Override
    protected Object part2() {
        var busList = Arrays.asList(inputReader.streamLines().collect(Collectors.toList()).get(1).split(","));
        var increment = Long.parseLong(busList.get(0));
        var timestamp = increment;

        for (var i=1; i < busList.size(); i++) {
            if ("x".equals(busList.get(i))) {
                continue;
            }

            var currentBus = Integer.parseInt(busList.get(i));

            while ((timestamp + i) % currentBus != 0) {
                timestamp += increment;
            }

            increment *= currentBus;
        }
        return timestamp;
    }
}
