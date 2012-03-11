father(Father, Child) :- male(Father), parent(Father, Child).
mother(Mother, Child) :- female(Mother), parent(Mother, Child).
brother(Brother, Child) :- male(Brother), parent(Parent, Brother), parent(Parent, Child), Child \== Brother.
sister(Sister, Child) :- female(Sister), parent(Parent, Sister), parent(Parent, Child), Child \== Sister.
