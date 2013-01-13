import java.io.BufferedReader;
import java.io.ByteArrayOutputStream;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.io.StringReader;
import java.io.StringWriter;
import java.lang.reflect.Method;
import java.util.List;
import java.util.concurrent.CancellationException;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.TimeoutException;

public class Checker {

    private static final String VAL = "VAL";
    private static ExecutorService executor;

    private static void log(String message) {
        System.out.println(message);
    }

    public static void checkNormalFlow() throws Exception {
        final Promise<String> promise = new Promise<String>();
        log("prepare");
        log("promise is done: " + promise.isDone());
        setDelayed(promise, 200);
        String value = promise.get();
        log("got value: " + value);
        log("promise is done: " + promise.isDone());
    }

    public static void checkGetWithTimeoutNoException() throws Exception {
        final Promise<String> promise = new Promise<String>();
        log("prepare");
        log("promise is done: " + promise.isDone());
        setDelayed(promise, 200);
        String value = promise.get(1, TimeUnit.SECONDS);
        log("got value: " + value);
        log("promise is done: " + promise.isDone());
    }

    public static void checkGetWithTimeoutException() throws Exception {
        final Promise<String> promise = new Promise<String>();
        log("prepare");
        log("promise is done: " + promise.isDone());
        setDelayed(promise, 200);
        try {
            promise.get(100, TimeUnit.MILLISECONDS);
        } catch (TimeoutException e) {
            log("threw timeout exception");
        }
    }

    public static void checkMultipleSet() throws Exception {
        Promise<String> promise = new Promise<String>();
        log("prepare");
        log("promise is done: " + promise.isDone());
        log("try set value first time");
        promise.set(VAL);
        log("set first time");
        log("try set value second time");
        try {
            promise.set(VAL);
        } catch (IllegalStateException e) {
            log("threw exception");
        }
    }

    public static void checkCancellationWithoutBlockedThreads() throws Exception {
        Promise<String> promise = new Promise<String>();
        log("prepare");
        log("promise is done: " + promise.isDone());
        log("promise is cancelled: " + promise.isCancelled());
        log("cancel promise: " + promise.cancel(true));
        log("promise is done: " + promise.isDone());
        log("promise is cancelled: " + promise.isCancelled());
        log("try get");
        try {
            promise.get();
        } catch (CancellationException e) {
            log("threw exception");
        }
        log("try get with timeout");
        try {
            promise.get(1, TimeUnit.SECONDS);
        } catch (CancellationException e) {
            log("threw exception");
        }
    }

    public static void checkCancellationWithBlockedThreads() throws Exception {
        Promise<String> firstPromise = new Promise<String>();
        log("prepare first");
        log("first promise is done: " + firstPromise.isDone());
        log("first promise is cancelled: " + firstPromise.isCancelled());
        cancelDelayed(firstPromise, 200);
        log("try get");
        try {
            firstPromise.get();
        } catch (CancellationException e) {
            log("threw exception");
        }
        log("first promise is done: " + firstPromise.isDone());
        log("first promise is cancelled: " + firstPromise.isCancelled());

        Promise<String> secondPromise = new Promise<String>();
        log("prepare second");
        log("second promise is done: " + secondPromise.isDone());
        log("second promise is cancelled: " + secondPromise.isCancelled());
        cancelDelayed(secondPromise, 200);
        log("try get with timeout");
        try {
            secondPromise.get(1, TimeUnit.SECONDS);
        } catch (CancellationException e) {
            log("threw exception");
        }
        log("second promise is done: " + secondPromise.isDone());
        log("second promise is cancelled: " + secondPromise.isCancelled());
    }

    public static void checkCancellationAfterPromiseDone() throws Exception {
        Promise<String> promise = new Promise<String>();
        log("prepare");
        log("promise is done: " + promise.isDone());
        log("promise is cancelled: " + promise.isCancelled());
        log("set promise");
        promise.set(VAL);
        log("promise is done: " + promise.isDone());
        log("promise is cancelled: " + promise.isCancelled());
        log("cancel promise: " + promise.cancel(true));
        log("promise is done: " + promise.isDone());
        log("promise is cancelled: " + promise.isCancelled());
    }

    private static void setDelayed(final Promise<String> promise, final long delay) {
        executor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(delay);
                    log("setting value to promise");
                    promise.set(VAL);
                } catch (Exception e) {
                    log("fail");
                }
            }
        });

    }

    private static void cancelDelayed(final Promise<String> promise, final long delay) {
        executor.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(delay);
                    log("cancel promise: " + promise.cancel(true));
                } catch (Exception e) {
                    log("fail");
                }
            }
        });

    }

    private static void runTest(String test) throws Exception {
        Method testMethod = Checker.class.getMethod(test);
        testMethod.invoke(null);
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String testName = reader.readLine();
        reader.close();
        executor = Executors.newSingleThreadExecutor();
        runTest(testName);
        executor.shutdown();
    }
}
