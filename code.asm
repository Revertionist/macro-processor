PGM START 0
ABC MACRO &A,&B
    STA &A
    STB &B
    MEND
BCD MACRO &C,&D
    STA &C
    STA &B
    MEND
    ABC P,Q
    ABC R,S
    END