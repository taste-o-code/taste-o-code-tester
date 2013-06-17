package com.tasteocode;

import java.io.IOException;
import java.io.Serializable;
import java.util.List;

public class Basic implements Serializable {

    private long privateInt = 12321;

    protected Basic(int privateInt) {
        this.privateInt = privateInt;
    }

    public double sum(int a, Integer b) throws IOException {
        return a + b;
    }
}
