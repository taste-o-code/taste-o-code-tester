(ns test-generator.core
  (:require [quil.core :refer :all]
            [clojure.set :refer [map-invert]]
            [clojure.string :refer [join]]))

(def sq-size 20)
(def field-size 20)

(def dirs {:left [-1 0]
           :right [1 0]
           :up [0 -1]
           :down [0 1]})

(defn move [pos dir]
  (map + pos (dirs dir)))

(def black (atom #{}))

(defn draw-grid []
  (doseq [ind (range field-size)]
    (line 0 (* ind sq-size) (* sq-size field-size) (* ind sq-size))
    (line (* ind sq-size) 0 (* ind sq-size) (* sq-size field-size))))

(defn draw-filled []
  (doseq [[x y] @black]
    (rect (* x sq-size) (* y sq-size) sq-size sq-size)))

(defn draw []
  (fill 255)
  (rect 0 0 (width) (height))
  (color 0)
  (fill 0)
  (draw-grid)
  (draw-filled))

(defn toggle-square []
  (let [x (quot (mouse-x) sq-size)
        y (quot (mouse-y) sq-size)]
    (println x y)
    (swap! black #((if (% [x y]) disj conj) % [x y]))))

(defn neibs [ids pos]
  (into {} (for [dir (keys dirs)
                 :let [neib (move pos dir)]
                 :when (ids neib)]
             [dir (ids neib)])))

(defn save-level []
  (let [ids (->> (repeatedly #(rand-int 100))
                 distinct
                 (map #(keyword (str "v" %)))
                 (zipmap @black))
        neibs-map (into {} (for [pos (keys ids)]
                             [(ids pos) (neibs ids pos)]))]
    (spit "input.clj" (pr-str neibs-map))
    (->> (sort-by first ids)
         (map #(join " " %))
         (join \newline)
         (spit "output"))))

(defn mouse []
  (case (mouse-button)
    :left (toggle-square)
    :right (save-level)))


(defn run []
  (sketch :draw #'draw
          :size [(* sq-size field-size) (* sq-size field-size)]
          :mouse-clicked mouse))

(run)
