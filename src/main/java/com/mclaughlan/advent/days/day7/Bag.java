package com.mclaughlan.advent.days.day7;

import java.util.*;
import java.util.regex.Pattern;

public class Bag {
    private final String colour;
    private final Map<Bag, Integer> contents;
    private final String rule;

    public Bag(String colour, String rule) {
        this.colour = colour;
        this.rule = rule;
        contents = new HashMap<>();
    }

    public String getColour() {
        return colour;
    }

    public void addContainedBag(Bag bag, int times) {
        contents.put(bag, times);
    }

    public boolean containsBags() {
        return contents.size() > 0;
    }

    public boolean couldContain(Bag bag) {
        if (contents.size() == 0) {
            return false;
        }

        if (contents.containsKey(bag)) {
            return true;
        }

        return contents.keySet().stream().anyMatch(b -> b.couldContain(bag));
    }

    public int mustContain() {
        return contents.keySet().stream()
                .mapToInt(b -> b.mustContain() * contents.get(b))
                .reduce(1, (acc, b) -> acc + b);
    }

    public void evaluateRule(Map<String, Bag> bagMap) {
        if (rule.contains("no other bags")) {
            return;
        }

        var parts = Arrays.asList(rule.split(","));

        var regex = Pattern.compile("(\\d+) (.*) (bag[s]{0,1})");

        parts.forEach(part -> {
            var matcher = regex.matcher(part);
            if (matcher.find()) {
                var times = Integer.parseInt(matcher.group(1));
                var colour = matcher.group(2);
                var bag = bagMap.get(colour);
                contents.put(bag, times);
            }
        });
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Bag bag = (Bag) o;

        return colour == bag.colour;
    }
}
