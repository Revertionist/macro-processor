PGM START 0
ABC MACRO &A,&B
    STA &A
    STB &B
    MEND
BCD MACRO &C,&D
    STA &C
    STB &D
    MEND
    ABC P,Q
    BCD R,S
    END