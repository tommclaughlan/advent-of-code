package com.mclaughlan.advent.utility;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.stream.Stream;

public class InputReader {

    private String input;

    public InputReader(String input) {
        this.input = input;
    }

    public Stream<String> streamLines() {
        var inputStream = getClass().getClassLoader().getResourceAsStream(input);
        var isr = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
        var reader = new BufferedReader(isr);
        return reader.lines();
    }
}
