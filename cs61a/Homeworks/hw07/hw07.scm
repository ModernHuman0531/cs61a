(define (filter-lst fn lst)
  'YOUR-CODE-HERE
  (if (null? lst)
    '()
    (if (fn (car lst))
      (append(cons (car lst) nil) (filter-lst fn (cdr lst)))
      (filter-lst fn (cdr lst))
    )
  )
)
;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)


(define (interleave first second)
  'YOUR-CODE-HERE
  (if (or (null? first) (null? second))
    (append first second)
    (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))) 
  )
)

(interleave (list 1 3 5) (list 2 4 6))
; expect (1 2 3 4 5 6)

(interleave (list 1 3 5) nil)
; expect (1 3 5)

(interleave (list 1 3 5) (list 2 4))
; expect (1 2 3 4 5)


(define (accumulate combiner start n term)
  'YOUR-CODE-HERE
  (begin
    (define (helper combiner start num term)
      (if (> num n)
        start
        (helper combiner (combiner start (term num)) (+ num 1) term)
      )
    )
    (helper combiner start 1 term)
  )
)


(define (no-repeats lst)
  'YOUR-CODE-HERE
  (if (null? lst)
    '()
    (cons (car lst) (no-repeats(filter (lambda (x) (not (= (car lst) x))) (cdr lst))))
  )
)

