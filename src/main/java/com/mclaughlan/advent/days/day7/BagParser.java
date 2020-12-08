package com.mclaughlan.advent.days.day7;

public class BagParser {

    public static Bag parseBag(String rule) {
        var parts = rule.split("bags contain");
        var bagName = parts[0].trim();
        var canContain = parts[1].trim();

        return new Bag(bagName, canContain);
    }
}
