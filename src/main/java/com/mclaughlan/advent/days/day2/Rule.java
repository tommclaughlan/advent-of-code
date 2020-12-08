package com.mclaughlan.advent.days.day2;

public class Rule {

    private char character;
    private int lower;
    private int upper;

    public Rule(String rule) {
        var parts = rule.split(" ");
        var range = parts[0].split("-");
        character = parts[1].charAt(0);
        lower = Integer.parseInt(range[0]);
        upper = Integer.parseInt(range[1]);
    }

    public boolean isValid(String password) {
        var length = password.length();
        var count = 0;

        for (var i = 0; i < length; i++) {
            if (password.charAt(i) == character) {
                count++;
            }
        }

        return count >= lower && count <= upper;
    }
}
