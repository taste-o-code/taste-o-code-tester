package com.tasteocode;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.List;

public class Outer {


    private abstract class Inner {

        private final Thread thread;

        private Inner() {
            thread = null;
        }

        protected Inner(Thread thread) {
            this.thread = thread;
        }

        public abstract int abstractMethod(int[][] arg1, List<Integer> list);

        private void manyExceptions() throws IOException, IllegalArgumentException, RuntimeException, FileNotFoundException {

        }
    }
}
