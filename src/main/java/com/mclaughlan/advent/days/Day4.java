package com.mclaughlan.advent.days;

import com.mclaughlan.advent.days.day4.Passport;
import com.mclaughlan.advent.solution.Solution;

import java.util.ArrayList;
import java.util.stream.Stream;

public class Day4 extends Solution {

    public Day4() {
        super("day4/input");
    }

    @Override
    protected Object part1() {
        var passports = parsePassports(inputReader.streamLines());
        return passports.stream().filter(p -> p.isValid()).count();
    }

    @Override
    protected Object part2() {
        var passports = parsePassports(inputReader.streamLines());
        return passports.stream().filter(p -> p.isValidStrict()).count();
    }

    private ArrayList<Passport> parsePassports(Stream<String> stream) {
        var list = new ArrayList<Passport>();
        var sb = new StringBuilder();
        stream.forEach(l -> {
            if (l.equals("")) {
                list.add(new Passport(sb.toString().trim()));
                sb.delete(0, sb.length());
            } else {
                sb.append(l + " ");
            }
        });

        if (sb.length() > 0) {
            list.add(new Passport(sb.toString().trim()));
        }

        return list;
    }
}
