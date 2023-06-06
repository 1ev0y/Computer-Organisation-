import sys
#----------------------------------------------- Floating point
import random
memorydump=[]
def dump_pc(pc):
    counter=fix_len_part2(bin(pc),7)
    counter_out=""
    for k in range(len(counter)):
        if counter[k]=="b":
            counter_out+="0"
        else:
            counter_out+=counter[k]
    if len(counter_out)==8:
        counter_out=counter_out[1:8]
    if len(counter_out)==9:
        counter_out=counter_out[2:9]
    
    print(counter_out,end="        ")
def dump_rf():    
    for i in reg_list.values():
        print(fix_len_part2(i,16),end=" ")
    print()
    

def fix_len_part1(s1):
    s1 = str(s1)
    if len(s1)==7:
        return s1
    
    while len(s1)!=7:
        s1 = '0' + s1

    return s1

def fix_len_part2(s1,n):
    s1 = str(s1)

    if len(s1)>=n+1:
        return s1
    
    if len(s1)==n:
        return s1
    
    while len(s1)!=n:
        s1 = '0' + s1

    return s1
def convert_decimalpt_to_bin(number, precision):
    str1 = ''
    count = 0
    while 1:
        count += 1
        number = round(number*2,8)
        if number > 1:
            str1 = str1 + '1'
            number-=1
        elif number < 1:
            str1 = str1 + '0'
        else:
            str1 = str1 + '1'
            return str1

        if count==precision:
            return str1

def convert_float_to_binary(n):
    n0 = float(n)
    n1 = str(n0)
    n2 = ''
    count = 0
    while(1):
        if n1[count]!='.':
            n2 = n2 + n1[count]
        else:
            break
        count+=1

    n2 = int(n2)
    n3 = round(n0-n2,8)

    n4 = bin(n2)[2:]
    main_str = n4 + '.' + convert_decimalpt_to_bin(n3,10)

    for i in range(len(main_str)):
        if main_str[i] == '1':
            n5 = i
            break

    for i in range(len(main_str)): 
        if main_str[i] == '.':
            n6 = i
            break
    if n6 == n5 + 1:
        str2 = ''
        str2 = str2 + main_str[n5] + '.'
        count4 = 0
        for i in range(n6+1,len(main_str)):
            str2 = str2 + main_str[i]
            count4+=1
            exponent = 3
            if(count4==5):
                break

        while count4 != 5 and count4 <=5:
            str2 = str2 + '0'
            count4+=1

        s3 = bin(exponent)[2:]
        s3 = fix_len_part2(s3,3)

        l1 = []
        l1.append(s3)
        l1.append(str2[2:])
        return l1

    else:
        str2 = ''
        if n6 < n5:
            exponent = n6-n5
            str2 = str2 + main_str[n5] + '.'
            count2 = 0
            for i in range(n5+1,len(main_str)):
                str2 = str2 + main_str[i]
                count2+=1
                if(count2==5):
                    break

            while count2 != 5 and count2 <=5:
                str2 = str2 + '0'
                count2+=1

            exponent+=3
            s3 = bin(exponent)[2:]
            s3 = fix_len_part2(s3,3)

            l1 = []
            l1.append(s3)
            l1.append(str2[2:])
            return l1
        
        elif n5 < n6:
            exponent = n6-n5-1
            str2 = str2 + main_str[n5] + '.'
            count3 = 0
            for i in range(n5+1,n6):
                str2 = str2 + main_str[i]
                count3+=1
                if count3 == 5:
                    break

            for i in range(n6+1,len(main_str)):
                if(count3==5):
                    break
                str2 = str2 + main_str[i]
                count3+=1

            while count3 != 5 and count3 <=5:
                str2 = str2 + '0'
                count3+=1

            exponent+=3
            s3 = bin(exponent)[2:]
            s3 = fix_len_part2(s3,3)

            l1 = []
            l1.append(s3)
            l1.append(str2[2:])
            return l1

def convert_float(s1):
    num = float(s1)
    num = (str(num))[2:]
    count = -1
    sum = 0

    for i in num:
        sum += int(i)*(2**count)
        count -= 1

    return str(sum)

