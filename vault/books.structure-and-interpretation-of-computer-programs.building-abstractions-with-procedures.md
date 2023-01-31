---
id: rcc7fayzutpi6l4qvboz0cu
title: Building Abstractions with Procedures
desc: ''
updated: 1675096951117
created: 1675086563525
---

* Procedures should suppress details. 
* Users should not have to know how the procedure was implemented to use it.
* If you only want to write a sqrt procedure, the other procedures can be scoped inside sqrt.
```
(define (sqrt x)
    (define (good-enough? guess x)
        (< (abs (- (square guess) x)) 0.001))
    (define (improve guess x) 
        (average guess (/ x guess)))
    (define (sqrt-iter guess x)
        (if (good-enough? guess x)
            guess
            (sqrt-iter (improve guess x) x)))
    (sqrt-iter 1.0 x))
```
* Another way to improve this code is to allow x to be a free variable, instead of passing it around. This is known as _lexical scoping_.
```
(define (sqrt x)
    (define (average a b) (/ (+ a b) 2.0))
    (define (good-enough? guess)
        (< (abs (- (square guess) x)) 0.001))
    (define (improve guess) 
        (average guess (/ x guess)))
    (define (sqrt-iter guess)
        (if (good-enough? guess)
            guess
            (sqrt-iter (improve guess))))
    (sqrt-iter 1.0))
```
* Knowing that a program consists of data and operations is similar to knowing how the pieces move in chess. You still need to know tactics, strategy to know what moves are worth making.
* An expert programmer can visualize the consequences of their actions vividly, just like any other creative activity.
* Linear recursion
```
(define (factorial x) 
    (if (= x 1) 1
    (* x (factorial (- x 1)))))
```
* Linear iteration
```
(define (factorial x) 
    (define (iter product counter)
        (if (> counter x) 
            product
            (iter (* product counter) (+ counter 1))))
    (iter 1 1))
```
* In most languages, the amount of memory grows with the number of recursive calls, even when the process is, in principle, iterative. If a language executes an iterative process in constant space, it's called __tail recursive__.
* Fast exponentiation
```
(define (pow a b)
    (cond [(= b 0) 1]
          [(even? b) (square (pow a (/ b 2)))]
          [else (* a (pow a (- b 1)))]))
```
* **Fermat's Little Theorem**: If $$n$$ is a prime number and $$a$$ is a positive integer less than $$n$$, then $$a$$ raised to the $$n$$th power is congruent to $$a$$ modulo $$n$$.
* Prime testing probabilistically
```
(define (expmod base exp m)
    (cond [(= exp 0) 1]
          [(even? exp) (remainder (square (expmod base (/ exp 2) m)) m)]
          [else (remainder (* base (expmod base (- exp 1) m)) m)]))

(define (fermat-test n)
    (define (try-it a)
        (= (expmod a n n) a))
    (try-it (+ 1 (random (- n 1)))))

(define (prime? n times)
    (cond [(= times 0) true]
          [(fermat-test n) (prime? n (- times 1))]
          [else false]))
```
* Procedures that manipulate procedures are called higher-order procedures.