;scm> (curry-cook '(a) 'a)
;(lambda (a) a)
;scm> (curry-cook '(x y) '(+ x y))
;(lambda (x) (lambda (y) (+ x y)))

(define (curry-cook formals body) 
    (if (null? (cdr formals))
        `(lambda ,formals ,body)
        `(lambda ,(cons (car formals) nil) ,(curry-cook (cdr formals) body))))


;scm> (define three-curry (lambda (x) (lambda (y) (lambda (z) (+ x (* y z)))) ))
;three-curry
;scm> (define eat-two (curry-consume three-curry '(1 2))) ; pass in only two arguments, return should be a one-arg lambda function!
;eat-two
;scm> eat-two
;(lambda (z) (+ x (* y z)))
;scm> (eat-two 3) ; pass in the last argument; 1 + (2 * 3)
;7
;scm> (curry-consume three-curry '(1 2 3)) ; all three arguments at once
;7

(define (curry-consume curry args)
  (if (null? args)
      curry
      (curry-consume (curry (car args)) (cdr args))))

(define-macro (switch expr cases)
  (switch-to-cond (list 'switch expr cases)))


;scm> (switch-to-cond `(switch (+ 1 1) ((1 2) (2 4) (3 6))))
;(cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))

(define (switch-to-cond switch-expr)
  (cons 'cond 
        (map
         (lambda (case) (cons (list 'equal? (car (cdr switch-expr)) (car case)) (cdr case)))
         (car (cdr (cdr switch-expr))))))

(define (min x y)
  (if (< x y)
      x
      y))

(define (count f n i)
  (if (= i 0)
      0
      (+ (if (f n i)
             1
             0)
         (count f n (- i 1)))))

(define (is-factor dividend divisor)
  (if (equal? (modulo dividend divisor) 0)
      #t
      #f))


;scm> (switch-factors 1)
;one
;scm> (switch-factor 17)
;prime
;scm> (switch-factor 9)
;composite

(define (switch-factors n)
  (switch (min 3 (count is-factor n n)) ((1 'one) (2 'prime) (3 'composite))))
