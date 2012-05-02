(declare derivative)

(def ^:dynamic x)

(defn calc [expr value]
  (binding [x value]
    (str (eval (derivative expr)))))

(defn test [expr values]
  (println (mapv #(calc expr %) values)))

