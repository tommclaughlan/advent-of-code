package com.mclaughlan.advent.days.day8;

import com.mclaughlan.advent.utility.Pair;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;

public class Program {
    private final List<Line> lines;
    private List<Pair<Line, Integer>> history;

    private int acc;
    private int pointer;

    public Program(List<String> lines) {
        this.lines = lines.stream().map(l -> new Line(l)).collect(Collectors.toList());
        this.history = new ArrayList<>();
        acc = 0;
        pointer = 0;
    }

    public void reset() {
        lines.forEach(l -> l.reset());
        history = new ArrayList<>();
        acc = 0;
        pointer = 0;
    }

    public Result run(Integer toMod) {
        try {
            while (runNext(Optional.ofNullable(toMod))) {
            }
        } catch (Exception e) {
            return new Result(acc, history, true);
        }
        return new Result(acc, history, false);
    }

    private boolean runNext(Optional<Integer> toMod) throws Exception {
        if (pointer >= lines.size()) {
            return false;
        }

        var nextLine = lines.get(pointer);
        if (nextLine.runCount() > 0) {
            throw new Exception("LOOP");
        }

        history.add(new Pair(nextLine, pointer));
        nextLine.run(toMod.isPresent() && toMod.get() == pointer);
        return true;
    }

    public class Result {
        public final int acc;
        public final List<Pair<Line, Integer>> stack;
        public final boolean loop;

        public Result(int acc, List<Pair<Line, Integer>> stack, boolean loop) {
            this.acc = acc;
            this.stack = stack;
            this.loop = loop;
        }
    }

    public class Line {
        private final AtomicInteger runCount;
        private final Instruction instruction;
        private final int argument;

        public Line(String line) {
            var parts = line.split(" ");
            instruction = Instruction.valueOf(parts[0].toUpperCase());
            argument = Integer.parseInt(parts[1]);
            runCount = new AtomicInteger(0);
        }

        public void run(boolean mod) {
            runCount.incrementAndGet();
            switch (instruction) {
                case NOP:
                    if (mod) {
                        jmp();
                    } else {
                        nop();
                    }
                    break;
                case ACC:
                    acc += argument;
                    pointer++;
                    break;
                case JMP:
                    if (mod) {
                        nop();
                    } else {
                        jmp();
                    }
                    break;
            }
        }

        public int runCount() {
            return runCount.get();
        }

        public void reset() {
            runCount.set(0);
        }

        private void nop() {
            pointer++;
        }
        private void jmp() {
            pointer+=argument;
        }
    }

    private enum Instruction {
        NOP,
        ACC,
        JMP
    }
}
