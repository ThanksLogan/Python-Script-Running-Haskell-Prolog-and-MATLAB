% Rule to reverse a list using recursion
reverse_list([], []).  % Base case
reverse_list([Head|Tail], Reversed) :-
    reverse_list(Tail, ReversedTail),
    append(ReversedTail, [Head], Reversed).

% Helper rule to print list elements without commas and brackets
write_list([]).
write_list([Head]) :-
    write(Head), !.  % No extra space after the last element
write_list([Head|Tail]) :-
    write(Head), write(' '), write_list(Tail).

% Main wrapper rule
main :-
    read(InputList),  % Read input list
    reverse_list(InputList, Reversed),  % Call reverse_list rule
    write_list(Reversed),  % Write output without commas and brackets
    nl.  % New line for better formatting