def convert_binary_to_float(l):
    integer=l[0]
    decimal=l[1]
    i=0
    d=0
    for l in range(len(integer)):
        i+=(int(integer[l]))*2**(len(integer)-l-1)
    
    for l in range(len(decimal)):
        d+=(int(decimal[l]))*2**(-(l+1))

    ir=2**(i-3)*(1+d)
    
    return ir

'''

dict1 = {}

def make_float_list(dict1):
    s1 = '1.'
    for a in ['0','1']:
        for b in ['0','1']:
            for c in ['0','1']:
                for d in ['0','1']:
                    for e in ['0','1']:
                        s2 = s1 + a + b + c + d + e
                        s3 = convert_float(s2)
                        s3 = float(s3)
                        s3 = s3 + 1
                        s3 = round(s3,5)
                        for f in range(-3,5):
                            i1 = s3 * (2**f)
                            i1 = round(i1,8)

                            l2  = []
                            l2.append(s2[2:])
                            f = bin(f+3)[2:]
                            l2.append(fix_len_part2(f,3))
                            i1 = str(i1)
                            dict1[i1] = l2

make_float_list(dict1)
'''

#-------------------------------------------------------------------
opcodes=[]
commands=[]
types=[]
memory=[] # nested list where each element is a instruction
A = {'00000':'add','00001':'sub','00110':'mul','01010':'xor','01011':'or','01100':'and','10000':'addf','10001':'subf','10111':'random'}
B = {'00010':'mov','01000':'rs','01001':'ls','10100':'rotate'} #move immediate
C = {'00011':'mov','00111':'div','01101':'not','01110':'cmp','10011':'swap','10110':'floor','10101':'ceil'}  #move register
D = {'00100':'ld','00101':'st',}
E = {'01111':'jmp','11100':'jlt','11101':'jgt','11111':'je'}
F = {'11010':'hlt'}
memaddrvalues={}
Floating={'10010':'mov'}
R0 = R1 = R2 = R3 = R4 = R5 = R6 = FLAGS = "0000000000000000" #16 bit value for each register
reg_list = {'000':R0,'001':R1,'010':R2,'011':R3,'100':R4,'101':R5,'110':R6,'111':FLAGS} #adress gives register


def initialize():
    
    content=sys.stdin.readlines()
    j=0
    for i in content:
        memorydump.append(i[0:16])
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
            l=[i[6:9],i[9:16]]
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
            l=bin(j)
            k=""
            for i in l:
                if i=="b":
                    k+="0"
                else:
                    k+=i
            k=fix_len_part2(k,7)
            memory.append(k)
             
        if opcode in Floating:
            l=[i[5:8],i[8:16]]
            types.append("Floating")
            commands.append(Floating[opcode])
            memory.append(l)
        j+=1
            

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
    if int(reg_list[reg2],2)+int(reg_list[reg3],2) <= 127:
        reg_list[reg1] = fix_len(str(bin(int(reg_list[reg2],2)+int(reg_list[reg3],2))[2:]))
    else:
        set_flags("V")
        reg_list[reg1]="0000000000000000"
def rand(reg1,reg2,reg3):
    # reg_list[reg1]=fix_len(str(bin(random.randint(int(reg_list[reg2]),int(reg_list[reg3])))[2:]))
    ll = int(reg_list[reg2],2)
    ul = int(reg_list[reg3],2)
    num = random.randint(ll,ul)
    binf = str(bin(num))
    binf = binf[2:]
    reg_list[reg1] = binf

def subtraction(reg1,reg2,reg3):
    if int(reg_list[reg2],2)-int(reg_list[reg3],2) >= 0:
        reg_list[reg1] = fix_len(str(bin(int(reg_list[reg2],2)-int(reg_list[reg3],2))[2:]))
    else:
        set_flags("V")
        reg_list[reg1]="0000000000000000"
def multiplication(reg1,reg2,reg3):
    if int(reg_list[reg2],2)*int(reg_list[reg3],2) <= 127:
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
# print([i for i in reg_list.values()])
# print([int(i,2) for i in reg_list.values()])

#-------------------------------------------------------------------
def movf(reg,immediateval):
    reg_list[reg]=convert_float_to_binary(immediateval)[0]+convert_float_to_binary(immediateval)[1]
    

