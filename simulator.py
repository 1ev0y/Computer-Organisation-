fobj=open("Executable.txt","r")
content=fobj.readlines()
opcodes=[]
commands=[]
types=[]
memory=[]
A = {'00000':'add','00001':'sub','00110':'mul','01010':'xor','01011':'or','01100':'and'}
C= {'00111':'div','01101':'not','01110':'cmp'}
B = {'00010':'mov','01000':'rs','01001':'ls'}
D = {'00100':'ld','00101':'st'}
E = {'01111':'jmp','11100':'jlt','11101':'jgt','11111':'je'}
F={'11010':'hlt'}
reg_list = {'000':'R0','001':'R1','010':'R2','011':'R3','100':'R4','101':'R5','110':'R6','111':'FLAGS'}


for i in content:
    opcode=i[:5]
    opcodes.append(opcode)
    for j in A:
        if opcode==j:
            types.append("A")
            commands.append(A[j])
    for j in B:
        if opcode==j:
            types.append("B")
            commands.append(B[j])
    for j in C:
        if opcode==j:
            types.append("C")
            commands.append(C[j])
    for j in D:
        if opcode==j:
            types.append("D")
            commands.append(D[j])
    for j in E:
        if opcode==j:
            types.append("E")
            commands.append(E[j])
    for j in F:
        if opcode==j:
            types.append("F")
            commands.append(F[j])
    
print(opcodes)
print(types)
print(commands)
print(memory)
