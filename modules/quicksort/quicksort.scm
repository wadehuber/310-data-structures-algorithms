;;; quicksort.scm
;;;
;;; A Scheme port of the quicksort example for our DSA class.
;;; Adapted from the code provided with:
;;;   Java Foundations (2nd & 3rd ed) by Lewis, DePasquale, & Chase
;;;   Algorithms (4th ed) by Sedgewick & Wayne
;;;
;;; Where the Java/C++/Go versions sort an array in place, Scheme leans on
;;; lists and recursion, so this is the classic *functional* quicksort:
;;; pick a pivot, build the sublists of smaller and larger elements, and
;;; recurse.  No mutation required.
;;;
;;; Run (examples):
;;;   chibi-scheme quicksort.scm
;;;   csi -s quicksort.scm        ; Chicken Scheme
;;;   mit-scheme < quicksort.scm

;; ---- Helper operations ------------------------------------------------

;; Return the element at the middle of a list (our pivot choice, matching
;; the middle-element pivot used in the other ports).
(define (middle-element lst)
  (list-ref lst (quotient (length lst) 2)))

;; Is the list sorted in non-decreasing order?
(define (sorted? lst)
  (cond
    ((null? lst) #t)
    ((null? (cdr lst)) #t)
    ((> (car lst) (cadr lst)) #f)
    (else (sorted? (cdr lst)))))

;; ---- Quicksort --------------------------------------------------------

(define (quicksort lst)
  (if (or (null? lst) (null? (cdr lst)))
      lst                               ; 0 or 1 elements: already sorted
      (let ((pivot (middle-element lst)))
        ;; Partition the *remaining* elements around the pivot.  We drop a
        ;; single copy of the pivot so duplicates are still handled.
        (let loop ((rest lst)
                   (seen-pivot #f)
                   (smaller '())
                   (larger '()))
          (cond
            ((null? rest)
             (append (quicksort (reverse smaller))
                     (list pivot)
                     (quicksort (reverse larger))))
            ((and (not seen-pivot) (= (car rest) pivot))
             (loop (cdr rest) #t smaller larger))
            ((< (car rest) pivot)
             (loop (cdr rest) seen-pivot (cons (car rest) smaller) larger))
            (else
             (loop (cdr rest) seen-pivot smaller (cons (car rest) larger))))))))

;; ---- Test harness -----------------------------------------------------

;; A tiny, self-contained linear congruential generator so the demo does
;; not depend on any particular Scheme's random primitive.
(define rng-state 123456789)
(define (next-random modulus)
  (set! rng-state (modulo (+ (* rng-state 1103515245) 12345) 2147483648))
  (modulo rng-state modulus))

(define (random-list n modulus)
  (if (= n 0)
      '()
      (cons (next-random modulus) (random-list (- n 1) modulus))))

(define (print-list lst)
  (for-each (lambda (x) (display x) (display " ")) lst)
  (newline))

(define (run-tests)
  (let loop ((kk 0) (failures 0))
    (if (= kk 5)
        (begin
          (newline)
          (if (= failures 0)
              (begin (display "Test successful! (") (display failures)
                     (display " failures)") (newline))
              (begin (display "Test unsuccessful! (") (display failures)
                     (display " failures)") (newline))))
        (let* ((unsorted (random-list 20 1000))
               (sorted (quicksort unsorted)))
          (display "\nUnsorted: ") (print-list unsorted)
          (display "  Sorted: ") (print-list sorted)
          (if (sorted? sorted)
              (loop (+ kk 1) failures)
              (begin (display "Fail!") (newline)
                     (loop (+ kk 1) (+ failures 1))))))))

(run-tests)
