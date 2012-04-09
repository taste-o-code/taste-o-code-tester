bound(X) :- member(X, [1, 2, 3, 4]).
all_bounded([]).
all_bounded([Head | Tail]) :- bound(Head), all_bounded(Tail).
distinct(A, B, C, D) :- A \== B, A \== C, A \== D, B \== C, B \== D, C \== D.

sudoku(Puzzle, Solution) :-
    Puzzle = Solution,
    Puzzle = [[A1, A2, A3, A4],
              [B1, B2, B3, B4],
              [C1, C2, C3, C4],
              [D1, D2, D3, D4]],
    all_bounded([A1, A2, A3, A4]),
    distinct(A1, A2, A3, A4),
    all_bounded([B1, B2, B3, B4]),
    distinct(B1, B2, B3, B4),
    distinct(A1, A2, B1, B2),
    distinct(A3, A4, B3, B4),
    all_bounded([C1, C2, C3, C4]),
    distinct(C1, C2, C3, C4),
    all_bounded([D1, D2, D3, D4]),
    distinct(D1, D2, D3, D4),
    distinct(C1, C2, D1, D2),
    distinct(C3, C4, D3, D4),
    distinct(A1, B1, C1, D1),
    distinct(A2, B2, C2, D2),
    distinct(A3, B3, C3, D3),
    distinct(A4, B4, C4, D4).
