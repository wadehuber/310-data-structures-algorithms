;;; Floyd-Warshall All-Pairs Shortest Paths  (CSC310 Module 10)
;;; ===========================================================
;;;
;;; Floyd-Warshall: d^(k)[i,j] = min( d^(k-1)[i,j],
;;;                                   d^(k-1)[i,k] + d^(k-1)[k,j] ).
;;; After allowing every vertex k as an intermediate, D holds all-pairs shortest
;;; distances.  Handles negative edges (no negative cycle).  Time/space Theta(n^3)/Theta(n^2).
;;;
;;; Run (GNU Guile):  guile floyd_warshall.scm

(define n 5)
(define INF 1000000000)

;; Directed weighted edges (i j w), 1-indexed.
(define edges '((1 2 3) (1 3 8) (1 5 -4) (2 4 1) (2 5 7)
                (3 2 4) (4 1 2) (4 3 -5) (5 4 6)))

(define (make-matrix n)
  (let ((m (make-vector n)))
    (do ((i 0 (+ i 1))) ((= i n) m)
      (vector-set! m i (make-vector n INF)))))

(define (mref m i j) (vector-ref (vector-ref m i) j))
(define (mset! m i j v) (vector-set! (vector-ref m i) j v))

(define (init-matrix)
  (let ((D (make-matrix n)))
    (do ((i 0 (+ i 1))) ((= i n))      ; zero diagonal
      (mset! D i i 0))
    (for-each                          ; load edges (convert to 0-indexed)
      (lambda (e) (mset! D (- (car e) 1) (- (cadr e) 1) (caddr e)))
      edges)
    D))

(define (floyd-warshall D)
  (do ((k 0 (+ k 1))) ((= k n) D)
    (do ((i 0 (+ i 1))) ((= i n))
      (do ((j 0 (+ j 1))) ((= j n))
        (let ((dik (mref D i k))
              (dkj (mref D k j)))
          ;; Replaced (when ...) with (if ...) for R5RS compatibility
          (if (and (< dik INF) (< dkj INF)
                   (< (+ dik dkj) (mref D i j)))
              (mset! D i j (+ dik dkj))
              #f))))))

(define (print-number v)
  (if (>= v INF)
      (display "9999")
      (let ((s (number->string v)))
        (display (make-string (- 4 (string-length s)) #\space))
        (display s))))

(define (print-matrix D)
  (do ((i 0 (+ i 1))) ((= i n))
    (display "  ")
    (do ((j 0 (+ j 1))) ((= j n))
      (print-number (mref D i j)))
    (newline)))

(define (main)
  (display "Floyd-Warshall all-pairs shortest distances (CLRS Fig. 25.1):") (newline)
  (display "(rows/cols = vertices 1..5)") (newline)
  (print-matrix (floyd-warshall (init-matrix))))

(main)