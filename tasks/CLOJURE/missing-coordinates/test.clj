
(require 'clojure.edn)

(let [input (clojure.edn/read)
      res (coordinates input)]
  (doseq [[v pos] (sort-by first res)]
    (println v (vec pos))))
