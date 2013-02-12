import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class ConcatStream extends InputStream {

    private List<? extends InputStream> streams;
    private int cur;


    ConcatStream(List<? extends InputStream> streams) {
        this.streams = streams;
    }

    @Override
    public int read(byte[] b, int off, int len) throws IOException {
        if (cur == streams.size()) {
            return -1;
        } else {
            int readLength = streams.get(cur).read(b, off, len);
            if (readLength == -1) {
                cur++;
                return read(b, off, len);
            } else {
                return readLength;
            }
        }
    }

    @Override
    public int read() throws IOException {
        if (cur == streams.size()) {
            return -1;
        } else {
            int got = streams.get(cur).read();
            if (got == -1) {
                cur++;
                return read();
            } else {
                return got;
            }
        }
    }

    @Override
    public int available() throws IOException {
        if (isFinished()) {
            return 0;
        } else {
            int av = streams.get(cur).available();
            if (av == 0) {
                cur++;
                return available();
            } else {
                return av;
            }
        }
    }

    @Override
    public void close() throws IOException {
        cur = streams.size();
        for (InputStream stream : streams) {
            stream.close();
        }
    }

    private boolean isFinished() {
        return cur == streams.size();
    }
}