import java.util.concurrent.CancellationException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class Promise<T> implements Future<T> {

    private CountDownLatch latch;
    private boolean done;
    private boolean cancelled;
    private T value;

    public Promise() {
        latch = new CountDownLatch(1);
    }

    @Override
    public synchronized boolean cancel(boolean mayInterruptIfRunning) {
        if (isDone()) {
            return false;
        } else {
            cancelled = true;
            done = true;
            latch.countDown();
            return true;
        }
    }

    @Override
    public boolean isCancelled() {
        return cancelled;
    }

    @Override
    public boolean isDone() {
        return done;
    }

    @Override
    public T get() throws InterruptedException, ExecutionException {
        latch.await();
        return getValue();
    }

    @Override
    public T get(long timeout, TimeUnit unit) throws InterruptedException, ExecutionException, TimeoutException {
        if (latch.await(timeout, unit)) {
            return getValue();
        } else {
            throw new TimeoutException();
        }
    }

    private T getValue() {
        if (cancelled) {
            throw new CancellationException();
        }
        return value;
    }

    public synchronized void set(T value) {
        if (isCancelled()) {
            throw new CancellationException();
        }
        if (isDone()) {
            throw new IllegalStateException();
        }
        this.value = value;
        done = true;
        latch.countDown();

    }
}
