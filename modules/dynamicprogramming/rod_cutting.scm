;;; Rod Cutting  (CSC310 Module 11 - Dynamic Programming)
;;; =====================================================
;;;
;;; Bottom-up dynamic programming: r[j] = best revenue for a rod of length j,
;;; with a choice table s[j] = optimal first cut, used to reconstruct the cuts.

(define prices #(0 1 5 8 9 10 17 17 20 24 30))

(define (bottom-up-cut-rod prices n)
  "Return two vectors: r (best revenue 0..n) and s (optimal first cut 1..n)."
  (let ((r (make-vector (+ n 1) 0))
        (s (make-vector (+ n 1) 0)))
    (do ((j 1 (+ j 1)))                  ; rod length j = 1..n
        ((> j n) (values r s))
      (let ((best -1))
        (do ((i 1 (+ i 1)))              ; try every first cut i = 1..j
            ((> i j))
          (let ((q (+ (vector-ref prices i)
                      (vector-ref r (- j i)))))
            (if (> q best)
                (begin
                  (set! best q)
                  (vector-set! s j i)))))
        (vector-set! r j best)))))

(define (reconstruct s n)
  "Walk the choice table to list the piece lengths in an optimal cut."
  (let loop ((k n) (acc '()))
    (if (= k 0)
        (reverse acc)
        (loop (- k (vector-ref s k))
              (cons (vector-ref s k) acc)))))

(define (main)
  (let ((n 8))
    (call-with-values
      (lambda () (bottom-up-cut-rod prices n))
      (lambda (r s)
        (display "Prices (length . price): ")
        (do ((i 1 (+ i 1))) ((> i 10))
          (display (cons i (vector-ref prices i))) (display " "))
        (newline)
        (display "Rod length n = ") (display n) (newline)
        (display "Maximum revenue = ") (display (vector-ref r n)) (newline)
        (display "Optimal cut (piece lengths) = ")
        (display (reconstruct s n)) (newline)))))

(main)