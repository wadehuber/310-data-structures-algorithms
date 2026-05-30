; Radix Sort (LSD)
; ----------------
; A demonstration of least-significant-digit radix sort from the
; "Sorting in Linear Time" notes.
;
; Radix sort extends counting sort to multi-digit numbers by sorting one
; digit at a time, from least significant to most significant.  Each pass
; uses a *stable* counting sort as its subroutine, so the ordering achieved
; by earlier (lower) digits survives later passes.
;
; For d-digit numbers in base r it runs in Theta(d * (n + r)) time -- linear
; in the input when the number of digits d is small or constant.
;
; This example sorts fixed-width integer keys (think hashed feature ids or
; quantized values) in base 10 so you can print the array after each digit
; pass and watch it converge.

; Stable counting sort of vector A using the digit selected by exp.
;
; exp is a power of base: exp=1 sorts by the ones digit, exp=10 by the tens
; digit, and so on.  Stability here is what makes the multi-pass radix sort
; correct.  Takes a vector and returns a vector.
(define (counting-sort-by-digit A exp base)
  (let* ((n (vector-length A))
         (C (make-vector base 0))
         (B (make-vector n 0)))
    ; Count occurrences of each digit value (0..base-1).
    (do ((j 0 (+ j 1))) ((= j n))
      (let ((digit (modulo (quotient (vector-ref A j) exp) base)))
        (vector-set! C digit (+ (vector-ref C digit) 1))))
    ; Cumulative sums -> ending positions.
    (do ((d 1 (+ d 1))) ((= d base))
      (vector-set! C d (+ (vector-ref C d) (vector-ref C (- d 1)))))
    ; Place right-to-left to preserve stability.
    (do ((j (- n 1) (- j 1))) ((< j 0))
      (let ((digit (modulo (quotient (vector-ref A j) exp) base)))
        (vector-set! C digit (- (vector-ref C digit) 1))
        (vector-set! B (vector-ref C digit) (vector-ref A j))))
    B))

; Return a sorted list (non-negative integers), one digit pass at a time.
; When trace is true, print the list after each pass.
(define (radix-sort lst base trace)
  (if (null? lst)
      '()
      (let ((max-value (apply max lst)))
        (let loop ((exp 1) (cur (list->vector lst)))
          (if (> (quotient max-value exp) 0)
              (let ((next (counting-sort-by-digit cur exp base)))
                (when trace
                  (display "  after ")
                  (if (= exp 1) (display "  ones") (begin (display exp) (display "s")))
                  (display " digit: ")
                  (display (vector->list next))
                  (newline))
                (loop (* exp base) next))
              (vector->list cur))))))

; --- demonstration ---
(define keys '(329 457 657 839 436 720 355 8 90 3))
(display "Input keys: ") (display keys) (newline)
(display "Radix sort passes (LSD -> MSD):") (newline)
(define result (radix-sort keys 10 #t))
(display "Radix sorted:   ") (display result) (newline)
(display "Library sorted: ") (display (sort keys <)) (newline)
