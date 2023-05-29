opcodes=[]
commands=[]
types=[]
memory=[] # nested list where each element is a instruction
A = {'00000':'add','00001':'sub','00110':'mul','01010':'xor','01011':'or','01100':'and'}
B = {'00010':'mov','01000':'rs','01001':'ls'} #move immediate
C = {'00011':'mov','00111':'div','01101':'not','01110':'cmp'}  #move register
D = {'00100':'ld','00101':'st'}
E = {'01111':'jmp','11100':'jlt','11101':'jgt','11111':'je'}
F = {'11010':'hlt'}
R0 = R1 = R2 = R3 = R4 = R5 = R6 = FLAGS = "0000000000000000" #16 bit value for each register
reg_list = {'000':R0,'001':R1,'010':R2,'011':R3,'100':R4,'101':R5,'110':R6,'111':FLAGS} #adress gives register


def initialize():
    fobj=open("stdout.txt","r")
    content=fobj.readlines()
    
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

initialize()

def fix_len(s1):
    if len(s1)>16:
        x = len(s1) - 16
        s1 = s1[x:]
        return s1
    while len(s1)<16:
        s1 = '0' + s1
    return s1
def set_flags(x):
    if x == "V":
        reg_list["111"] = "0000000000001000"
    if x == "L":
        reg_list["111"] = "0000000000000100"
    if x == "G":
        reg_list["111"] = "0000000000000010"
    if x == "E":
        reg_list["111"] = "0000000000000001"

#---------------------------------------------------
def addition(reg1,reg2,reg3):
    x=int(reg_list[reg2],2)
    if int(reg_list[reg2],2)+int(reg_list[reg3],2) <= 65535:
        reg_list[reg1] = fix_len(str(bin(int(reg_list[reg2],2)+int(reg_list[reg3],2))[2:]))
    else:
        set_flags("V")
        reg_list[reg1]="0000000000000000"
def subtraction(reg1,reg2,reg3):
    if int(reg_list[reg2],2)-int(reg_list[reg3],2) >= 0:
        reg_list[reg1] = fix_len(str(bin(int(reg_list[reg2],2)-int(reg_list[reg3],2))[2:]))
    else:
        set_flags("V")
        reg_list[reg1]="0000000000000000"
def multiplication(reg1,reg2,reg3):
    if int(reg_list[reg2],2)*int(reg_list[reg3],2) <= 65535:
        reg_list[reg1] = fix_len(str(bin(int(reg_list[reg2],2)*int(reg_list[reg3],2))[2:]))
    else:
        set_flags("V")
        reg_list[reg1]="0000000000000000"
def XOR(reg1,reg2,reg3):
    reg_list[reg1] = binary_xor(reg_list[reg2],reg_list[reg3])
def binary_xor(a, b):
    result=[]
    for i in range(16):
        bit_a = int(a[i])
        bit_b = int(b[i])
        xor_result = bit_a ^ bit_b
        result.append(str(xor_result))
    return ''.join(result)
def OR(reg1,reg2,reg3):
    reg_list[reg1] = binary_or(reg_list[reg2],reg_list[reg3])
def binary_or(a, b):
    result=[]
    for i in range(16):
        bit_a = int(a[i])
        bit_b = int(b[i])
        xor_result = bit_a | bit_b
        result.append(str(xor_result))
    return ''.join(result)
def AND(reg1,reg2,reg3):
    reg_list[reg1] = binary_and(reg_list[reg2],reg_list[reg3])
def binary_and(a, b):
    result=[]
    for i in range(16):
        bit_a = int(a[i])
        bit_b = int(b[i])
        xor_result = bit_a & bit_b
        result.append(str(xor_result))
    return ''.join(result)
#-------------------------------------------------

def binary_to_integer(num):
    return int(num,2)
def int_to_bin(num):
    bin2=bin(int(num))
    k=str(bin2)
    k=k[2:]
    return k
def moveri(reg1,imm):
    reg_list[reg1] = fix_len(imm)

#----------------------------------------
def moverr(reg1,reg2):
    reg_list[reg1] = reg_list[reg2]
def div(reg1,reg2):
    q,r = divmod(int(reg_list[reg1],2),int(reg_list[reg2],2))
    if reg_list[reg2] != 0:
        reg_list["000"] = fix_len(str(bin(q)[2:]))
        reg_list["001"] = fix_len(str(bin(r)[2:]))
    else:
        set_flags("V")
        reg_list["000"]="0000000000000000"
        reg_list["001"]="0000000000000000"
def invert(reg1,reg2):
    reg_list[reg1] = fix_len(str(1111111111111111 - int(reg_list[reg2])))
def compare(reg1,reg2):
    if int(reg_list[reg1]) < int(reg_list[reg2]):
        set_flags("L")
    if int(reg_list[reg1]) > int(reg_list[reg2]):
        set_flags("G")
    if int(reg_list[reg1]) == int(reg_list[reg2]):
        set_flags("E")
#------------------------------------------------------------Z
def ls(reg,imm):
    dec_value = binary_to_integer(reg_list[reg])
    imm = binary_to_integer(imm)
    shifted_value = dec_value*(2**imm)
    bin_value = int_to_bin(shifted_value)
    r = fix_len(str(bin_value))
    reg_list[reg] = r
def rs(reg,imm):
    dec_value = binary_to_integer(reg_list[reg])
    imm = binary_to_integer(imm)
    shifted_value = dec_value//(2**imm)
    bin_value = int_to_bin(shifted_value)
    r = fix_len(str(bin_value))
    reg_list[reg] = r
print([i for i in reg_list.values()])
print([int(i,2) for i in reg_list.values()])

running_function(0)

def running_function(i):
    for i in range(len(types)):
        if types[i] == "A":
            if commands[i] == "add":
                addition(memory[i][0],memory[i][1],memory[i][2])
            if commands[i] == "sub":
                subtraction(memory[i][0],memory[i][1],memory[i][2])
            if commands[i] == "mul":
                multiplication(memory[i][0],memory[i][1],memory[i][2])
            if commands[i] == "xor":
                XOR(memory[i][0],memory[i][1],memory[i][2])
            if commands[i] == "or":
                OR(memory[i][0],memory[i][1],memory[i][2])
            if commands[i] == "and":
                AND(memory[i][0],memory[i][1],memory[i][2])
        if types[i] == "B":
            if commands[i] == "mov":
                moveri(memory[i][0],memory[i][1])
            if commands[i] == "rs":
                rs(memory[i][0],memory[i][1])
            if commands[i] == "ls":
                ls(memory[i][0],memory[i][1])
        if types[i] == "C":
            if commands[i] == "mov":
                moverr(memory[i][0],memory[i][1])
            if commands[i] == "div":
                div(memory[i][0],memory[i][1])
            if commands[i] == "cmp":
                compare(memory[i][0],memory[i][1])
            if commands[i] == "not":
                invert(memory[i][0],memory[i][1])
        if types[i] == "D":
            continue
        if types[i] == "E":
            if commands[i]=="jmp":
                running_function(binary_to_integer(memory[i][0]))
            if commands[i]=="jgt":
                if reg_list["111"] = "0000000000000010":
                    running_function(binary_to_integer(memory[i][0]))
            if commands[i]=="jlt":
                if reg_list["111"] = "0000000000000100":
                    running_function(binary_to_integer(memory[i][0]))
            continue
        if types[i] == "F":
            break
print([i for i in reg_list.values()])
print([int(i,2) for i in reg_list.values()])
