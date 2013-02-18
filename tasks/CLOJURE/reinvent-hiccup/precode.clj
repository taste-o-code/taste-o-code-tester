(require 'clojure.xml)

(declare html)

(defn str-to-stream [str]
  (java.io.ByteArrayInputStream. (.getBytes str)))

(defn safe-parse [content]
  (try
    (clojure.xml/parse content)
    (catch java.lang.Exception e)))

(defn check [to-encode expected]
  (->> [(html to-encode) expected]
       (map str-to-stream)
       (map safe-parse)
       (apply =)
       (println)))

