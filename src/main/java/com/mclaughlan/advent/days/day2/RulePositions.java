package com.mclaughlan.advent.days.day2;

public class RulePositions {

    private char character;
    private int pos1;
    private int pos2;

    public RulePositions(String rule) {
        var parts = rule.split(" ");
        var chars = parts[0].split("-");
        character = parts[1].charAt(0);
        pos1 = Integer.parseInt(chars[0]);
        pos2 = Integer.parseInt(chars[1]);
    }

    public boolean isValid(String password) {
        return password.charAt(pos1) == character ^ password.charAt(pos2) == character;
    }
}
