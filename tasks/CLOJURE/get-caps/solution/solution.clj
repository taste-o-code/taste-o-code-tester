(defn get-caps [st]
  (->> (seq st)
       (filter #(Character/isUpperCase %))
       (apply str)))