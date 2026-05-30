; Counting Sort
; -------------
; A demonstration of the stable counting sort described in the
; "Sorting in Linear Time" notes.
;
; Counting sort works when the input is integers in a small, known range
; {0, 1, ..., k}.  It runs in Theta(n + k) time, which is linear when k = O(n).
;
; This example sorts a list of small integer "class labels" -- the kind of
; bounded-range data the notes mention (one-hot category indices, histogram
; bins, discretized features) -- so you can watch the three passes in action.

; Return a sorted list, where every element is an integer in 0..k.
;
; Mirrors the stable pseudocode from the notes:
;   1. Count occurrences of each value.
;   2. Turn counts into cumulative end-positions.
;   3. Place elements right-to-left to keep equal keys stable.
(define (counting-sort lst k)
  (let* ((A (list->vector lst))
         (n (vector-length A))
         (C (make-vector (+ k 1) 0))     ; C[v] counts how many times v appears
         (B (make-vector n 0)))          ; output vector
    ; Pass 1: tally each value.
    (do ((j 0 (+ j 1))) ((= j n))
      (let ((v (vector-ref A j)))
        (vector-set! C v (+ (vector-ref C v) 1))))
    ; Pass 2: cumulative sums -> C[v] is the ending position of value v.
    (do ((v 1 (+ v 1))) ((> v k))
      (vector-set! C v (+ (vector-ref C v) (vector-ref C (- v 1)))))
    ; Pass 3: walk right-to-left so equal keys keep their original order.
    (do ((j (- n 1) (- j 1))) ((< j 0))
      (let ((v (vector-ref A j)))
        (vector-set! C v (- (vector-ref C v) 1))
        (vector-set! B (vector-ref C v) v)))
    (vector->list B)))

; Stable counting sort on (key . tag) pairs, keyed by the integer key.
;
; The tag carries along unchanged so you can SEE stability: items with the
; same key come out in the same order they went in.  This stability is
; exactly the property radix sort relies on.
(define (counting-sort-pairs pairs k)
  (let* ((A (list->vector pairs))
         (n (vector-length A))
         (C (make-vector (+ k 1) 0))
         (B (make-vector n #f)))
    (do ((j 0 (+ j 1))) ((= j n))
      (let ((key (car (vector-ref A j))))
        (vector-set! C key (+ (vector-ref C key) 1))))
    (do ((v 1 (+ v 1))) ((> v k))
      (vector-set! C v (+ (vector-ref C v) (vector-ref C (- v 1)))))
    (do ((j (- n 1) (- j 1))) ((< j 0))
      (let* ((p (vector-ref A j)) (key (car p)))
        (vector-set! C key (- (vector-ref C key) 1))
        (vector-set! B (vector-ref C key) p)))
    (vector->list B)))

(define (display-pairs pairs)
  (display "(")
  (let loop ((ps pairs) (first #t))
    (cond ((null? ps) (display ")"))
          (else
            (if (not first) (display " "))
            (let ((p (car ps)))
              (display "(") (display (car p)) (display " ") (display (cdr p)) (display ")"))
            (loop (cdr ps) #f)))))

; --- demonstration ---
(define labels '(3 0 5 2 3 1 0 4 2 3 5 1 0))
(display "Input labels: ") (display labels) (newline)
(display "Counting sorted: ") (display (counting-sort labels 5)) (newline)
(display "Library sorted:  ") (display (sort labels <)) (newline)
(newline)

; Show stability: each pair is (key . arrival-order).
; After sorting by key, equal keys must stay in arrival order.
(define pairs '((2 . "a") (1 . "b") (2 . "c") (0 . "d") (1 . "e") (2 . "f")))
(display "Stable sorted: ") (display-pairs (counting-sort-pairs pairs 2)) (newline)
(display "Notice the (2 ...) items stay in a, c, f order -> stable.") (newline)
