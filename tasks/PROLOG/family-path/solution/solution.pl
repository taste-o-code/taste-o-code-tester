path(Parent, Child, [Parent, Child]) :- parent(Parent, Child).
path(Parent, Child, [Parent | Rest]) :- parent(Parent, Inter), path(Inter, Child, Rest).
