(defn- build-let [def-args real-args]
  (let [pairs (partition 2 def-args)]
    (vec (mapcat (fn [ind]
                   (let [[var def-val] (nth pairs ind)]
                     [var (nth real-args ind def-val)]))
                 (range (count pairs))))))

(defmacro defargs [name args & body]
  (let [vars (take-nth 2 args)
        default (gensym "default")
        keys (gensym "keys")]
   `(defn ~name [& ~keys]
      (let [~default ~(vec (take-nth 2 (rest args)))
            ~@(mapcat (fn [ind]
                        [(nth vars ind) `(nth ~keys ~ind (nth ~default ~ind))])
                      (range (count vars)))]
        ~@body))))

