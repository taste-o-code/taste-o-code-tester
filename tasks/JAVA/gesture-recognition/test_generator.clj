(require '[clojure.string :as string])
(require '[clojure.java.io :as io])

(def delta 5)
(def step 10)

(defn rotate [points]
  (map reverse points))

(defn inverse [points]
  (map #(map - %) points))

(defn rand-delta []
  (- (rand-int delta) (quot delta 2)))

(defn next-point [[x _]]
  [(+ x (rand-delta) step)
   (rand-delta)])

(defn right-vector [n]
  (take n(iterate next-point [0 0])))

(defn translate [points center]
  (map #(map + center %) points))

(defn rand-vector [dir n]
  (let [v (right-vector n)]
   (case dir
     :right v
     :left (inverse v)
     :up (rotate v)
     :down (inverse (rotate v)))))

(rand-vector :down 5)

(defn rand-vectors [n & opts]
  (for [[dir center] opts]
    (translate (rand-vector dir n) center)))

(defn transpose [vectors]
  (apply map vector vectors))

(defn to-file [filename vectors]
  (let [t (count (first vectors))
        n (count vectors)]
    (with-open [file (io/writer filename)]
      (binding [*out* file]
        (println n t)
        (doseq [points (transpose vectors)]
          (doseq [[x y] (shuffle points)]
            (print x y " "))
          (println))))))

(defn to-screen [_ vectors]
  (println
   (string/join
    ", "
    (map (fn [v]
           (str "["
                (string/join
                 ", "
                 (map (fn [[x y]] (str "(" x ", " y ")"))
                      v))
                "]"))
         (transpose vectors)))))



(to-screen "test.txt" (rand-vectors 5 [:right [0 0]] [:right [0 5]]))

(def tests
  [
   ["SLIDE_RIGHT" [:right [0 0]]]
   ["SLIDE_RIGHT" [:right [1000 1000]]]
   ["SLIDE_LEFT" [:left [10 -50]]]
   ["SLIDE_LEFT" [:left [100 -500]]]
   ["SLIDE_UP" [:up [10 85]]]
   ["SLIDE_UP" [:up [28 94]]]
   ["SLIDE_DOWN" [:down [-10 -120]]]
   ["SLIDE_DOWN" [:down [-238 -232]]]
   ["DOUBLE_SLIDE_RIGHT" [:right [10 10]] [:right [10 20]]]
   ["DOUBLE_SLIDE_RIGHT" [:right [19 20]] [:right [29 30]]]
   ["DOUBLE_SLIDE_LEFT" [:left [-100 -100]] [:left [-100 -120]]]
   ["DOUBLE_SLIDE_LEFT" [:left [-100 -123]] [:left [-122 -123]]]
   ["DOUBLE_SLIDE_UP" [:up [0 0]] [:up [20 0]]]
   ["DOUBLE_SLIDE_UP" [:up [299 200]] [:up [250 200]]]
   ["DOUBLE_SLIDE_DOWN" [:down [20 20]] [:down [40 30]]]
   ["DOUBLE_SLIDE_DOWN" [:down [20 0]] [:down [40 0]]]
   ["ZOOM_IN" [:down [0 0]] [:up [0 30]]]
   ["ZOOM_IN" [:left [10 20]] [:right [10 20]]]
   ["ZOOM_OUT" [:right [-60 20]] [:left [60 10]]]
   ["ZOOM_OUT" [:up [0 -60]] [:down [0 60]]]
   ])

(defn create-tests []
  (doseq [[num [answer & input]] (zipmap (range) tests)]
    (let [name (format "%02d" num)
          t (+ 4 (rand-int 3))
          vectors (apply rand-vectors t input)]
      (spit (str name ".out") answer)
      (to-file (str name ".in") vectors))))

(create-tests)

(doseq [[answer & input] tests]
  (println answer)
  (to-screen nil (apply rand-vectors (+ 4 (rand-int 3)) input))
  (println "\n"))



