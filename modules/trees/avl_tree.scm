;;; AVL Tree (self-balancing BST)  (CSC310 Module 5 - Advanced Trees)
;;; ================================================================
;;;
;;; AVL invariant: at every node the balance factor (right height - left height)
;;; is in {-1, 0, 1}.  After a BST insert, rebalance with one of four cases:
;;;   LL -> right rotation        RR -> left rotation
;;;   LR -> left then right        RL -> right then left
;;;
;;; Run (GNU Guile):  guile avl_tree.scm

;; Simple tree node as list: (key left right height)
(define (mk key left right h) (list key left right h))
(define (avl-key n) (car n))
(define (avl-left n) (cadr n))
(define (avl-right n) (caddr n))
(define (avl-height n) (cadddr n))

(define (height n) (if (null? n) 0 (avl-height n)))

(define (node key left right)
  (mk key left right (+ 1 (max (height left) (height right)))))

(define (bf n) (- (height (avl-right n)) (height (avl-left n))))

(define (rot-left x)
  (let* ((y (avl-right x))
         (new-x (node (avl-key x) (avl-left x) (avl-left y))))
    (node (avl-key y) new-x (avl-right y))))

(define (rot-right y)
  (let* ((x (avl-left y))
         (new-y (node (avl-key y) (avl-right x) (avl-right y))))
    (node (avl-key x) (avl-left x) new-y)))

(define (insert n k)
  (if (null? n)
      (node k '() '())
      (let* ((nn (if (< k (avl-key n))
                     (node (avl-key n) (insert (avl-left n) k) (avl-right n))
                     (node (avl-key n) (avl-left n) (insert (avl-right n) k))))
             (b (bf nn)))
        (cond
          ((> b 1)                                    ; right heavy
           (if (< (bf (avl-right nn)) 0)
               (rot-left (node (avl-key nn) (avl-left nn)
                               (rot-right (avl-right nn))))   ; RL
               (rot-left nn)))                                ; RR
          ((< b -1)                                   ; left heavy
           (if (> (bf (avl-left nn)) 0)
               (rot-right (node (avl-key nn)
                                (rot-left (avl-left nn))
                                (avl-right nn)))               ; LR
               (rot-right nn)))                                ; LL
          (else nn)))))

(define (inorder n acc)
  (if (null? n) acc
      (inorder (avl-left n) (cons (avl-key n) (inorder (avl-right n) acc)))))

(define (preorder n acc)
  (if (null? n) acc
      (cons (avl-key n) (preorder (avl-left n) (preorder (avl-right n) acc)))))

(define (balanced? n)
  (or (null? n)
      (and (<= (abs (bf n)) 1) (balanced? (avl-left n)) (balanced? (avl-right n)))))

(define (main)
  (let ((keys '(50 20 70 10 30 60 80 5 25 35)))
    (let loop ((ks keys) (tree '()))
      (if (null? ks)
          (begin
            (display "insert order: ") (display keys) (newline)
            (display "inorder (sorted): ") (display (inorder tree '())) (newline)
            (display "preorder (structure): ") (display (preorder tree '())) (newline)
            (display "root: ") (display (avl-key tree))
            (display ", height: ") (display (height tree))
            (display ", balanced: ") (display (balanced? tree)) (newline))
          (loop (cdr ks) (insert tree (car ks)))))))

(main)