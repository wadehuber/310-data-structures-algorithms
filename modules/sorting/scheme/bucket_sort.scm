; Bucket Sort
; -----------
; A demonstration of bucket sort from the "Sorting in Linear Time" notes.
;
; Bucket sort assumes the input is real numbers uniformly distributed over
; [0, 1).  It divides that range into n equal buckets, drops each element
; into the bucket for its range, sorts each bucket with a simple method
; (insertion sort works well because buckets stay small), and concatenates.
;
; Under the uniform assumption each bucket holds roughly a constant number of
; elements, giving O(n) expected time.
;
; This example sorts uniform [0, 1) scores -- the kind of normalized
; confidence values the notes mention -- and prints the bucket contents so
; you can see the distribute-then-concatenate structure.

; Insert x into an already-sorted list, keeping ascending order.
(define (insert x sorted)
  (cond ((null? sorted) (list x))
        ((<= x (car sorted)) (cons x sorted))
        (else (cons (car sorted) (insert x (cdr sorted))))))

; Plain insertion sort; fast on the short lists inside each bucket.
(define (insertion-sort lst)
  (if (null? lst)
      '()
      (insert (car lst) (insertion-sort (cdr lst)))))

; Return a sorted list, where every element is in [0, 1).
; Uses n buckets so that element x lands in bucket floor(n * x).
(define (bucket-sort lst show-buckets)
  (let ((n (length lst)))
    (if (= n 0)
        '()
        (let ((buckets (make-vector n '())))
          ; Distribute: bucket index scales with the value (input in [0, 1)).
          (for-each
            (lambda (x)
              (let* ((raw (inexact->exact (floor (* n x))))
                     (index (if (>= raw n) (- n 1) raw)))   ; guard x == 1.0
                (vector-set! buckets index (cons x (vector-ref buckets index)))))
            lst)
          ; Sort each bucket, then concatenate in order.
          (let loop ((i 0) (result '()))
            (if (= i n)
                result
                (let ((sorted-bucket (insertion-sort (vector-ref buckets i))))
                  (when show-buckets
                    (display "  bucket ") (display i)
                    (display " [") (display (exact->inexact (/ i n)))
                    (display ", ") (display (exact->inexact (/ (+ i 1) n)))
                    (display "): ") (display sorted-bucket) (newline))
                  (loop (+ i 1) (append result sorted-bucket)))))))))

; --- demonstration ---
(define scores '(0.78 0.17 0.39 0.26 0.72 0.94 0.21 0.12 0.23 0.68))
(display "Input scores: ") (display scores) (newline)
(display "Buckets:") (newline)
(define result (bucket-sort scores #t))
(display "Bucket sorted:  ") (display result) (newline)
(display "Library sorted: ") (display (sort scores <)) (newline)
