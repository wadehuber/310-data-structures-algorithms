% quicksort.pl
%
% A Prolog port of the quicksort example for our DSA class.
% Adapted from the code provided with:
%   Java Foundations (2nd & 3rd ed) by Lewis, DePasquale, & Chase
%   Algorithms (4th ed) by Sedgewick & Wayne
%
% Prolog has no arrays to swap in place, so this is the classic
% *declarative* quicksort: take the head of the list as the pivot,
% partition the tail into the elements =< pivot and the elements > pivot,
% recursively sort each part, then join them with the pivot in between.
%
% Run:
%   swipl quicksort.pl
% (loading the file runs the demo, then halts)

% ---- Quicksort --------------------------------------------------------

% quicksort(+Unsorted, -Sorted)
quicksort([], []).
quicksort([Pivot|Tail], Sorted) :-
    partition_(Pivot, Tail, Smaller, Larger),
    quicksort(Smaller, SortedSmaller),
    quicksort(Larger, SortedLarger),
    append(SortedSmaller, [Pivot|SortedLarger], Sorted).

% partition_(+Pivot, +List, -Smaller, -Larger)
% Smaller holds the elements =< Pivot; Larger holds the elements > Pivot.
partition_(_, [], [], []).
partition_(Pivot, [H|T], [H|Smaller], Larger) :-
    H =< Pivot,
    !,
    partition_(Pivot, T, Smaller, Larger).
partition_(Pivot, [H|T], Smaller, [H|Larger]) :-
    H > Pivot,
    partition_(Pivot, T, Smaller, Larger).

% ---- Helpers ----------------------------------------------------------

% is_sorted(+List) succeeds when List is in non-decreasing order.
is_sorted([]).
is_sorted([_]).
is_sorted([A,B|T]) :-
    A =< B,
    is_sorted([B|T]).

% random_list(+N, +Max, -List) builds a list of N integers in 0..Max-1.
random_list(0, _, []) :- !.
random_list(N, Max, [X|Xs]) :-
    N > 0,
    Hi is Max - 1,
    random_between(0, Hi, X),
    N1 is N - 1,
    random_list(N1, Max, Xs).

% ---- Test harness -----------------------------------------------------

run_trial(Failures, Failures1) :-
    random_list(20, 1000, Unsorted),
    quicksort(Unsorted, Sorted),
    format("~nUnsorted: ~w~n", [Unsorted]),
    format("  Sorted: ~w~n", [Sorted]),
    ( is_sorted(Sorted)
    -> Failures1 = Failures
    ;  writeln('Fail!'), Failures1 is Failures + 1
    ).

run_trials(0, Failures, Failures) :- !.
run_trials(N, Failures, Final) :-
    N > 0,
    run_trial(Failures, Failures1),
    N1 is N - 1,
    run_trials(N1, Failures1, Final).

main :-
    run_trials(5, 0, Failures),
    nl,
    ( Failures =:= 0
    -> format("Test successful! (~w failures)~n", [Failures])
    ;  format("Test unsuccessful! (~w failures)~n", [Failures])
    ).

:- initialization(main, main).
