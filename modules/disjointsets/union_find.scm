;;; Disjoint-Set Forest (Union-Find)  (CSC310 Module 6A - Disjoint Sets)
;;; ==================================================================
;;;
;;; Forest-of-rooted-trees representation using two vectors: parent[] and rank[].
;;; FIND-SET uses recursive path compression; UNION links by rank.
;;;
;;; Run (GNU Guile):  guile union_find.scm

(define (make-dsu n)
  "Return (parent . rank) vectors; MAKE-SET each element to itself."
  (let ((parent (make-vector n))
        (rank   (make-vector n 0)))
    (do ((i 0 (+ i 1))) ((= i n))
      (vector-set! parent i i))
    (cons parent rank)))

(define (find dsu x)
  "Representative of x, with recursive path compression."
  (let ((parent (car dsu)))
    (if (= (vector-ref parent x) x)
        x
        (let ((root (find dsu (vector-ref parent x))))
          (vector-set! parent x root)        ; path compression
          root))))

(define (union! dsu x y)
  (let* ((parent (car dsu)) (rank (cdr dsu))
         (rx (find dsu x)) (ry (find dsu y)))
    (cond
      ((= rx ry) #t)                          ; already together
      ((> (vector-ref rank rx) (vector-ref rank ry))
       (vector-set! parent ry rx))
      (else
       (vector-set! parent rx ry)
       ;; Replaced (when ...) with (if ...) for R5RS
       (if (= (vector-ref rank rx) (vector-ref rank ry))
           (vector-set! rank ry (+ 1 (vector-ref rank ry)))
           #f)))))

(define (connected dsu x y) (= (find dsu x) (find dsu y)))

(define (print-sets dsu n)
  ;; group elements by representative, print each set with elements ascending
  (display "Sets: ")
  (do ((r 0 (+ r 1))) ((= r n))            ; r = candidate root in ascending order
    (if (= (find dsu r) r)
        (begin
          (display "{")
          (let ((first #t))
            (do ((x 0 (+ x 1))) ((= x n))
              (if (= (find dsu x) r)
                  (begin
                    (if (not first) (display ", "))
                    (display x)
                    (set! first #f))
                  #f)))
          (display "} "))
        #f))
  (newline))

(define (main)
  (let ((dsu (make-dsu 7)) (n 7))            ; elements 0..6
    (display "Disjoint-set forest (union by rank + path compression)") (newline)
    (display "Operations: union(0,1) union(2,3) union(1,3) union(4,5)") (newline)
    (union! dsu 0 1)
    (union! dsu 2 3)
    (union! dsu 1 3)
    (union! dsu 4 5)
    (print-sets dsu n)
    (display "connected(0,3)? ") (display (if (connected dsu 0 3) "true" "false")) (newline)
    (display "connected(0,4)? ") (display (if (connected dsu 0 4) "true" "false")) (newline)))

(main)