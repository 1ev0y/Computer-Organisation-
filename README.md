# Computer-Organisation-

This is the project done by Group No. A25. It includes a fully functional assembler and a simulator that work for floating point numbers as well. We also have implemented 5 bonus functions, the opcodes/functionalities of which are mentioned below:-

1)  Instruction :- swap  
    Opcode      :- 10011  
    Syntax      :- swap reg1 reg2  
    Type        :- C  
    Semantics   :- Swaps values of reg1 and reg2  

2)  Instruction :- ceil  
    Opcode      :- 10101  
    Syntax      :- ceil reg1 reg2  
    Type        :- C  
    Semantics   :- Takes the value of reg2 and computes its ceil into reg1  

3)  Instruction :- floor  
    Opcode      :- 10110  
    Syntax      :- floor reg1 reg2  
    Type        :- C  
    Semantics   :- Takes the value of reg2 and computes its floor into reg1  

4)  Instruction :- rot  
    Opcode      :- 10100  
    Syntax      :- rot reg1 $Imm  
    Type        :- B  
    Semantics   :- Takes the value in reg1 and rotates it rightwards  

5)  Instruction :- rand  
    Opcode      :- 10111  
    Syntax      :- rand reg1 reg2 reg3  
    Type        :- A  
    Semantics   :- Finds a random integer between reg2 and reg3(both included) and places it in reg1

Some Notes for the TAs for Assembler:-

1) The code returns special error messages for a couple of errors that we thought might be there in the test cases apart from those given in the project document file. Any other error is called a 'General Syntax Error.'

2) We assumed that we had to print ony one error and not all the errors that are possible as it was explicitly mentioned to do so in the project documents.

Notes for Simulator:-

1) We assumed that the floats occupied a continuous range rather than a discrete one.

2) We assumed overflow to be when value goes above 16 bits and not 7 bits.
