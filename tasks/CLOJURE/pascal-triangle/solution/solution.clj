(defn next-row [row]
  (let [sum-pairs (map #(apply + %) (partition 2 1 row))]
    (concat [1] sum-pairs [1])))

(defn triangle-row [n]
  (nth (iterate next-row [1]) (dec n)))