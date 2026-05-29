;; CSC310 — Module 01: Algorithm Analysis
;; Sample implementations in Scheme (R7RS / R6RS portable).
;;
;; Scheme is a particularly good language for this module because:
;;   - Recursion is idiomatic, so divide-and-conquer reads naturally.
;;   - Tail recursion makes the "recursive vs iterative" distinction
;;     concrete: a tail-recursive procedure runs in Θ(1) stack space.
;;
;; Tested with: DrRacket 7.7 and guile 3.0 
;;   $ guile algorithms_module01.scm
;;   $ csi -s algorithms_module01.scm

;; --------------------------------------------------------------------
;; 1. LINEAR SEARCH on a list
;;    Time  : best Θ(1), worst Θ(n)
;;    Space : Θ(n) in naive recursion, Θ(1) when tail-recursive
;; --------------------------------------------------------------------
(define (linear-search lst target)
  ;; Tail-recursive form — Scheme implementations must optimize tail calls,
  ;; so this runs in constant stack space.
  (let loop ((xs lst) (i 0))
    (cond ((null? xs)            -1)
          ((equal? (car xs) target) i)
          (else (loop (cdr xs) (+ i 1))))))

;; --------------------------------------------------------------------
;; 2. BINARY SEARCH on a vector (sorted)
;;    Time  : worst Θ(log n).  Requires Θ(1)-access indexing → vector, not list.
;; --------------------------------------------------------------------
(define (binary-search vec target)
  (let loop ((lo 0) (hi (- (vector-length vec) 1)))
    (if (> lo hi)
        -1
        (let* ((mid (quotient (+ lo hi) 2))
               (v   (vector-ref vec mid)))
          (cond ((= v target) mid)
                ((< v target) (loop (+ mid 1) hi))
                (else         (loop lo (- mid 1))))))))

;; --------------------------------------------------------------------
;; 3. INSERTION SORT  (CLRS Figure 2.1, functional style)
;;    Time  : best Θ(n), worst Θ(n^2)
;;    Space : Θ(n) here because lists are immutable; the in-place
;;            array version is Θ(1), but functional Scheme builds new lists.
;; --------------------------------------------------------------------
(define (insertion-sort lst)
  (define (insert x sorted)
    (cond ((null? sorted)      (list x))
          ((<= x (car sorted)) (cons x sorted))
          (else                (cons (car sorted) (insert x (cdr sorted))))))
  (if (null? lst)
      '()
      (insert (car lst) (insertion-sort (cdr lst)))))

;; --------------------------------------------------------------------
;; 4. MERGE SORT — the divide-and-conquer poster child
;;    Recurrence: T(n) = 2 T(n/2) + Θ(n)   →   Θ(n log n)
;; --------------------------------------------------------------------
(define (merge-sort lst)
  (define (split xs)
    (let loop ((slow xs) (fast xs) (acc '()))
      (if (or (null? fast) (null? (cdr fast)))
          (values (reverse acc) slow)
          (loop (cdr slow) (cddr fast) (cons (car slow) acc)))))
  (define (merge a b)
    (cond ((null? a) b)
          ((null? b) a)
          ((<= (car a) (car b))
           (cons (car a) (merge (cdr a) b)))
          (else
           (cons (car b) (merge a (cdr b))))))
  (if (or (null? lst) (null? (cdr lst)))
      lst
      (call-with-values
        (lambda () (split lst))
        (lambda (left right)
          (merge (merge-sort left) (merge-sort right))))))

;; --------------------------------------------------------------------
;; 5. TOWERS OF HANOI — canonical Θ(2^n) recursive algorithm
;;    Returns the list of moves; each move is (from . to).
;; --------------------------------------------------------------------
(define (hanoi n from to via)
  (if (= n 0)
      '()
      (append (hanoi (- n 1) from via to)
              (list (cons from to))
              (hanoi (- n 1) via to from))))

;; --------------------------------------------------------------------
;; 6. RECURSIVE vs TAIL-RECURSIVE (= iterative under the hood)
;;    Both are Θ(n) time. The naive recursive form uses Θ(n) stack
;;    frames; the tail-recursive form runs in Θ(1) stack.
;; --------------------------------------------------------------------
(define (factorial-naive n)               ; Θ(n) time, Θ(n) stack
  (if (<= n 1) 1
      (* n (factorial-naive (- n 1)))))

(define (factorial-tail n)                ; Θ(n) time, Θ(1) stack
  (let loop ((k n) (acc 1))
    (if (<= k 1) acc
        (loop (- k 1) (* acc k)))))

;; --------------------------------------------------------------------
;; 7. COUNTING COMPARISONS — easier with a mutable closure
;; --------------------------------------------------------------------
(define (make-counter)
  (let ((n 0))
    (lambda msg
      (cond ((null? msg)           n)
            ((eq? (car msg) 'inc!) (set! n (+ n 1)) n)
            ((eq? (car msg) 'reset!) (set! n 0))))))

(define (linear-search/count lst target)
  (let ((c (make-counter)))
    (let loop ((xs lst) (i 0))
      (cond ((null? xs)            (values -1 (c)))
            (else
             (c 'inc!)
             (if (equal? (car xs) target)
                 (values i (c))
                 (loop (cdr xs) (+ i 1))))))))

;; --------------------------------------------------------------------
;; DEMO
;; --------------------------------------------------------------------
(define (range-list lo hi)
  (if (> lo hi) '() (cons lo (range-list (+ lo 1) hi))))

(define (run-demos)
  (display "=== Linear Search ===") (newline)
  (call-with-values
    (lambda () (linear-search/count (range-list 1 1000) 750))
    (lambda (idx cmps)
      (display "Found at index ") (display idx)
      (display " with ") (display cmps) (display " comparisons.")
      (newline)))

  (display "=== Binary Search ===") (newline)
  (let* ((v (list->vector (range-list 1 1000)))
         (idx (binary-search v 750)))
    (display "Found at index ") (display idx) (newline)
    (display "log2 1000 ≈ 10 — about that many comparisons max.") (newline))

  (display "=== Insertion Sort ===") (newline)
  (display (insertion-sort '(5 2 8 1 9 3 7 4 6))) (newline)

  (display "=== Merge Sort ===") (newline)
  (display (merge-sort '(38 27 43 3 9 82 10 5 1 100))) (newline)

  (display "=== Towers of Hanoi (n=3) ===") (newline)
  (for-each
    (lambda (m)
      (display "  ") (display (car m))
      (display " -> ") (display (cdr m)) (newline))
    (hanoi 3 'A 'C 'B))
  (display "Total moves for n=10: ")
  (display (length (hanoi 10 'A 'C 'B)))
  (display " (2^10 - 1 = 1023)") (newline)

  (display "=== Factorial: naive vs tail-recursive ===") (newline)
  (display "10! = ") (display (factorial-naive 10)) (newline)
  (display "10! = ") (display (factorial-tail  10)) (newline)
  (display "Tail-recursive form handles much larger n without stack growth.")
  (newline))

(run-demos)
