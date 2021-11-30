package com.mclaughlan.advent.utility;

public class Pair<T, R> {
    private T a;
    private R b;

    public Pair(T a, R b) {
        this.a = a;
        this.b = b;
    }

    public T getFirst() {
        return a;
    }

    public R getSecond() {
        return b;
    }
}
