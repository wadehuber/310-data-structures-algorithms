% demo.pl
%
% Driver for leftist_heap.pl -- the Prolog counterpart of HeapExample and
% PQTester.  Run with:
%
%     swipl -q -g main -t halt demo.pl

:- use_module(leftist_heap).

main :-
    % --- heap sort of integers (cf. removeMin on the int heap) ---------
    Nums = [49, 20, 25, 14, 33, 32, 49, 12, 50, 2, 62, 10],
    heap_sort(Nums, Sorted),
    format("heap_sort ~w~n  -> ~w~n~n", [Nums, Sorted]),

    % --- find_min / delete_min step by step ----------------------------
    heap_from_list(Nums, H),
    find_min(H, Min),
    delete_min(H, Min, H1),
    find_min(H1, Min2),
    format("find_min      = ~w~n", [Min]),
    format("after delete, find_min = ~w~n~n", [Min2]),

    % --- priority queue (the PQTester data set) -------------------------
    Pairs = [ "first"-1,
              "bbb"-200,
              "third"-50,
              "fifth"-92,
              "second"-10,
              "fourth"-55,
              "aaa"-200,
              "this one should be first"-0 ],
    pq_drain(Pairs, Order),
    format("priority queue order:~n", []),
    forall(member(E, Order), format("  ~w~n", [E])).
