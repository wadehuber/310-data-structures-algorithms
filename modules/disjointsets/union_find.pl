% Disjoint-Set Forest (Union-Find)  (CSC310 Module 6A - Disjoint Sets)
% ===================================================================
%
% Forest representation as dynamic facts: parent/2 (each element's parent) and
% rank/2 (an upper bound on subtree height).  FIND-SET compresses the path by
% retracting and re-asserting parent facts; UNION links by rank.
%
% Run (SWI-Prolog):  swipl -g main -t halt union_find.pl
% Run (SICStus):     sicstus -l union_find.pl --goal "main."

:- dynamic parent/2, rank/2.

% Initialize all sets
init_dsu :-
    retractall(parent(_, _)),
    retractall(rank(_, _)),
    make_set(0),
    make_set(1),
    make_set(2),
    make_set(3),
    make_set(4),
    make_set(5),
    make_set(6).

make_set(X) :-
    assertz(parent(X, X)),
    assertz(rank(X, 0)).

% Find with path compression
find(X, Root) :-
    parent(X, Y),
    (X == Y ->
        Root = X
    ;
        find(Y, Root),
        retract(parent(X, _)),
        assertz(parent(X, Root))
    ).

% Union by rank
union(X, Y) :-
    find(X, RX),
    find(Y, RY),
    RX \== RY,
    rank(RX, RankX),
    rank(RY, RankY),
    (RankX > RankY ->
        retract(parent(RY, _)),
        assertz(parent(RY, RX))
    ; RankX < RankY ->
        retract(parent(RX, _)),
        assertz(parent(RX, RY))
    ;
        retract(parent(RY, _)),
        assertz(parent(RY, RX)),
        retract(rank(RX, _)),
        NewRank is RankX + 1,
        assertz(rank(RX, NewRank))
    ).

connected(X, Y) :-
    find(X, RX),
    find(Y, RY),
    RX == RY.

% Print sets
print_sets :-
    write('Sets: '),
    print_set(0),
    print_set(1),
    print_set(2),
    print_set(3),
    print_set(4),
    print_set(5),
    print_set(6),
    nl.

print_set(R) :-
    find(R, RR),
    (R == RR ->
        write('{'),
        print_members(R, 0, true),
        write('} ')
    ; true).

print_members(_, 7, _) :- !.
print_members(R, X, First) :-
    find(X, RX),
    (RX == R ->
        (First = true -> true ; write(', ')),
        write(X),
        NextFirst = false
    ;
        NextFirst = First
    ),
    X1 is X + 1,
    print_members(R, X1, NextFirst).

% Main predicate
main :-
    init_dsu,
    write('Disjoint-set forest (union by rank + path compression)'), nl,
    union(0,1),
    union(2,3),
    union(1,3),
    union(4,5),
    print_sets,
    (connected(0,3) -> write('connected(0,3)? true') ; write('connected(0,3)? false')), nl,
    (connected(0,4) -> write('connected(0,4)? true') ; write('connected(0,4)? false')), nl.

:- main.
