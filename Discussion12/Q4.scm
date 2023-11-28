(define-macro (max expr1 expr2)
    (let (
            (val1 (eval expr1))
            (val2 (eval expr2))
          )
      (if (>= val1 val2)
          val1
          val2)
      )
    )

;(define-macro (max expr1 expr2)
;    `(if (>= ,expr1 ,expr2) ,expr1 ,expr2)
;    )

;(define-macro (max expr1 expr2)
;    (list (if (>= ,expr1 ,expr2) ,expr1 ,expr2))
;    )

;(define-macro (max expr1 expr2)
;    (cons 'if
;          (cons
;                (cons '>= (cons expr1 (cons expr2 nil)))
;                (cons expr1 (cons expr2 nil))
;          )
;    )
;    )



; Test
(expect (max -3 (+ 1 2)) 3)
(expect (max 1 1) 1)
