gcd(X, 0, X).
gcd(X, Y, Res) :- Y =\= 0, M is X mod Y, gcd(Y, M, Res).
