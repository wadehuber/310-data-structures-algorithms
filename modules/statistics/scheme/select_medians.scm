; Deterministic Selection (Median of Medians)
; --------------------------------------------
; The SELECT algorithm from the "Medians & Order Statistics" notes -- the
; worst-case O(n) selection algorithm, in contrast to RANDOMIZED-SELECT
; (randselect.scm), which is only O(n) *expected*.
;
; The trick is choosing a provably good pivot instead of a random one:
;   1. Split the elements into groups of 5.
;   2. Find each group's median (by sorting the tiny group).
;   3. Recursively SELECT the median OF those medians.
;   4. Partition around that "median of medians" -- it is guaranteed to be
;      far enough from the extremes that each recursive call shrinks the
;      problem by a constant fraction, which keeps the worst case linear.
;
; As the notes point out, this guarantee comes with larger constant factors,
; so in practice quickselect is usually preferred -- a classic case of
; theoretical optimality not matching real-world speed.

; First (up to) n elements of a list.
(define (take-up-to lst n)
  (if (or (= n 0) (null? lst))
      '()
      (cons (car lst) (take-up-to (cdr lst) (- n 1)))))

; The list with its first (up to) n elements removed.
(define (drop-up-to lst n)
  (if (or (= n 0) (null? lst))
      lst
      (drop-up-to (cdr lst) (- n 1))))

; Median of each successive group of 5, returned as a list.
(define (group-medians data)
  (if (null? data)
      '()
      (let* ((group (take-up-to data 5))
             (rest (drop-up-to data 5))
             (sorted-group (sort group <))
             (med (list-ref sorted-group (quotient (- (length group) 1) 2))))
        (cons med (group-medians rest)))))

; Split data into (less equal greater) relative to pivot.
(define (partition-by pivot data)
  (let loop ((d data) (less '()) (eq '()) (greater '()))
    (if (null? d)
        (list (reverse less) (reverse eq) (reverse greater))
        (let ((x (car d)))
          (cond ((< x pivot) (loop (cdr d) (cons x less) eq greater))
                ((> x pivot) (loop (cdr d) less eq (cons x greater)))
                (else        (loop (cdr d) less (cons x eq) greater)))))))

; Return the i-th smallest element of data (1-based) in worst-case O(n).
(define (median-of-medians-select data i)
  (let ((n (length data)))
    (if (<= n 5)
        (list-ref (sort data <) (- i 1))
        (let* ((medians (group-medians data))
               ; Step 3: median of the medians (recursively).
               (pivot (median-of-medians-select
                        medians (quotient (+ (length medians) 1) 2)))
               ; Step 4: partition around the pivot.
               (parts (partition-by pivot data))
               (less (car parts)) (eq (cadr parts)) (greater (caddr parts))
               (nl (length less)) (ne (length eq)))
          (cond ((<= i nl)        (median-of-medians-select less i))
                ((<= i (+ nl ne)) pivot)              ; pivot is the answer
                (else (median-of-medians-select greater (- i (+ nl ne)))))))))

; --- demonstration ---
(define A '(25 3 41 17 9 38 2 14 30 7 22 11 36 5 19 28 1 33 16))
(display "Array: ") (display A) (newline) (newline)

(define ordered (sort A <))
(define n (length A))

(define (rank-label i)
  (cond ((= i 1) "min")
        ((= i (+ (quotient n 2) 1)) "median")
        ((= i n) "max")
        (else "")))

(for-each
  (lambda (i)
    (let ((got (median-of-medians-select A i)))
      (display i) (display "th smallest (") (display (rank-label i)) (display "): ")
      (display got) (display "   (sorted check: ") (display (list-ref ordered (- i 1)))
      (display ")") (newline)))
  (list 1 (+ (quotient n 2) 1) n))

(newline)
; Confirm it agrees with a full sort for all ranks.
(define all-match
  (let loop ((i 1))
    (cond ((> i n) #t)
          ((= (median-of-medians-select A i) (list-ref ordered (- i 1)))
           (loop (+ i 1)))
          (else #f))))
(display "Matches sorted order for every rank: ") (display all-match) (newline)
