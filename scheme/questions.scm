(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (help index lst)
      (if (null? lst)
          nil
          (append (list (list index (car lst))) (help (+ 1 index) (cdr lst)))))
  (help 0 s)
 )
  ; END PROBLEM 15
  


;; Problem 16

;; Merge two lists S1 and S2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? s1 s2)
  ; BEGIN PROBLEM 16
  (cond
      ((null? s1) s2)
      ((null? s2) s1)
      ((ordered? (car s1) (car s2)) (cons (car s1) (merge ordered? (cdr s1) s2)))
      (else (cons (car s2) (merge ordered? (cdr s2) s1))))
  )
  ; END PROBLEM 16

;; Optional Problem 2

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN OPTIONAL PROBLEM 2
        expr
         ; END OPTIONAL PROBLEM 2
         )
        ((quoted? expr)
         ; BEGIN OPTIONAL PROBLEM 2
         expr
         ; END OPTIONAL PROBLEM 2
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
            (append (cons form (cons params nil)) (map let-to-lambda body))
           ; END OPTIONAL PROBLEM 2
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
           (define tmp (zip values))
           (define args (car tmp))
           (define vals (cadr tmp))
           (append (cons (append (cons 'lambda (cons args nil)) (map let-to-lambda body)) nil) vals)
           ; END OPTIONAL PROBLEM 2
           ))
        (else
         ; BEGIN OPTIONAL PROBLEM 2
         expr
         ; END OPTIONAL PROBLEM 2
         )))

; Some utility functions that you may find useful to implement for let-to-lambda

;(
;     (x 1) 
;     (y (+ 1 2)) 
;     (z (* 1 (+ 2 1)))
;)


 

(define (zip pairs)
  
 (define (firsts pairs)
        (if (null? pairs) nil
            (cons (car (car pairs)) (firsts (cdr pairs)))))
    (define (nexts pairs) 
        (if (null? pairs) nil
            (cons  (cdr (car pairs)) (nexts (cdr pairs)))))

(define (check pairs)
    (cond
        ((null? pairs) #f)
        ((null? (car pairs)) #t)
        (else (check (cdr pairs)))))
    (define (loop pairs)
        (if (check pairs) nil
            (append (cons (firsts pairs) nil) (loop (nexts pairs)))))
    (loop pairs)
  )



;(append (cons (firsts '((1 2 3) (4 5 6))) nil) 
;        (append (cons (firsts '((2 3) (5 6))) nil)
;                (append (cons (firsts '((3) (6))) nil)
;                        (append (cons (firsts '(() ())) nil)))))


