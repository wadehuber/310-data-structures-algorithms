% Graph Search: BFS and DFS  (CSC310 Module 7 - Graph Algorithms)
% ===============================================================
%
% Both traversals visit neighbors in alphabetical order and mark a vertex as
% visited when it is first enqueued/discovered (so each vertex is visited once).
%
% Run (SWI-Prolog):  swipl -g main -t halt graph_search.pl
% Run (SICStus):     sicstus -l graph_search.pl --goal "main."

% Undirected edges (each listed once).  DISTINCT from every CSC310 assignment.
% Graph Search: BFS and DFS  (CSC310 Module 7 - Graph Algorithms)
% ===============================================================
%
% Portable SWI-Prolog + SICStus Prolog version.
% Uses a different graph (p..u) to avoid overlapping with assignments.

% Undirected edges (each listed once)
edge(p, q).
edge(p, r).
edge(q, s).
edge(r, s).
edge(r, t).
edge(s, u).
edge(t, u).

adjacent(X, Y) :- edge(X, Y).
adjacent(X, Y) :- edge(Y, X).

neighbors(V, Ns) :-
    setof(Y, adjacent(V, Y), Ns), !.
neighbors(_, []).

% drop_visited(+Candidates, +Visited, -New)
drop_visited([], _, []).
drop_visited([X|Xs], Vis, New) :-
    ( member(X, Vis) -> New1 = New
    ; New = [X|New1]
    ),
    drop_visited(Xs, Vis, New1).

% ---- BFS (queue) ----
bfs(Start, Order) :- bfs_loop([Start], [Start], Order).

bfs_loop([], _, []).
bfs_loop([U|Queue], Visited, [U|Order]) :-
    neighbors(U, Ns),
    drop_visited(Ns, Visited, New),
    append(Queue, New, Queue1),
    append(Visited, New, Visited1),
    bfs_loop(Queue1, Visited1, Order).

% ---- DFS (recursion) ----
dfs(Start, Order) :-
    dfs_visit(Start, [], Rev),
    reverse_list(Rev, Order).

dfs_visit(U, Vin, Vout) :-
    \+ member(U, Vin), !,
    neighbors(U, Ns),
    dfs_list(Ns, [U|Vin], Vout).
dfs_visit(_, V, V).

dfs_list([], V, V).
dfs_list([N|Ns], Vin, Vout) :-
    dfs_visit(N, Vin, Vmid),
    dfs_list(Ns, Vmid, Vout).

% Portable reverse (no library dependency)
reverse_list(L, R) :- rev(L, [], R).
rev([], Acc, Acc).
rev([H|T], Acc, R) :- rev(T, [H|Acc], R).

% ---- Main ----
main :-
    bfs(p, B),
    dfs(p, D),
    write('Undirected graph on vertices p..u'), nl,
    write('BFS from p: '), write(B), nl,
    write('DFS from p: '), write(D), nl.

:- initialization(main).
