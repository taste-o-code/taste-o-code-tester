package com.tasteocode;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public final class Complex extends ArrayList<Complex>
        implements Serializable, Cloneable, List<Complex>, Collection<Complex> {

    public int publicInt;
    private final double privateDouble;
    transient protected Object obj;
    volatile Long aLong;
    Class[][][][][][][] classes;

    public Complex(int initialCapacity, double privateDouble) {
        super(initialCapacity);
        this.privateDouble = privateDouble;
    }

    public Complex(Class[][][][][][][] classes, Long aLong) {
        this.classes = classes;
        this.aLong = aLong;
        privateDouble = 123;
    }

    public native void helloNative(int a, boolean b, short c, byte d, float e, long f, double j);

    private void manyExceptions() throws RuntimeException, IllegalArgumentException, Exception, IOException, FileNotFoundException {

    }
}
