(defn derivative
  ([expr]
    (cond (= expr 'x) 1
          (number? expr) 0
          :else (apply derivative expr)))
  ([op a b]
    (cond (= op '+)
          (list '+ (derivative a) (derivative b))
          (= op '-)
          (list '- (derivative a) (derivative b))
          (= op '*)
          (list '+ (list '* a (derivative b))
                   (list '* (derivative a) b))
          (= op '/)
          (list '/ (list '- (list '* (derivative a) b)
                            (list '* a (derivative b)))
                (list '* b b)))))