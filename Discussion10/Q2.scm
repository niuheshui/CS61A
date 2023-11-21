(define with-list
    (list
        (list 'a 'b)
        'c
        'd
        (list 'e)
    )
)
(draw with-list)


(define with-quote
    '(
        (a b)
        c
        d
        (e)
    )

)
(draw with-quote)

(define helpful-list
   (cons 'a (cons 'b nil)))
(draw helpful-list)

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))
(draw another-helpful-list)

(define with-cons
    (cons
        helpful-list another-helpful-list
    )
)
(draw with-cons)

