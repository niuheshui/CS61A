
(define (vir-fib n)
    (cond
        ((= 0 n) 0)
        ((= 1 n) 1)
        (else (+ (vir-fib (- n 1)) (vir-fib (- n 2)))))
)

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)
