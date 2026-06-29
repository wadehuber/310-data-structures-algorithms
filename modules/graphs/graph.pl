% Simple Graph Data Structure  (CSC310 Module 6B - Graphs)
% ========================================================
%
% Representation: dynamic facts.  vertex/1 stores vertices (in assertion order);
% adj/3 stores directed (From, To, Weight) edges.  An undirected edge is just two
% directed facts.
%
% Run (SWI-Prolog):  swipl -g main -t halt graph.pl
% Run (SICStus):     sicstus -l graph.pl --goal "main."

:- dynamic vertex/1.
:- dynamic adj/3.

% Clear previous state (important for repeated runs / initialization)
build_demo :-
    retractall(vertex(_)),
    retractall(adj(_,_,_)),
    % Arizona road network example
    add_vertex('PHX'), add_vertex('TUS'), add_vertex('MESA'), add_vertex('TEMPE'),
    add_edge('PHX',  'MESA',  20,  false),
    add_edge('PHX',  'TEMPE', 11,  false),
    add_edge('MESA', 'TEMPE', 8,   false),
    add_edge('PHX',  'TUS',   116, false),
    add_edge('TUS',  'MESA',  100, false).

add_vertex(V) :-
    (vertex(V) -> true ; assertz(vertex(V))).

add_edge(U, V, W, Directed) :-
    add_vertex(U),
    add_vertex(V),
    assertz(adj(U, V, W)),
    (Directed == false -> assertz(adj(V, U, W)) ; true).

neighbors(V, Sorted) :-
    findall(N-W, adj(V, N, W), Pairs),
    sort(Pairs, Sorted).

edge_weight(U, V, W) :-
    adj(U, V, W).

print_neighbors([]).
print_neighbors([N-W]) :- !,
    write(N), write('('), write(W), write(')').
print_neighbors([N-W|T]) :-
    write(N), write('('), write(W), write('), '),
    print_neighbors(T).

print_graph :-
    write('Graph (undirected, weighted) - adjacency list:'), nl,
    print_vertices.

print_vertices :-
    findall(V, vertex(V), Vertices),
    print_vertex_list(Vertices).

print_vertex_list([]).
print_vertex_list([V|Vs]) :-
    neighbors(V, Ns),
    write('  '), write(V), write(' -> '),
    print_neighbors(Ns),
    nl,
    print_vertex_list(Vs).

names([]).
names([N-_]) :- !, write(N).
names([N-_|T]) :-
    write(N), write(', '),
    names(T).

main :-
    build_demo,
    print_graph,
    neighbors('PHX', PhxN),
    write('Neighbors of PHX: '), names(PhxN), nl,
    edge_weight('PHX', 'MESA', W),
    write('Weight PHX-MESA: '), write(W), nl.

:- initialization(main).
