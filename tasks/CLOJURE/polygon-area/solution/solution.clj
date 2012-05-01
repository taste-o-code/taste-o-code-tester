(defn trapezoid-area [[[x1 y1] [x2 y2]]]
  (/ (* (- x2 x1) (+ y1 y2)) 2))

(defn abs [x]
  (if (neg? x) (- x) x))

(defn area [points]
  (->> (cons (last points) points)
       (partition 2 1)
       (map trapezoid-area)
       (apply +)
       abs))