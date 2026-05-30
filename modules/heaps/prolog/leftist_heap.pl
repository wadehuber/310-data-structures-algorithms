% leftist_heap.pl
%
% A heap implementation in Prolog.
%
% The Java/Python/C++ versions in this repo use a *mutable linked tree*
% whose nodes are rewired in place.  Prolog has no mutable state, so the
% idiomatic equivalent is a *persistent* (immutable) heap built by
% merging.  This is a leftist min-heap: every operation is expressed in
% terms of merge/3, which is the natural way to do a functional heap.
%
% Representation of a heap:
%     nil                              the empty heap
%     node(Rank, Element, Left, Right) a node holding Element
%
% "Leftist" means the right spine is always the shortest path to a nil,
% which keeps merge logarithmic.  Rank = length of that right spine.
%
% Elements are compared with @=</2 (standard order of terms), so the heap
% works for numbers, atoms, strings, and compound keys alike.

:- module(leftist_heap,
          [ empty_heap/1,
            is_empty/1,
            insert/3,
            find_min/2,
            delete_min/3,
            heap_from_list/2,
            heap_sort/2,
            pq_drain/2 ]).

% empty_heap(-H): H is the empty heap.
empty_heap(nil).

% is_empty(+H): true when H is the empty heap.
is_empty(nil).

% rank(+H, -R): R is the rank (right-spine length) of H.
rank(nil, 0).
rank(node(R, _, _, _), R).

% make_node(+X, +A, +B, -Node): build a node holding X with children A
% and B, putting the higher-rank child on the left (the leftist property)
% and giving the node rank = 1 + rank of the (shorter) right child.
make_node(X, A, B, Node) :-
    rank(A, RA),
    rank(B, RB),
    ( RA >= RB
    ->  R is RB + 1, Node = node(R, X, A, B)
    ;   R is RA + 1, Node = node(R, X, B, A)
    ).

% merge(+H1, +H2, -H): H is the heap containing every element of H1 and
% H2.  This is the workhorse -- insert and delete_min both defer to it.
merge(nil, H, H) :- !.
merge(H, nil, H) :- !.
merge(H1, H2, H) :-
    H1 = node(_, X, L1, R1),
    H2 = node(_, Y, _,  _),
    X @=< Y, !,                       % X is the smaller root: keep it on top
    merge(R1, H2, Merged),            % recurse down the right spine
    make_node(X, L1, Merged, H).
merge(H1, H2, H) :-
    H2 = node(_, Y, L2, R2),          % otherwise Y is smaller: keep Y on top
    merge(H1, R2, Merged),
    make_node(Y, L2, Merged, H).

% insert(+X, +H0, -H): H is H0 with X added.
insert(X, H0, H) :-
    merge(node(1, X, nil, nil), H0, H).

% find_min(+H, -Min): Min is the smallest element (the root).
find_min(node(_, X, _, _), X).

% delete_min(+H0, -Min, -H): Min is the smallest element of H0 and H is
% H0 with that element removed.
delete_min(node(_, X, L, R), X, H) :-
    merge(L, R, H).

% heap_from_list(+List, -H): fold a list of elements into a heap.
heap_from_list(List, H) :-
    foldl(insert, List, nil, H).

% heap_sort(+List, -Sorted): build a heap, then repeatedly remove the
% minimum -- the elements come out in ascending order.
heap_sort(List, Sorted) :-
    heap_from_list(List, H),
    drain(H, Sorted).

% drain(+H, -Elements): pull every element out of H in sorted order.
drain(nil, []).
drain(H, [Min | Rest]) :-
    H \= nil,
    delete_min(H, Min, H1),
    drain(H1, Rest).

% --- Priority-queue layer ------------------------------------------------
%
% Mirrors priorityqueue/PriorityQueue.java: each item carries an integer
% priority, and ties are broken first-come-first-served.  We encode each
% queue entry as the compound key  (Priority - Arrival) - Element.  Under
% standard order of terms @=< compares Priority first, then Arrival, so a
% lower priority number leaves first and equal priorities leave in arrival
% order -- exactly the Java PrioritizedObject.compareTo behaviour.

% pq_drain(+Pairs, -Order): Pairs is a list of  Element-Priority  terms;
% Order is the elements removed in priority (then arrival) order.
pq_drain(Pairs, Order) :-
    tag_arrival(Pairs, 0, Entries),     % attach an arrival index to each
    heap_from_list(Entries, H),
    drain(H, Drained),
    strip_keys(Drained, Order).

tag_arrival([], _, []).
tag_arrival([Element-Priority | T], N, [ (Priority-N)-Element | T2 ]) :-
    N1 is N + 1,
    tag_arrival(T, N1, T2).

strip_keys([], []).
strip_keys([ _-Element | T ], [Element | T2]) :-
    strip_keys(T, T2).
