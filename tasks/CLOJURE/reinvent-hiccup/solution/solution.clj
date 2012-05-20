(declare html)

(defn attrs-to-str [attrs]
  (->> (map (fn [[attr value]]
              (format "%s='%s'" (name attr) value))
            attrs)
       (interpose " ")
       (apply str)))

(defn encode-part [part]
  (cond (vector? part) (html part)
        (seq? part) (apply str (map encode-part part))
        :else (str part)))

(defn html [[tag & body]]
  (let [[attrs content] (if (map? (first body))
                          [(attrs-to-str (first body)) (encode-part (rest body))]
                          ["" (encode-part body)])]
    (format "<%1$s %2$s>%3$s</%1$s>" (name tag) attrs content)))
