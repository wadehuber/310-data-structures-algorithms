% Activity Selection  (CSC310 Module 12 - Greedy Algorithms)
% ==========================================================
%
% Greedy rule: sort activities by finish time, then repeatedly take the next
% activity whose start time is >= the finish time of the last one selected.
% Prolog expresses this declaratively.
%
% Run (SWI-Prolog):     swipl -g main -t halt activity_selection.pl
% Run (SICStus):        sicstus -l activity_selection.pl --goal "main."

% activity(Name, Start, Finish)  -- DISTINCT from the Lab 12 instance.
activity(a1, 1,  3).
activity(a2, 2,  5).
activity(a3, 4,  7).
activity(a4, 1,  8).
activity(a5, 5,  9).
activity(a6, 8,  10).
activity(a7, 9,  11).
activity(a8, 11, 14).
activity(a9, 13, 16).

% Collect activities sorted by increasing finish time.
sorted_by_finish(Sorted) :-
    findall(F-act(N,S,F), activity(N,S,F), Pairs),
    keysort(Pairs, Keyed),
    strip_keys(Keyed, Sorted).

strip_keys([], []).
strip_keys([_-V|T], [V|T2]) :- strip_keys(T, T2).

% greedy(+SortedActivities, +LastFinish, -SelectedNames)
greedy([], _, []).
greedy([act(N,S,F)|Rest], LastF, [N|Sel]) :-
    S >= LastF, !,
    greedy(Rest, F, Sel).
greedy([act(_,_,_)|Rest], LastF, Sel) :-
    greedy(Rest, LastF, Sel).

% Portable replacement for forall/2
print_activities([]).
print_activities([act(N,S,F)|T]) :-
    format("  ~w  (start ~w, finish ~w)~n", [N,S,F]),
    print_activities(T).

main :-
    sorted_by_finish(Sorted),
    greedy(Sorted, -1, Selected),
    length(Selected, Count),
    format("Activities sorted by finish time:~n", []),
    print_activities(Sorted),
    format("~nGreedy selection: ~w~n", [Selected]),
    format("Number selected : ~w~n", [Count]).

:- initialization(main).