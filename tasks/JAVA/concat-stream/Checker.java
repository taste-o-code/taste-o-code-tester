import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class Checker {

    private Scanner scanner;

    public static void main(String[] args) throws Exception {
        new Checker().run();
    }


    private void run() throws Exception {
        scanner = new Scanner(System.in);
        String methodName = scanner.next();
        List<ConstantStream> streams = buildStreams();
        Method method = getClass().getMethod(methodName, List.class);
        try {
            method.invoke(this, streams);
            System.out.println("true");
        } catch (InvocationTargetException e) {
            if (e.getCause() instanceof WrongAnswerException) {
                System.out.println("false");
            } else {
                throw e;
            }
        }
    }


    private List<ConstantStream> buildStreams() {
        List<ConstantStream> streams = new ArrayList<ConstantStream>();
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            streams.add(new ConstantStream(scanner.nextByte(), scanner.nextInt()));
        }
        return streams;
    }


    public void checkReadToInt(List<ConstantStream> streams) throws Exception{
        ConcatStream concatStream = new ConcatStream(streams);
        for (ConstantStream constant: streams) {
            for (int i = 0; i < constant.getN(); i++) {
                assertEquals(concatStream.read(), constant.getConstant());
            }
        }
    }

    public void checkReadToArray(List<ConstantStream> streams) throws Exception {
        ConcatStream concatStream = new ConcatStream(streams);
        byte[] array = new byte[1000];
        int cur = 0;
        int readLength = 0;
        for (ConstantStream constant: streams) {
            int left = constant.getN();
            while (left != 0) {
                if (cur == readLength) {
                    readLength = concatStream.read(array);
                    cur = 0;
                }
                assertEquals(array[cur], constant.getConstant());
                left--;
		cur++;
            }
        }
    }

    public void checkReadToArrayWithBounds(List<ConstantStream> streams) throws Exception {
        ConcatStream concatStream = new ConcatStream(streams);
        byte[] array = new byte[100];
        int cur = 0;
        int readLength = 0;
        int offset = 0;
        Random random = new Random();
        for (ConstantStream constant: streams) {
            int left = constant.getN();
            while (left != 0) {
                if (cur == readLength) {
                    offset = random.nextInt(40);
                    int length = random.nextInt(50) + 10;
                    readLength = concatStream.read(array, offset, length);
		    cur = 0;
                }
                assertEquals(array[offset + cur], constant.getConstant());
                left--;
		cur++;
            }
        }
    }

    public void checkAvailable(List<ConstantStream> streams) throws Exception {
        ConcatStream concatStream = new ConcatStream(streams);
        for (ConstantStream constant: streams) {
            for (int i = 0; i < constant.getN(); i++) {
                assertTrue(concatStream.available() > 0);
                assertEquals(concatStream.read(), constant.getConstant());
            }
        }
    }

    public void checkClose(List<ConstantStream> streams) throws Exception {
        ConcatStream concatStream = new ConcatStream(streams);
        for (ConstantStream constant: streams) {
            assertTrue(!constant.isClosed());
        }
        concatStream.close();
        for (ConstantStream constant: streams) {
            assertTrue(constant.isClosed());
        }
    }

    private void assertEquals(int b1, int b2) {
        if (b1 != b2) {
            throw new WrongAnswerException();
        }
    }

    private void assertTrue(boolean value) {
        if (!value) {
            throw new WrongAnswerException();
        }
    }

    public class WrongAnswerException extends RuntimeException {}

    public static class ConstantStream extends InputStream {

        private byte constant;
        private int n;
        private int cur;
        private boolean closed;

        public ConstantStream(byte constant, int n) {
            this.constant = constant;
            this.n = n;
        }

        @Override
        public int read() throws IOException {
            if (cur < n) {
                cur++;
                return constant;
            } else {
                return -1;
            }
        }

        @Override
        public int read(byte[] b, int off, int len) throws IOException {
            if (b == null) {
                throw new NullPointerException();
            } else if (off < 0 || len < 0 || len > b.length - off) {
                throw new IndexOutOfBoundsException();
            } else if (len == 0) {
                return 0;
            } else if (cur == n) {
                return -1;
            }
            len = Math.min(len, n - cur);
            Arrays.fill(b, off, off + len, constant);
            cur += len;
            return len;
        }

        @Override
        public int available() throws IOException {
            return n;
        }

        public byte getConstant() {
            return constant;
        }

        public int getN() {
            return n;
        }

        public boolean isClosed() {
            return closed;
        }

        @Override
        public void close() throws IOException {
            closed = true;
        }
    }

}