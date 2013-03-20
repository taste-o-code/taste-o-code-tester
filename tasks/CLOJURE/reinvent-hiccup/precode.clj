(require 'clojure.xml)

(declare html)

;;; Use some random stuff at the end to reduce probability of user defining function with same name.
(defn check-hiccup-task-48gj4Jk [to-encode expected]
  (letfn [(str-to-stream [str]
            (java.io.ByteArrayInputStream. (.getBytes str)))
          (safe-parse [content]
            (try
              (clojure.xml/parse content)
    (catch java.lang.Exception e)))]
      (->> [(html to-encode) expected]
        (map str-to-stream)
        (map safe-parse)
        (apply =)
        (println))))

