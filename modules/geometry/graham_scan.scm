;;; Graham's Scan - Convex Hull  (CSC310 Module 15 - Computational Geometry)
;;; =======================================================================
;;;
;;; Graham's scan: pick the lowest point p0, sort the rest by polar angle around
;;; p0 (compared with the cross product, no trigonometry), then sweep with a
;;; stack, popping any point that is not a left turn.  O(n log n).
;;;
;;; Run (GNU Guile):  guile graham_scan.scm

(define points '((0 . 0) (2 . 0) (4 . 1) (4 . 4) (2 . 5)
                 (0 . 3) (2 . 2) (1 . 1) (3 . 2)))

(define (x p) (car p))
(define (y p) (cdr p))

;; cross product of (a-o) and (b-o)
(define (cross o a b)
  (- (* (- (x a) (x o)) (- (y b) (y o)))
     (* (- (y a) (y o)) (- (x b) (x o)))))

(define (dist2 o p)
  (+ (* (- (x p) (x o)) (- (x p) (x o)))
     (* (- (y p) (y o)) (- (y p) (y o)))))

;; lowest point
(define (lower a b)
  (if (or (< (y a) (y b))
          (and (= (y a) (y b)) (< (x a) (x b))))
      a b))

(define (lowest pts)
  (let loop ((best (car pts)) (rest (cdr pts)))
    (if (null? rest) best (loop (lower best (car rest)) (cdr rest)))))

;; portable filter
(define (my-filter pred lst)
  (cond ((null? lst) '())
        ((pred (car lst)) (cons (car lst) (my-filter pred (cdr lst))))
        (else (my-filter pred (cdr lst)))))

;; Simple insertion sort for R5RS
(define (insertion-sort lst pred)
  (define (insert x sorted)
    (cond ((null? sorted) (list x))
          ((pred x (car sorted)) (cons x sorted))
          (else (cons (car sorted) (insert x (cdr sorted))))))
  (if (null? lst)
      '()
      (insert (car lst) (insertion-sort (cdr lst) pred))))

(define (graham-scan pts)
  (let* ((p0 (lowest pts))
         (rest (my-filter (lambda (p) (not (equal? p p0))) pts))
         (sorted (insertion-sort rest
                   (lambda (a b)
                     (let ((c (cross p0 a b)))
                       (if (= c 0)
                           (< (dist2 p0 a) (dist2 p0 b))
                           (> c 0)))))))
    ;; sweep
    (let loop ((ps sorted) (stack (list p0)))
      (if (null? ps)
          (reverse stack)
          (let ((p (car ps)))
            (if (and (>= (length stack) 2)
                     (<= (cross (cadr stack) (car stack) p) 0))
                (loop ps (cdr stack))
                (loop (cdr ps) (cons p stack))))))))

(define (main)
  (let ((hull (graham-scan points)))
    (display "Convex hull (Graham's scan), CCW from the lowest point:") (newline)
    (for-each (lambda (p)
                (display "  ") (display (x p)) (display " ") (display (y p)) (newline))
              hull)
    (display "(") (display (length hull)) (display " hull vertices)") (newline)))

(main)