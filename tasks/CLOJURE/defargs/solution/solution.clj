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


