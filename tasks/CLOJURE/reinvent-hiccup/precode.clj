(require 'clojure.xml)

(declare html)

(defn str-to-stream [str]
  (java.io.ByteArrayInputStream. (.getBytes str)))

(defn check [to-encode expected]
  (->> [(html to-encode) expected]
       (map str-to-stream)
       (map clojure.xml/parse)
       (apply =)
       (println)))

