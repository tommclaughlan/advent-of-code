package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.concurrent.atomic.AtomicInteger;

public class Day6 extends Solution {
    public Day6() {
        super("day6/input");
    }

    @Override
    protected Object part1() {
        var count = new AtomicInteger();

        var group = new Group();
        inputReader.streamLines().forEach(l -> {
            if (l.equals("")) {
                count.addAndGet(group.getUniqueCharacters());
                group.clear();
            } else {
                group.addMember(getCharacterSet(l.toCharArray()));
            }
        });

        if (group.size() > 0) {
            count.addAndGet(group.getUniqueCharacters());
        }

        return count.get();
    }

    @Override
    protected Object part2() {
        var count = new AtomicInteger();

        var group = new Group();
        inputReader.streamLines().forEach(l -> {
            if (l.equals("")) {
                count.addAndGet(group.getCommonCharacters());
                group.clear();
            } else {
                group.addMember(getCharacterSet(l.toCharArray()));
            }
        });

        if (group.size() > 0) {
            count.addAndGet(group.getCommonCharacters());
        }

        return count.get();
    }

    private Set<Character> getCharacterSet(char[] array) {
        var set = new HashSet<Character>();
        for (var c : array) {
            set.add(c);
        }
        return set;
    }

    class Group {
        private List<Set<Character>> members = new ArrayList<>();

        public void addMember(Set<Character> member) {
            members.add(member);
        }

        public int getUniqueCharacters() {
            var superSet = new HashSet<Character>();
            members.forEach(m -> superSet.addAll(m));
            return superSet.size();
        }

        public int getCommonCharacters() {
            var superSet = new HashSet<Character>();
            members.forEach(m -> superSet.addAll(m));
            members.forEach(m -> superSet.retainAll(m));
            return superSet.size();
        }

        public void clear() {
            members.clear();
        }

        public int size() {
            return members.size();
        }
    }
}
