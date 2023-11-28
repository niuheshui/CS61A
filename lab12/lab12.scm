; scm> (if-program '(= 0 0) '2 '3)
; (if (= 0 0) 2 3)
; scm> (eval (if-program '(= 0 0) '2 '3))
; 2
; scm> (if-program '(= 1 0) '(print 3) '(print 5))
; (if (= 1 0) (print 3) (print 5))
; scm> (eval (if-program '(= 1 0) '(print 3) '(print 5)))
; 5
(define (if-program condition if-true if-false)
  `(if ,condition
       ,if-true
       ,if-false))

; scm> (define expr (pow-expr 5 1))
; expr
; scm> expr
; (* 1 5)
; scm> (eval expr)
; 5
; scm> (define expr2 (pow-expr 5 2))
; expr2
; scm> expr2
; (* (* 1 5) 5)
; scm> (eval expr2)
; 25
(define (pow-expr n p)
  (if (zero? p)
      1
      `(* ,(pow-expr n (- p 1)) ,n)))

(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (swap expr)
  (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
    (if (> (eval second) (eval first))
        (append `(,op ,second ,first) rest)
        (append `(,op ,first ,second) rest))))
