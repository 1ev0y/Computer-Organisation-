f1 = open("Assembly Instructions.txt","r")
f2 = open("Executable.txt","w")

line_count = 0

var_list = []
instr_list = []
label_list = []
opcode_list = ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']
op_4_list = ['add','sub','mul','xor','or','and']
op_3_list = ['mov','ld','st','div','rs','ls','not','cmp']
op_2_list = ['jmp','jlt','jgt','je']

toggle_var_start = 33

for i in f1:
    line_count+=1
    instr_list.append(i)

    if i.endswith('\n'):
        s1 = i[:-1]
    else:
        s1 = i

    l2 = s1.split()

    if l2 == []:
        continue
    
    if l2[0]=='var':
        if toggle_var_start == 33:
            if len(l2) != 2:
                s2 = "Line " + str(line_count) + ": General Syntax Error"
                f2.write(s2)
                break
            else:
                if l2[1] not in var_list:
                    if l2[1].isalnum():
                        var_list.append(l2[1])
                    else:
                        s2 = "Line " + str(line_count) + ": General Syntax Error"
                        f2.write(s2)
                        break
        
        else:
            s2 = "Line " + str(line_count) + ": Variables not declared at the beginning"
            f2.write(s2)
            break
    
    elif len(l2) == 1:
        toggle_var_start = 0
        if l2[0].endswith(':'):
            s3 = l2[0][:-1]
            if s3.isalnum() and s3 not in label_list:
                label_list.append(s3)
            else:
                s2 = "Line " + str(line_count) + ": General Syntax Error"
                f2.write(s2)
                break
        else:
            if l2[0] != 'hlt':
                s2 = "Line " + str(line_count) + ": Typo in Instruction Name"
                f2.write(s2)
                break