def addf(reg1,reg2,reg3):
    x=round(convert_binary_to_float(reg_list[reg2])+convert_binary_to_float(reg_list[reg3]),9)
    
    if x>31.5:
        set_flags("V")
        reg_list[reg1]="0000000000000000"
    else:
        reg_list[reg1]=convert_float_to_binary(x)[0]+convert_float_to_binary(x)[1]
    
def subf(reg1,reg2,reg3):
    x=round(convert_binary_to_float(reg_list[reg2])-convert_binary_to_float(reg_list[reg3]),8)
    if x<0:
        set_flags("V")
        reg_list[reg1]="0000000000000000"
    else:
        reg_list[reg1]=convert_float_to_binary(x)[0]+convert_float_to_binary(x)[1]

def swap(r1,r2):
    dummy = reg_list[r2]
    reg_list[r2] = reg_list[r1]
    reg_list[r1] = dummy

def floor(r1,r2):
    reg_list[r1] = int_to_bin(int(binary_to_integer(reg_list[r2])))

def ceil (r1,r2):
    reg_list[r1] = int_to_bin(int(binary_to_integer(reg_list[r2]))+1)

def rotate(reg_value , n):
    copy = reg_list[reg_value]
    if n == 0:
        return 
    elif n > 0:
        for i in range(n,len(copy)):
            reg_list[reg_value][i] = copy[i-n]
        for i in range(n):
            reg_list[reg_value][i] = copy[i+(len(copy) - n)]


