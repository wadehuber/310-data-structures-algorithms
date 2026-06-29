;;; Simple Graph Data Structure  (CSC310 Module 6B - Graphs)
;;; ========================================================
;;;
;;; Adjacency-list representation: a record holding an insertion-ordered vertex
;;; list and a hash table mapping each vertex to a list of (neighbor . weight).
;;;
;;; Uses association lists (no hash tables or SRFIs)
;;;
;;; Run (GNU Guile):  guile graph.scm

(define (make-graph)
  (cons '() '()))  ; (order . adj-alist)

(define (add-vertex! g v)
  (let ((order (car g))
        (adj   (cdr g)))
    (if (assoc v adj)
        #f
        (begin
          (set-car! g (append order (list v)))
          (set-cdr! g (cons (cons v '()) adj))
          #t))))

(define (add-edge! g u v w directed?)
  (add-vertex! g u)
  (add-vertex! g v)
  (let ((adj (cdr g)))
    ;; u -> v
    (let ((u-entry (assoc u adj)))
      (set-cdr! u-entry (cons (cons v w) (cdr u-entry))))
    ;; reverse for undirected
    (if (not directed?)
        (let ((v-entry (assoc v adj)))
          (set-cdr! v-entry (cons (cons u w) (cdr v-entry))))
        #f)))

(define (neighbors g v)
  (let ((entry (assoc v (cdr g))))
    (if entry
        (cdr entry)          ; no sort - fine for correctness
        '())))

(define (edge-weight g u v)
  (let ((u-entry (assoc u (cdr g))))
    (if u-entry
        (let ((hit (assoc v (cdr u-entry))))
          (and hit (cdr hit)))
        #f)))

(define (print-graph g)
  (display "Graph (undirected, weighted) - adjacency list:") (newline)
  (for-each
    (lambda (v)
      (display "  ") (display v) (display " -> ")
      (let loop ((ns (neighbors g v)) (first #t))
        (cond ((null? ns) (newline))
              (else
               (if (not first) (display ", "))
               (display (caar ns)) (display "(") (display (cdar ns)) (display ")")
               (loop (cdr ns) #f)))))
    (car g)))

(define (main)
  (let ((g (make-graph)))
    ;; Arizona road network example
    (for-each (lambda (v) (add-vertex! g v))
              '("PHX" "TUS" "MESA" "TEMPE"))
    (add-edge! g "PHX"  "MESA"  20  #f)
    (add-edge! g "PHX"  "TEMPE" 11  #f)
    (add-edge! g "MESA" "TEMPE" 8   #f)
    (add-edge! g "PHX"  "TUS"   116 #f)
    (add-edge! g "TUS"  "MESA"  100 #f)

    (print-graph g)

    (display "Neighbors of PHX: ")
    (let loop ((ns (neighbors g "PHX")) (first #t))
      (cond ((null? ns) (newline))
            (else
             (if (not first) (display ", "))
             (display (caar ns))
             (loop (cdr ns) #f))))
    (display "Weight PHX-MESA: ")
    (display (edge-weight g "PHX" "MESA"))
    (newline)))

(main)
