# Randomized Algorithms

Code examples for **Module 13 — Randomized Algorithms** (CLRS Ch. 5). 
Randomized algorithms use internal randomness so their expected
performance holds for *every* input, defeating adversarial orderings. The notes
also cover probabilistic analysis with indicator random variables.

## Las Vegas vs. Monte Carlo 

- **Las Vegas** — always correct, running time varies (e.g. randomized
  quicksort).
- **Monte Carlo** — bounded running time, small chance of a wrong answer (e.g.
  Miller–Rabin, Monte Carlo π).

## Running

```bash
# Miller-Rabin
python3 miller_rabin.py
gcc -O2 miller_rabin.c -o miller_rabin && ./miller_rabin

# Probabilistic analysis demos
python3 balls_and_bins.py
python3 coin_streaks.py

# Monte Carlo pi  (Scheme)
guile monte_carlo_pi.scm

# Fermat Primality Test
python3 fermattest.py
g++ -O2 fermattest.cpp -o fermattest && ./fermattest

# Randomized Quicksort
python3 quicksort.py
```

## Where each ties back to the notes

- *Randomized Primality Testing / Miller–Rabin* → `miller_rabin.py`, `miller_rabin.c`, `fermattest.*`
- *Las Vegas vs. Monte Carlo Algorithms* → `quicksort.py` (Las Vegas), `miller_rabin.*` and `monte_carlo_pi.scm` (Monte Carlo)
- *Balls and Bins (load balancing/hashing)* → `balls_and_bins.py`
- *Streaks in Coin Flips* → `coin_streaks.py`
