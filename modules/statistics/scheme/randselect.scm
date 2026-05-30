; Randomized Selection (Quickselect)
; ----------------------------------
; RANDOMIZED-SELECT from the "Medians & Order Statistics" notes: find the
; i-th smallest element (1-based) of a list in Theta(n) expected time.
;
; It reuses quicksort's partition, but recurses into only the one side that
; must contain the answer -- so on average it does linear work instead of
; the n log n a full sort would cost.

(define (swap! A i j)
  (let ((tmp (vector-ref A i)))
    (vector-set! A i (vector-ref A j))
    (vector-set! A j tmp)))

; Standard Lomuto partition scheme over the vector slice A[p..r].
(define (partition! A p r)
  (let ((pivot (vector-ref A r))
        (i (- p 1)))
    (do ((j p (+ j 1))) ((= j r))
      (when (<= (vector-ref A j) pivot)
        (set! i (+ i 1))
        (swap! A i j)))
    (swap! A (+ i 1) r)
    (+ i 1)))

; Chooses a random pivot, swaps it with A[r], then partitions around it.
; Returns the final pivot index.
(define (randomized-partition! A p r)
  (let ((pivot-index (+ p (random (+ (- r p) 1)))))
    (swap! A pivot-index r)
    (partition! A p r)))

; Returns the i-th smallest element of A[p..r] (i is 1-based).
(define (randomized-select-range A p r i)
  (if (= p r)
      (vector-ref A p)
      (let* ((q (randomized-partition! A p r))
             (k (+ (- q p) 1)))     ; rank of pivot within the slice
        (cond ((= i k) (vector-ref A q))
              ((< i k) (randomized-select-range A p (- q 1) i))
              (else    (randomized-select-range A (+ q 1) r (- i k)))))))

; Returns the i-th smallest element of the list (i is 1-based).
; Copies into a fresh vector so the caller's list is left untouched.
(define (randomized-select lst i)
  (let ((A (list->vector lst)))
    (randomized-select-range A 0 (- (vector-length A) 1) i)))

; --- demonstration ---
(define A '(13 19 9 5 12 8 7 4 21 2 6 11))
(define i 5)   ; Find the 5th smallest element

(display "Original array: ") (display A) (newline)
(display i) (display "th smallest element: ") (display (randomized-select A i)) (newline)

; Verification.
(define sorted-A (sort A <))
(display "Sorted array: ") (display sorted-A) (newline)
(display "Check: ") (display (list-ref sorted-A (- i 1))) (newline)
