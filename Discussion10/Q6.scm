(define (duplicate lst)
    (if (null? lst)
        nil
        (let
            (
                (first (car lst))
                (rest (cdr lst))
            )
            (cons first (cons first (duplicate rest)))
        )
    )
)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))
(expect (duplicate '(1 1)) (1 1 1 1))

