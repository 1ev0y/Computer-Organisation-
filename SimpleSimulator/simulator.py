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
    if opcode in A:
        l=[i[7:10],i[10:13],i[13:16]]
        types.append("A")
        commands.append(A[opcode])
        memory.append(l)
    if opcode in B:
        l=[i[6:9],i[9:16]]
        types.append("B")
        commands.append(B[opcode])
        memory.append(l)
    if opcode in C:
        l=[i[10:13],i[13:16]]
        types.append("C")
        commands.append(C[opcode])
        memory.append(l)
    if opcode in D:
        l=[[i[6:9],i[9:16]]]
        types.append("D")
        commands.append(D[opcode])
        memory.append(l)
    if opcode in E:
        l=[i[9:16]]
        types.append("E")
        commands.append(E[opcode])
        memory.append(l)
    if opcode in F:
        types.append("F")
        commands.append(F[opcode])
        memory.append("end")
    
print(opcodes)
print(types)
print(commands)
print(memory)
