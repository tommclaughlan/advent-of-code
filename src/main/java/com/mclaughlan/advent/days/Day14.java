package com.mclaughlan.advent.days;

import com.mclaughlan.advent.solution.Solution;

import java.util.HashMap;
import java.util.Map;
import java.util.regex.Pattern;

public class Day14 extends Solution {
    public Day14() {
        super("day14/input");
    }

    @Override
    protected Object part1() {
        Map<Long, Long> memory = new HashMap<>();

        var mask = new Mask();

        inputReader.streamLines().forEach(l -> {
            var parts = l.split(" = ");
            if (parts[0].equals("mask")) {
                mask.setMask(parts[1]);
            } else {
                var regex = Pattern.compile("mem\\[(\\d+)\\]");
                var match = regex.matcher(parts[0]);
                match.find();
                var mem = Long.parseLong(match.group(1));
                var val = Long.parseLong(parts[1]) & mask.getAndMask() | mask.getOrMask();

                memory.put(mem, val);
            }
        });

        return memory.values().stream().reduce(0L, (a, b) -> a + b).longValue();
    }

    @Override
    protected Object part2() {
        Map<Long, Long> memory = new HashMap<>();
        var mask = new Mask();

        inputReader.streamLines().forEach(l -> {
            var parts = l.split(" = ");
            if (parts[0].equals("mask")) {
                mask.setMask(parts[1]);
            } else {
                var regex = Pattern.compile("mem\\[(\\d+)\\]");
                var match = regex.matcher(parts[0]);
                match.find();
                var mem = Long.parseLong(match.group(1));

                var addresses = mask.getMemAddresses(mem);

                var val = Long.parseLong(parts[1]);

                for (var i = 0; i < addresses.length; i++) {
                    memory.put(addresses[i], val);
                }
            }
        });
        return memory.values().stream().reduce(0L, (a, b) -> a + b).longValue();
    }

    class Mask {
        private String maskString = "";
        private int floats = 0;

        public void setMask(String mask) {
            maskString = mask;
            floats = 0;
            for (var i=0; i < maskString.length(); i++) {
                if (maskString.charAt(i) == 'X') {
                    floats++;
                }
            }
        }

        public long getAndMask() {
            return Long.parseLong(maskString.replace("X", "1"), 2);
        }

        public long getOrMask() {
            return Long.parseLong(maskString.replace("X", "0"), 2);
        }

        public long[] getMemAddresses(long mem) {
            var memMask = String.format("%1$" + 36 + "s", Long.toUnsignedString(mem | getOrMask(), 2)).replace(' ', '0');
            var builder = new StringBuilder();
            for (var x = 0; x < maskString.length(); x++) {
                if (maskString.charAt(x) == 'X') {
                    builder.append('X');
                } else {
                    builder.append(memMask.charAt(x));
                }
            }

            var mask = builder.toString();

            var nResults = (int)Math.pow(2, floats);
            var result = new long[nResults];

            for (var f = 0; f < nResults; f++) {

                var floatMask = String.format("%1$" + floats + "s", Long.toUnsignedString(f, 2)).replace(' ', '0');
                var tmpMask = mask;
                for (var i = 0; i < floatMask.length(); i++) {
                    tmpMask = tmpMask.replaceFirst("X", String.valueOf(floatMask.charAt(i)));
                }
                result[f] = Long.parseLong(tmpMask, 2);
            }
            return result;
        }
    }
}
