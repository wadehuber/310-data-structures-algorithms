;;; Kruskal's Minimum Spanning Tree  (CSC310 Module 9 - Spanning Trees)
;;; ==================================================================
;;;
;;; Kruskal: consider edges in increasing weight order; add an edge only if its
;;; endpoints are in different components (no cycle), merging them via union-find.
;;; Stop at n-1 edges.  Expected total weight for this graph: 14.
;;;
;;; Run (GNU Guile):  guile kruskal.scm

;; Undirected weighted edges (u v w).  DISTINCT from every assignment graph.

(define edges '((0 1 4) (0 2 3) (1 2 1) (1 3 2)
                (2 3 4) (3 4 2) (4 5 6) (3 5 8) (2 4 5)))
(define num-vertices 6)

;; ---- Union-Find with path compression ----
(define (make-uf n)
  (let ((parent (make-vector n)))
    (do ((i 0 (+ i 1))) ((= i n) parent)
      (vector-set! parent i i))))

(define (uf-find parent x)
  (if (= (vector-ref parent x) x)
      x
      (let ((root (uf-find parent (vector-ref parent x))))
        (vector-set! parent x root)
        root)))

(define (uf-union! parent x y)
  (vector-set! parent (uf-find parent x) (uf-find parent y)))

;; Simple insertion sort (R5RS compatible, no built-in sort)
(define (sort-edges es)
  (if (null? es)
      '()
      (let insert ((e (car es)) (rest (sort-edges (cdr es))))
        (cond ((null? rest) (list e))
              ((< (caddr e) (caddr (car rest))) (cons e rest))
              (else (cons (car rest) (insert e (cdr rest))))))))

(define (kruskal edges n)
  (let ((parent (make-uf n))
        (sorted (sort-edges edges)))
    (let loop ((es sorted) (mst '()) (total 0))
      (if (null? es)
          (values (reverse mst) total)
          (let* ((e (car es))
                 (u (car e))
                 (v (cadr e))
                 (w (caddr e)))
            (if (= (uf-find parent u) (uf-find parent v))
                (loop (cdr es) mst total)          ; cycle -> skip
                (begin
                  (uf-union! parent u v)
                  (loop (cdr es) (cons e mst) (+ total w)))))))))

(define (main)
  (call-with-values
    (lambda () (kruskal edges num-vertices))
    (lambda (mst total)
      (display "Kruskal's MST edges (u v w):") (newline)
      (for-each (lambda (e)
                  (display "  ") (display e) (newline))
                mst)
      (display "Total weight: ") (display total) (newline))))

(main)