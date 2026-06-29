;;; Separate-Chaining Hash Table with Resizing  (CSC310 Module 4B - Hashing)
;;; =======================================================================
;;;
;;; Separate chaining: a vector of buckets, each an association list of
;;; (key . value).  When the load factor count/capacity exceeds 0.75, the table
;;; doubles and every entry is rehashed.  Keys are strings, values are numbers.
;;;
;;; Run (GNU Guile):  guile hash_table.scm

(define (make-ht cap)
  (vector (make-vector cap '()) 0))  ; #(buckets count)

(define (ht-buckets ht) (vector-ref ht 0))
(define (ht-count ht) (vector-ref ht 1))
(define (set-ht-buckets! ht new-buckets) (vector-set! ht 0 new-buckets))
(define (set-ht-count! ht new-count) (vector-set! ht 1 new-count))

(define (ht-capacity ht) (vector-length (ht-buckets ht)))
(define (ht-load ht)
  (if (= (ht-capacity ht) 0)
      0.0
      (/ (ht-count ht) (ht-capacity ht))))

;; polynomial string hash
(define (ht-hash key cap)
  (let loop ((chars (string->list key)) (h 0))
    (if (null? chars)
        (modulo h cap)
        (loop (cdr chars) (+ (* h 31) (char->integer (car chars)))))))

(define (ht-put! ht key value)
  (let* ((cap (ht-capacity ht))
         (idx (ht-hash key cap))
         (bucket (vector-ref (ht-buckets ht) idx))
         (pair (assoc key bucket)))
    (if pair
        (set-cdr! pair value)
        (begin
          (vector-set! (ht-buckets ht) idx (cons (cons key value) bucket))
          (set-ht-count! ht (+ 1 (ht-count ht)))
          ;; load factor check
          (if (> (/ (ht-count ht) cap) 0.75)
              (ht-resize! ht (* cap 2))
              #f)))))

(define (ht-resize! ht new-cap)
  (let ((old (ht-buckets ht)))
    (set-ht-buckets! ht (make-vector new-cap '()))
    (set-ht-count! ht 0)
    (do ((i 0 (+ i 1))) ((= i (vector-length old)))
      (for-each (lambda (kv) (ht-put! ht (car kv) (cdr kv)))
                (vector-ref old i)))))

(define (ht-get ht key)
  (let* ((bucket (vector-ref (ht-buckets ht) (ht-hash key (ht-capacity ht))))
         (pair (assoc key bucket)))
    (if pair (cdr pair) #f)))

(define (ht-remove! ht key)
  (let* ((idx (ht-hash key (ht-capacity ht)))
         (bucket (vector-ref (ht-buckets ht) idx)))
    (if (assoc key bucket)
        (begin
          (vector-set! (ht-buckets ht) idx
                       (filter (lambda (kv) (not (string=? (car kv) key))) bucket))
          (set-ht-count! ht (- (ht-count ht) 1)))
        #f)))

;; Simple filter for R5RS
(define (filter pred lst)
  (if (null? lst)
      '()
      (if (pred (car lst))
          (cons (car lst) (filter pred (cdr lst)))
          (filter pred (cdr lst)))))

(define (main)
  (let ((t (make-ht 4))
        (names '("Andy" "Maribel" "Zoey" "Julie" "Ann" "Stephen"))
        (age 20))
    (for-each
      (lambda (nm)
        (ht-put! t nm age)
        (set! age (+ age 1))
        (display "put ") (display nm)
        (display " -> capacity now ") (display (ht-capacity t))
        (display ", load ") (display (ht-load t)) (newline))
      names)
    (newline)
    (display "get Zoey: ") (display (ht-get t "Zoey")) (newline)
    (ht-remove! t "Zoey")
    (display "after remove Zoey, get Zoey: ")
    (display (if (ht-get t "Zoey") (ht-get t "Zoey") "absent")) (newline)
    (display "size=") (display (ht-count t))
    (display ", capacity=") (display (ht-capacity t)) (newline)))

(main)