#--------------------------------------------------------------------------------------
pc=0
cond=False
halted= False
while(halted==False):
    
    if types[pc] == "A":
        setflag=False
        fl=False
        for m in memory[pc]:
            if m=="111":
                fl=True
        if fl==False:
            reg_list["111"]='0000000000000000'


        if commands[pc]=="random":
            rand(memory[pc][0],memory[pc][1],memory[pc][2])
        if commands[pc] == "addf":
            addf(memory[pc][0],memory[pc][1],memory[pc][2])
            if reg_list['111']!='0000000000000000':
                fl=True
                setflag=True
        if commands[pc] == "add":
            addition(memory[pc][0],memory[pc][1],memory[pc][2])
            if reg_list['111']!='0000000000000000':
                fl=True
                setflag=True
        if commands[pc] == "sub":
            subtraction(memory[pc][0],memory[pc][1],memory[pc][2])
            if reg_list['111']!='0000000000000000':
                fl=True
                setflag=True
        if commands[pc] == "subf":
            subf(memory[pc][0],memory[pc][1],memory[pc][2])
            if reg_list['111']!='0000000000000000':
                fl=True
                setflag=True
        if commands[pc] == "mul":
            multiplication(memory[pc][0],memory[pc][1],memory[pc][2])
            if reg_list['111']!='0000000000000000':
                fl=True
                setflag=True
        if commands[pc] == "xor":
            XOR(memory[pc][0],memory[pc][1],memory[pc][2])
        if commands[pc] == "or":
            OR(memory[pc][0],memory[pc][1],memory[pc][2])
        if commands[pc] == "and":
            AND(memory[pc][0],memory[pc][1],memory[pc][2])
        if setflag==False:
            fl=False
        
        if types[pc+1]!="E":
            for m in memory[pc+1]:
                if m=="111":
                    fl=True
            if fl==False:
                reg_list["111"]='0000000000000000'

    if types[pc] == "B":
        fl=False
        for m in memory[pc]:
            if m=="111":
                fl=True
        if fl==False:
            reg_list["111"]='0000000000000000'
        if commands[pc] == "mov":
            moveri(memory[pc][0],memory[pc][1])
        if commands[pc] == "rs":
            rs(memory[pc][0],memory[pc][1])
        if commands[pc] == "ls":
            ls(memory[pc][0],memory[pc][1])
        if commands[pc]=="rotate":
            rotate(memory[pc][0],memory[pc][1])
        fl=False
        
        if types[pc+1]!="E":
            for m in memory[pc+1]:
                if m=="111":
                    fl=True
            if fl==False:
                reg_list["111"]='0000000000000000'
    if types[pc] == "C":
        setflag=False
        fl=False
        for m in memory[pc]:
            if m=="111":
                fl=True
        if fl==False:
            reg_list["111"]='0000000000000000'
        if commands[pc] == "mov":
            moverr(memory[pc][0],memory[pc][1])
        if commands[pc] == "div":
            div(memory[pc][0],memory[pc][1])
            if reg_list['111']!='0000000000000000':
                fl=True
                setflag=True
        if commands[pc] == "cmp":
            compare(memory[pc][0],memory[pc][1])
        if commands[pc] == "not":
            invert(memory[pc][0],memory[pc][1])
        if commands[pc] == "ceil":
            ceil(memory[pc][0],memory[pc][1])
        if commands[pc] == "floor":
            floor(memory[pc][0],memory[pc][1])
        if commands[pc] == "swap":
            swap(memory[pc][0],memory[pc][1])
        if setflag==False:
            fl=False
        
        if types[pc+1]!="E":
            for m in memory[pc+1]:
                if m=="111":
                    fl=True
            if fl==False:
                reg_list["111"]='0000000000000000'
    
    if types[pc] == "D":
        fl=False
        for m in memory[pc]:
            if m=="111":
                fl=True
        if fl==False:
            reg_list["111"]='0000000000000000'
        if commands[pc]=="st":
            memaddrvalues[memory[pc][1]] = reg_list[memory[pc][0]] #key is mem_addr and value is reg value
        
        if commands[pc]=="ld":
            if memory[pc][1] not in memaddrvalues.keys():
                
                memaddrvalues[memory[pc][1]]=0
            
            reg_list[memory[pc][0]] = memaddrvalues[memory[pc][1]]
        fl=False
        
        if types[pc+1]!="E":
            for m in memory[pc+1]:
                if m=="111":
                    fl=True
            if fl==False:
                reg_list["111"]='0000000000000000'
    
    
    if types[pc]=="Floating":
        fl=False
        for m in memory[pc]:
            if m=="111":
                fl=True
        if fl==False:
            reg_list["111"]='0000000000000000'
        if commands[pc]=="mov":
            movf(memory[i][0],memory[i][1])
        fl=False
        
        if types[pc+1]!="E":
            for m in memory[pc+1]:
                if m=="111":
                    fl=True
            if fl==False:
                reg_list["111"]='0000000000000000'
        
    
    if types[pc]=="F":
        reg_list['111']='0000000000000000'
        dump_pc(pc)
        dump_rf()
        a=True
        break    
    
    if types[pc] == "E":
        
        
        if commands[pc]=="jmp":
            reg_list["111"] = "0000000000000000"
            i=pc
            dump_pc(i)
            dump_rf()
            cond=True
            pc=binary_to_integer(memory[i][0])
            
            
            
                    
        if commands[pc]=="jgt":
            if reg_list["111"] == "0000000000000010":
                reg_list["111"] = "0000000000000000"
                i=pc
                dump_pc(i)
                dump_rf()
                cond=True
                pc=binary_to_integer(memory[i][0]) 
                
                
            else:
                reg_list["111"] = "0000000000000000"
        
        if commands[pc]=="jlt":
            if reg_list["111"] == "0000000000000100":
                reg_list["111"] = "0000000000000000"
                i=pc
                dump_pc(i)
                dump_rf()
                cond=True
                pc=binary_to_integer(memory[i][0])
                
                
                
            else:
                reg_list["111"] = "0000000000000000"
            
        if commands[pc]=="je":
            
            if reg_list["111"]=="0000000000000001":
                reg_list["111"] = "0000000000000000"
                i=pc
                dump_pc(i)
                dump_rf()
                cond=True
                pc=binary_to_integer(memory[i][0])
                
                
            else:
                reg_list["111"] = "0000000000000000"
            

        

        
        
    if cond==False:
        
        dump_pc(pc)
        dump_rf()
        pc=pc+1
    cond=False
    
        
        
            
      
for i in memaddrvalues.values():
    if i==0:
        memorydump.append("0000000000000000")
    else:
        memorydump.append(i)
while len(memorydump)!=128:
    memorydump.append("0000000000000000")


for i in memorydump:
    print(i)
