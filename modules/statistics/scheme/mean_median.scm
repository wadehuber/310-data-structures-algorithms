; Mean vs. Median: A Robustness Illustration
; -------------------------------------------
; A demonstration of the "Robust Statistics" idea from the "Medians & Order
; Statistics" notes:
;
;     Mean is sensitive to values.  Median is sensitive only to order.
;
; This script computes both, then injects a single extreme value and
; recomputes, so you can see the mean lurch toward the outlier while the
; median barely moves.  That is the whole point of calling the median
; *robust*: a small fraction of extreme values cannot significantly change it.
;
; (Computing the median here uses a sort for clarity.  As the notes explain --
; and as select_medians.scm / randselect.scm show -- the median can actually
; be found in Theta(n) time without fully sorting.)

; Arithmetic mean: sum of values divided by count. Uses every value.
(define (mean data)
  (/ (apply + data) (length data)))

; Middle value after ordering.  Depends only on relative order, not on how
; large the extreme values are.
(define (median data)
  (let* ((s (sort data <))
         (n (length data))
         (mid (quotient n 2)))
    (if (odd? n)
        (list-ref s mid)
        (/ (+ (list-ref s (- mid 1)) (list-ref s mid)) 2))))

(define (report label data)
  (display label) (newline)
  (display "  data:   ") (display data) (newline)
  (display "  mean:   ") (display (exact->inexact (mean data))) (newline)
  (display "  median: ") (display (exact->inexact (median data))) (newline)
  (newline))

; --- demonstration ---
; Server response times in milliseconds: tightly clustered, no outlier.
(define clean '(102 98 105 99 101 103 100 97 104))
(report "Clean readings:" clean)

; One request hit a stall (a 4000 ms spike). Same data plus one outlier.
(define with-outlier (append clean '(4000)))
(report "With one extreme outlier added:" with-outlier)

(display "Effect of the single outlier:") (newline)
(display "  mean   moved by ")
(display (exact->inexact (- (mean with-outlier) (mean clean))))
(display " ms  (chases the outlier)") (newline)
(display "  median moved by ")
(display (exact->inexact (- (median with-outlier) (median clean))))
(display " ms  (stays put -> robust)") (newline)
