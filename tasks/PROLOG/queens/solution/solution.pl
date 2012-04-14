% http://www.csupomona.edu/~jrfisher/www/prolog_tutorial/2_11.html
queens(N, P) :-
    range(N, List),
    permutation(List, P),
    combine(List, P, S, D),
    all_diff(S),
    all_diff(D).


range(0, []).
range(Max, [Max | Tail]) :- Max =\= 0, Next is Max - 1, range(Next, Tail).

combine([X1|X],[Y1|Y],[S1|S],[D1|D]) :-
     S1 is X1 + Y1,
     D1 is X1 - Y1,
     combine(X,Y,S,D).
combine([],[],[],[]).

all_diff([X|Y]) :-  \+member(X,Y), all_diff(Y).
all_diff([_]).
