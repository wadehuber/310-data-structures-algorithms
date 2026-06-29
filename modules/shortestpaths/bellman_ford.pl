% Bellman-Ford Single-Source Shortest Paths  (CSC310 Module 10)
% =============================================================
%
% Bellman-Ford relaxes every edge |V|-1 times; this handles negative edges and a
% final pass detects a negative-weight cycle.  Distances are carried in a list of
% V-D pairs (Prolog has no mutable arrays), rebuilt each relaxation.
% Expected: s=0, t=2, x=4, y=7, z=-2; no negative cycle.
%
% Run (SWI-Prolog):  swipl -g main -t halt bellman_ford.pl
% Run (SICStus):     sicstus -l bellman_ford.pl --goal "main."

inf(1000000000).   % large sentinel for +infinity (weights are small)

% Directed weighted edges, CLRS Fig. 24.4.
edge(s, t, 6).
edge(s, y, 7).
edge(t, x, 5).
edge(t, y, 8).
edge(t, z, -4).
edge(x, t, -2).
edge(y, x, -3).
edge(y, z, 9).
edge(z, x, 7).
edge(z, s, 2).

vertices([s, t, x, y, z]).

get_dist(V, Dist, D) :- member(V-D, Dist).

set_dist(V, D, [V-_|T], [V-D|T]) :- !.
set_dist(V, D, [P|T], [P|T2]) :- set_dist(V, D, T, T2).

init_dist(_, [], []).
init_dist(Source, [V|Vs], [V-D|Rest]) :-
    (V == Source -> D = 0 ; inf(D)),
    init_dist(Source, Vs, Rest).

relax_edge(edge(U,V,W), Din, Dout) :-
    get_dist(U, Din, Du),
    get_dist(V, Din, Dv),
    (Du + W < Dv
    -> NewDv is Du + W, set_dist(V, NewDv, Din, Dout)
    ;  Dout = Din).

relax_all([], D, D).
relax_all([E|Es], Din, Dout) :-
    relax_edge(E, Din, Dmid),
    relax_all(Es, Dmid, Dout).

passes(0, _, D, D) :- !.
passes(N, Edges, Din, Dout) :-
    N > 0,
    relax_all(Edges, Din, Dmid),
    N1 is N - 1,
    passes(N1, Edges, Dmid, Dout).

has_neg_cycle(Edges, Dist) :-
    member(edge(U,V,W), Edges),
    get_dist(U, Dist, Du),
    get_dist(V, Dist, Dv),
    Du + W < Dv.

main :-
    findall(edge(U,V,W), edge(U,V,W), Edges),
    vertices(Vs),
    length(Vs, N),
    N1 is N - 1,
    init_dist(s, Vs, D0),
    passes(N1, Edges, D0, Dist),
    write('Bellman-Ford from source s (CLRS Fig. 24.4):'), nl,
    print_dists(Dist),
    (has_neg_cycle(Edges, Dist)
    -> write('Negative-weight cycle detected.'), nl
    ;  write('No negative-weight cycle reachable from s.'), nl).

print_dists([]).
print_dists([V-D|T]) :-
    write('  '), write(V), write(': '), write(D), nl,
    print_dists(T).

:- initialization(main).
