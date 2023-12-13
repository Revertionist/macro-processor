PGM START 0
ABC MACRO &A,&B
LABEL$ STA &A
    STB &B
    MEND
BCD MACRO &C,&D
    STA &C
    STB &D
    MEND
    ABC P,Q
    ABC X,Y
    BCD R,S
    END