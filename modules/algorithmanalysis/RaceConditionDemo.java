/*
 * CSC310 — Module 01: Race Condition Demonstration
 *
 * The module notes describe a shared counter being read, incremented, and
 * written without synchronization. This file demonstrates the actual data
 * loss using Java threads.
 *
 * Compile: javac RaceConditionDemo.java
 * Run    : java  RaceConditionDemo
 *
 * Why this fits in an algorithm-analysis module:
 *   An operation we *assumed* was Θ(1) — incrementing a counter — turns
 *   out to be incorrect under concurrent access. The "race condition"
 *   section of the notes warns that complexity assumptions can quietly
 *   fail when an algorithm is reused in a multi-threaded context.
 */

import java.util.concurrent.atomic.AtomicLong;

public class RaceConditionDemo {

    // The "unsafe" counter mirrors the pseudocode in the notes:
    //     read counter ; counter = counter + 1 ; write counter
    //
    // On a real multi-core machine, plain `value = value + 1` is already
    // unsafe and loses updates. The Thread.yield() between read and write
    // here just *guarantees* the race manifests, including on single-core
    // virtualized environments.
    static class UnsafeCounter {
        long value = 0;
        void increment() {
            long current = value;        // READ
            Thread.yield();              // force a scheduler switch opportunity
            value = current + 1;         // WRITE — may overwrite another thread
        }
    }

    // Two correct alternatives: synchronized block, or AtomicLong.
    static class SynchronizedCounter {
        long value = 0;
        synchronized void increment() {
            long current = value;
            Thread.yield();
            value = current + 1;
        }
    }

    static class AtomicCounter {
        final AtomicLong value = new AtomicLong(0);
        void increment() { value.incrementAndGet(); }
        long get() { return value.get(); }
    }

    public static void main(String[] args) throws InterruptedException {
        final int THREADS    = 8;
        final int ITERATIONS = 20_000;
        final long EXPECTED  = (long) THREADS * ITERATIONS;

        // ----- UnsafeCounter: expect data loss -----
        UnsafeCounter unsafe = new UnsafeCounter();
        runWith(THREADS, ITERATIONS, unsafe::increment);
        System.out.printf("UnsafeCounter      : expected %,d, got %,d, lost %,d%n",
                EXPECTED, unsafe.value, EXPECTED - unsafe.value);

        // ----- SynchronizedCounter: should be exact -----
        SynchronizedCounter sync = new SynchronizedCounter();
        runWith(THREADS, ITERATIONS, sync::increment);
        System.out.printf("SynchronizedCounter: expected %,d, got %,d, lost %,d%n",
                EXPECTED, sync.value, EXPECTED - sync.value);

        // ----- AtomicCounter: should be exact, often faster than locking -----
        AtomicCounter atomic = new AtomicCounter();
        runWith(THREADS, ITERATIONS, atomic::increment);
        System.out.printf("AtomicCounter      : expected %,d, got %,d, lost %,d%n",
                EXPECTED, atomic.get(), EXPECTED - atomic.get());

        System.out.println("\nTake-away: a Θ(1) increment is *not* Θ(1) when shared,");
        System.out.println("and may not even be correct. Algorithm complexity always");
        System.out.println("rests on assumptions — concurrency can invalidate them.");
    }

    /** Spawn `threads` workers each calling `action` `iterations` times. */
    private static void runWith(int threads, int iterations, Runnable action)
            throws InterruptedException {
        Thread[] pool = new Thread[threads];
        for (int t = 0; t < threads; t++) {
            pool[t] = new Thread(() -> {
                for (int i = 0; i < iterations; i++) action.run();
            });
            pool[t].start();
        }
        for (Thread t : pool) t.join();
    }
}
