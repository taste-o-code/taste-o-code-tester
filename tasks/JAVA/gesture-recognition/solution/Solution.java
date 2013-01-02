import java.awt.Point;

public class Solution {

    public static enum Gesture {
        SLIDE_LEFT(1, Dir.LEFT),
        SLIDE_RIGHT(1, Dir.RIGHT),
        SLIDE_UP(1, Dir.UP),
        SLIDE_DOWN(1, Dir.DOWN),
        DOUBLE_SLIDE_LEFT(2, Dir.LEFT),
        DOUBLE_SLIDE_RIGHT(2, Dir.RIGHT),
        DOUBLE_SLIDE_UP(2, Dir.UP),
        DOUBLE_SLIDE_DOWN(2, Dir.DOWN),
        ZOOM_IN() {
            @Override
            public boolean satisfy(Point[][] chains, Dir[] dirs) {
                if (chains.length != 2) {
                    return false;
                }
                if (dirs[0].opposite() != dirs[1]) {
                    return false;
                }
                int t = chains[0].length;
                return chains[0][0].distanceSq(chains[1][0]) < chains[0][t - 1].distanceSq(chains[1][t - 1]);
            }},
        ZOOM_OUT() {
            @Override
            public boolean satisfy(Point[][] chains, Dir[] dirs) {
                if (chains.length != 2) {
                    return false;
                }
                if (dirs[0].opposite() != dirs[1]) {
                    return false;
                }
                int t = chains[0].length;
                return chains[0][0].distanceSq(chains[1][0]) > chains[0][t - 1].distanceSq(chains[1][t - 1]);
            }};

        private int n;
        private Dir dir;

        public boolean satisfy(Point[][] chains, Dir[] dirs) {
            if (chains.length != n) {
                return false;
            }
            for (Dir d : dirs) {
                if (d != dir) {
                    return false;
                }
            }
            return true;
        }

        private Gesture() {}

        private Gesture(int n, Dir dir) {
            this.n = n;
            this.dir = dir;
        }
    }

    public static enum Dir {
        RIGHT, LEFT, UP, DOWN;

        public  Dir opposite() {
            switch (this) {
            case LEFT: return Dir.RIGHT;
            case RIGHT: return Dir.LEFT;
            case UP: return Dir.DOWN;
            case DOWN: return Dir.UP;
            default: throw new IllegalArgumentException("What is " + this);
            }
        }
    }

    private Dir getDir(Point[] chain) {
        Point first = chain[0];
        Point last = chain[chain.length - 1];
        int dx = Math.abs(first.x - last.x);
        int dy = Math.abs(first.y - last.y);
        if (dx > dy) {
            if (first.x > last.x) {
                return Dir.LEFT;
            } else {
                return Dir.RIGHT;
            }
        } else {
            if (first.y > last.y) {
                return Dir.DOWN;
            } else {
                return Dir.UP;
            }
        }
    }

    private Dir[] getDirs(Point[][] chains) {
        Dir[] dirs = new Dir[chains.length];
        for (int i = 0; i < chains.length; i++) {
            dirs[i] = getDir(chains[i]);
        }
        return dirs;
    }

    private Point findClosest(Point[] points, Point base) {
        Point best = null;
        for (Point point : points) {
            if (point == null) {
                continue;
            }
            if (best == null || base.distanceSq(best) > base.distanceSq(point)) {
                best = point;
            }
        }
        for (int i = 0; i < points.length; i++) {
            if (best == points[i]) {
                points[i] = null;
            }
        }
        return best;
    }

    private Point[] getChain(Point[][] data, Point first) {
        Point current = first;
        Point[] chain = new Point[data.length];
        for (int i = 0; i < data.length; i++) {
            current = findClosest(data[i], current);
            chain[i] = current;
        }
        return chain;
    }

    private Point[][] splitByChains(Point[][] data) {
        int n = data[0].length;
        Point[][] chains = new Point[n][];
        for (int i = 0; i < n; i++) {
            chains[i] = getChain(data, data[0][i]);
        }
        return chains;
    }

    public Gesture recognize(Point[][] data) {
        Point[][] chains = splitByChains(data);
        Dir[] dirs = getDirs(chains);
        for (Gesture gesture : Gesture.values()) {
            if (gesture.satisfy(chains, dirs)) {
                return gesture;
            }
        }
        return null;
    }
}
