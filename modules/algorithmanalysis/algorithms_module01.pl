% CSC310 — Module 01: Algorithm Analysis
% Sample implementations in Prolog (SWI-Prolog).
%
% Prolog naturally expresses certain algorithms in this module:
%   - List membership corresponds directly to linear search
%   - Towers of Hanoi is one of the canonical Prolog examples
%   - Insertion sort and merge sort have elegant declarative forms
%
% Run all demos:
%   $ swipl -q -t run_demos algorithms_module01.pl
%
% Or interactively:
%   $ swipl algorithms_module01.pl
%   ?- linear_search([10,20,30,40,50], 30, I).      % I = 3
%   ?- merge_sort([5,2,8,1,9,3], S).                % S = [1,2,3,5,8,9]
%   ?- hanoi_count(10, N).                          % N = 1023


% --------------------------------------------------------------------


% --------------------------------------------------------------------
% 1. LINEAR SEARCH — return 1-based position of Target in List
%    Time: best Θ(1), worst Θ(n)
% --------------------------------------------------------------------
linear_search([X|_], X, 1) :- !.
linear_search([_|T], X, I) :-
    linear_search(T, X, I1),
    I is I1 + 1.

% --------------------------------------------------------------------
% 2. BINARY SEARCH on a sorted list
%    Prolog lists don't have O(1) random access, so this is not as
%    efficient as the array/vector form. We include it to mirror the
%    module's algorithm; in real Prolog code use library(assoc) or a
%    different data structure for fast lookups.
% --------------------------------------------------------------------
binary_search(List, Target, Index) :-
    length(List, N),
    binary_search_(List, Target, 0, N - 1, Index).

binary_search_(_, _, Lo, Hi, -1) :- Lo > Hi, !.
binary_search_(List, Target, Lo, Hi, Index) :-
    Mid is (Lo + Hi) // 2,
    nth0(Mid, List, V),
    (   V =:= Target -> Index = Mid
    ;   V  <  Target -> Lo1 is Mid + 1, binary_search_(List, Target, Lo1, Hi,  Index)
    ;                   Hi1 is Mid - 1, binary_search_(List, Target, Lo,  Hi1, Index)
    ).


% --------------------------------------------------------------------
% 3. INSERTION SORT
%    Time: best Θ(n), worst Θ(n^2)
% --------------------------------------------------------------------
insertion_sort([], []).
insertion_sort([H|T], Sorted) :-
    insertion_sort(T, SortedTail),
    insert(H, SortedTail, Sorted).

insert(X, [], [X]).
insert(X, [H|T], [X,H|T]) :- X =< H, !.
insert(X, [H|T], [H|R])    :- insert(X, T, R).


% --------------------------------------------------------------------
% 4. MERGE SORT — divide-and-conquer in declarative form
%    Time: Θ(n log n) in all cases
% --------------------------------------------------------------------
merge_sort([], []).
merge_sort([X], [X]).
merge_sort(List, Sorted) :-
    List = [_,_|_],                 % at least 2 elements
    split(List, Left, Right),
    merge_sort(Left,  SortedLeft),
    merge_sort(Right, SortedRight),
    merge(SortedLeft, SortedRight, Sorted).

% Split a list into two roughly equal halves via tortoise-and-hare.
split(List, Left, Right) :- split_(List, List, [], Left, Right).
split_(Slow, [], Acc, Left, Slow) :-
    reverse(Acc, Left).
split_(Slow, [_], Acc, Left, Slow) :-
    reverse(Acc, Left).
split_([S|Slow], [_,_|Fast], Acc, Left, Right) :-
    split_(Slow, Fast, [S|Acc], Left, Right).

merge([], R, R).
merge(L, [], L).
merge([X|Xs], [Y|Ys], [X|Rest]) :- X =< Y, !, merge(Xs, [Y|Ys], Rest).
merge([X|Xs], [Y|Ys], [Y|Rest]) :- merge([X|Xs], Ys, Rest).


% --------------------------------------------------------------------
% 5. TOWERS OF HANOI — the canonical Prolog program
%    hanoi(+N, +From, +To, +Via, -Moves)
% --------------------------------------------------------------------
hanoi(0, _, _, _, []) :- !.
hanoi(N, From, To, Via, Moves) :-
    N > 0,
    N1 is N - 1,
    hanoi(N1, From, Via, To, M1),
    hanoi(N1, Via, To, From, M2),
    append(M1, [move(From, To)|M2], Moves).

% Often we just want the count, not the list of moves.
%   T(n) = 2 T(n-1) + 1   →   T(n) = 2^n - 1
hanoi_count(0, 0) :- !.
hanoi_count(N, C) :-
    N > 0,
    N1 is N - 1,
    hanoi_count(N1, C1),
    C is 2 * C1 + 1.


% --------------------------------------------------------------------
% 6. RECURSIVE vs TAIL-RECURSIVE factorial
%    Both are Θ(n) time. With first-argument indexing and last-call
%    optimization, the accumulator version runs in Θ(1) stack space.
% --------------------------------------------------------------------
factorial_naive(0, 1) :- !.
factorial_naive(N, F) :-
    N > 0,
    N1 is N - 1,
    factorial_naive(N1, F1),
    F is N * F1.

factorial_tail(N, F) :- factorial_tail_(N, 1, F).
factorial_tail_(0, Acc, Acc) :- !.
factorial_tail_(N, Acc, F) :-
    N > 0,
    Acc1 is Acc * N,
    N1 is N - 1,
    factorial_tail_(N1, Acc1, F).


% --------------------------------------------------------------------
% DEMO
% --------------------------------------------------------------------
run_demos :-
    format("=== Linear Search ===~n"),
    linear_search([10,20,30,40,50,60,70,80,90,100], 70, I),
    format("  Found 70 at position ~w~n", [I]),

    format("=== Binary Search ===~n"),
    binary_search([10,20,30,40,50,60,70,80,90,100], 70, J),
    format("  Found 70 at index ~w (0-based)~n", [J]),

    format("=== Insertion Sort ===~n"),
    insertion_sort([5,2,8,1,9,3,7,4,6], S1),
    format("  ~w~n", [S1]),

    format("=== Merge Sort ===~n"),
    merge_sort([38,27,43,3,9,82,10,5,1,100], S2),
    format("  ~w~n", [S2]),

    format("=== Towers of Hanoi (n=3) ===~n"),
    hanoi(3, a, c, b, Moves),
    forall(member(move(F,T), Moves),
           format("  ~w -> ~w~n", [F,T])),

    format("=== Hanoi move count ===~n"),
    hanoi_count(10, Cnt),
    format("  n=10 takes ~w moves (2^10 - 1 = 1023)~n", [Cnt]),

    format("=== Factorial ===~n"),
    factorial_tail(10, F),
    format("  10! = ~w~n", [F]).
