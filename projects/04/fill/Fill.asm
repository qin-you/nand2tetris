// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.




// 24576:KBD addr  16384-24575: 8K for screen   SCREEN:16384



    @24575
    D = A

    // R0: maxaddr, max addr of screen
    @0
    M = D

    // R1: sp (regard screen as a stack), current minimal available address of screen
    @SCREEN
    D = A
    @1
    M = D

(LOOP)
    @KBD
    D = M		// ASCII or 0 if no key pressed
    @FILL
    D;JGT

    @CLEAR
    0;JMP

(FILL)
    @0
    D = M
    @1
    D = D - M
    @LOOP
    D;JLT

    @1
    D = M
    A = M
    M = -1		// -1 : 1111111111111111

    @1
    M = D + 1

    @LOOP
    0;JMP
(CLEAR)
    @SCREEN
    D = A
    @1
    D = M - D
    @LOOP
    D;JLE

    @1
    D = M
    A = M - 1
    M = 0

    @1
    M = D - 1

    @LOOP
    0;JMP
