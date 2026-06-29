;;; Monte Carlo Estimation of Pi  (CSC310 Module 13 - Randomized Algorithms)
;;; =======================================================================
;;;
;;; This illustrates a MONTE CARLO algorithm (from the Las Vegas vs. Monte Carlo
;;; section of the notes): the running time is fixed by the number of samples,
;;; and the answer is approximate, getting more accurate with more samples.
;;;
;;; Idea: throw random points into the unit square [0,1) x [0,1).  The fraction
;;; that land inside the quarter circle of radius 1 approximates (area of quarter
;;; circle) / (area of square) = (pi/4) / 1, so pi ~= 4 * (inside / total).
;;;
;;; Run (GNU Guile):  guile monte_carlo_pi.scm

(use-modules (ice-9 format))   ; Guile: enables ~a / ~% directives

;; Reseed so each run differs (Guile-specific; remove if your Scheme lacks it).
(set! *random-state* (random-state-from-platform))

(define (estimate-pi n)
  "Estimate pi using n random sample points."
  (let loop ((i 0) (inside 0))
    (if (= i n)
        (/ (* 4.0 inside) n)
        (let ((x (random 1.0))
              (y (random 1.0)))
          (if (<= (+ (* x x) (* y y)) 1.0)
              (loop (+ i 1) (+ inside 1))
              (loop (+ i 1) inside))))))

(define (main)
  (display "Monte Carlo estimate of pi (true value 3.14159265...)") (newline)
  (display "------------------------------------------------------") (newline)
  (for-each
    (lambda (n)
      (let ((est (estimate-pi n)))
        (format #t "  n = ~a   estimate = ~a~%" n est)))
    '(100 1000 10000 100000 1000000))
  (newline)
  (display "More samples -> better estimate, but the running time is fixed by n,") (newline)
  (display "and the answer is never exact: that is the Monte Carlo trade-off.") (newline))

(main)
