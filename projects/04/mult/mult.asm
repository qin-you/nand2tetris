// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)



// R2 = R0+R0+R0+..   number R1 of R0s add

@2
M = 0	// R2 = 0

@0
D = M
@END
D;JEQ		// if R0==0, need not calculate

(LOOP)		// let LOOP signs address of next line
@1
M = M - 1	// R1 -= 1
D = M
@END
D;JLT		// if R1 < 0: jmp  END.   unique exit of this loop

@0
D = M
@2
M = M + D	// R2 += R0

@LOOP
0;JMP		// loop


(END)
0;JMP