import sys
def fix_len(s1):
    if len(s1) >= 8:
        return s1
    
    s1 = str(s1)
    if len(s1)==7:
        return s1
    
    while len(s1)!=7:
        s1 = '0' + s1

    return s1

def file_analysis(l2):
    global main_string
    global toggle_var_start
    global mem_address

    if l2 == []:
        return 0
    
    if l2[0]=='var':
        if toggle_var_start == 33:
            if len(l2) != 2:
                s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
                f2.write(s2)
                return 12
            else:
                mem_address+=1
                if mem_address>=128:
                    return 12
                
                if l2[1] not in var_list:
                    var_list[l2[1]] = fix_len(bin(mem_address)[2:])
                
                else:
                    var_list[l2[1]] = fix_len(bin(mem_address)[2:])
        
        else:
            if len(l2) != 2:
                s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
                f2.write(s2)
                return 12
            
            s2 = "Error on Line " + str(line_count) + ": Variables not declared at the beginning"
            f2.write(s2)
            return 12
        
    elif len(l2) >= 2 and l2[1] == ':':
        s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
        f2.write(s2)
        return 12
    
    elif len(l2) == 1:
        toggle_var_start = 0

        if l2[0] not in opcode_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Instruction Name \'" + l2[0] + "\'"
            f2.write(s2)
            return 12

        elif l2[0] != 'hlt':
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12
    
    elif l2[0] in op_2_list:
        toggle_var_start = 0

        if len(l2) != 2:
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12

        if l2[1] not in label_list:
            if l2[1] in var_list:
                s2 = "Error on Line " + str(line_count) + ": Misuse of variable \'" + l2[1] + "\'"+" as label"
                f2.write(s2)
                return 12

            else:
                s2 = "Error on Line " + str(line_count) + ": Use of undefined label \'" + l2[1] + "\'"
                f2.write(s2)
                return 12
            
        main_string = main_string + op_2_list[l2[0]] + '0000' + label_list[l2[1]] + '\n'

    elif l2[0] in op_3_reg_mem_list:
        toggle_var_start = 0

        if len(l2) != 3:
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12
        
        if l2[1] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[1] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Register Name \'" + l2[1] + "\'"
            f2.write(s2)
            return 12

        if l2[2] not in var_list:
            if l2[2] in label_list:
                s2 = "Error on Line " + str(line_count) + ": Misuse of label \'" + l2[2] + "\'" + " as variable"
                f2.write(s2)
                return 12

            else:
                s2 = "Error on Line " + str(line_count) + ": Use of undefined variable \'" + l2[2] + "\'"
                f2.write(s2)
                return 12
            
        main_string = main_string + op_3_reg_mem_list[l2[0]] + '0' + reg_list[l2[1]] + var_list[l2[2]] + '\n'

    elif l2[0] in op_3_reg_imm_list:
        toggle_var_start = 0

        if len(l2) != 3:
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12
        
        if l2[1] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[1] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Register Name \'" + l2[1] + "\'"
            f2.write(s2)
            return 12

        if not l2[2].startswith("$"):
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12

        try:
            if not (0 <= int(l2[2][1:]) <= 127):
                s2 = "Error on Line " + str(line_count) + ": Illegal Immediate Value \'" + l2[2][1:] + "\'"
                f2.write(s2)
                return 12
        
        except:
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12
        
        main_string = main_string + op_3_reg_imm_list[l2[0]] + '0' + reg_list[l2[1]] + fix_len(bin(int(l2[2][1:]))[2:]) + '\n'

    elif l2[0] in op_3_reg_reg_list:
        toggle_var_start = 0

        if len(l2) != 3:
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12
        
        if l2[1] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[1] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Name of First Register \'" + l2[1] + "\'"
            f2.write(s2)
            return 12
        
        if l2[2] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[2] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Name of Second Register \'" + l2[2] + "\'"
            f2.write(s2)
            return 12
        
        main_string = main_string + op_3_reg_reg_list[l2[0]] + '00000' + reg_list[l2[1]] + reg_list[l2[2]] + '\n'

    elif l2[0] in op_4_list:
        toggle_var_start = 0

        if len(l2) != 4:
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12
        
        if l2[1] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[1] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Name of First Register \'" + l2[1] + "\'"
            f2.write(s2)
            return 12
        
        if l2[2] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[2] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Name of Second Register \'" + l2[2] + "\'"
            f2.write(s2)
            return 12
        
        if l2[3] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[3] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Name of Third Register \'" + l2[3] + "\'"
            f2.write(s2)
            return 12
        
        main_string = main_string + op_4_list[l2[0]] + '00' + reg_list[l2[1]] + reg_list[l2[2]] + reg_list[l2[3]] + '\n'

    elif l2[0] == 'mov':
        toggle_var_start = 0

        if len(l2) != 3:
            s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
            f2.write(s2)
            return 12
        
        if l2[1] == 'FLAGS':
            s2 = "Error on Line " + str(line_count) + ": Illegal use of FLAGS register"
            f2.write(s2)
            return 12

        if l2[1] not in reg_list:
            s2 = "Error on Line " + str(line_count) + ": Typo in Name of First Register \'" + l2[1] + "\'"
            f2.write(s2)
            return 12

        if l2[2] in reg_list:
            main_string = main_string + '0001100000' + reg_list[l2[1]] + reg_list[l2[2]] + '\n'

        else:
            if l2[2].startswith('$'):
                try:
                    if not (0 <= int(l2[2][1:]) <= 127):
                        s2 = "Error on Line " + str(line_count) + ": Illegal Immediate Value \'" + l2[2][1:] + "\'"
                        f2.write(s2)
                        return 12
                
                except:
                    s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
                    f2.write(s2)
                    return 12

            else:
                if l2[2] not in reg_list:
                    s2 = "Error on Line " + str(line_count) + ": Typo in Name of Second Register \'" + l2[2] + "\'"
                    f2.write(s2)
                    return 12
                
            main_string = main_string + '000100' + reg_list[l2[1]] + fix_len(bin(int(l2[2][1:]))[2:]) + '\n'
    
    else:
        toggle_var_start = 0
        s2 = "Error on Line " + str(line_count) + ": Typo in Instruction Name"
        f2.write(s2)
        return 12

f1 = sys.stdin.readlines()
f2 = sys.stdout

line_count = 0

var_list = {}
instr_list = []
label_list = {}
opcode_list = ['add','sub','mov','ld','st','mul','div','rs','ls','xor','or','and','not','cmp','jmp','jlt','jgt','je','hlt']
op_4_list = {'add':'00000','sub':'00001','mul':'00110','xor':'01010','or':'01011','and':'01100'}
op_3_reg_reg_list = {'div':'00111','not':'01101','cmp':'01110'}
op_3_reg_imm_list = {'rs':'01000','ls':'01001'}
op_3_reg_mem_list = {'ld':'00100','st':'00101'}
op_2_list = {'jmp':'01111','jlt':'11100','jgt':'11101','je':'11111'}
reg_list = {'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}

toggle_var_start = 33
toggle_first_part = 33
toggle_second_part = 33

main_string = ''

mem_address = -1

for i in f1:
    line_count+=1
    i.replace('\t','')
    if i.endswith('\n'):
        s1 = i[:-1]
    else:
        s1 = i
    l2 = s1.split()

    if len(l2) >= 1:
        if l2[0] != 'var':
            mem_address +=1
            
        if l2[0].endswith(':'):
            s3 = l2[0][:-1]
            if s3 not in label_list:
                label_list[s3] = fix_len(bin(mem_address)[2:])

            else:
                toggle_first_part = 0
                s2 = "Error on Line " + str(line_count) + ": General Syntax Error"
                f2.write(s2)
                break



if toggle_first_part == 33:
    
    line_count = 0

    for i in f1:
        line_count+=1
        i.replace('\t','')
        if i.endswith('\n'):
            s1 = i[:-1]
        else:
            s1 = i
        instr_list.append(s1)

        l2 = s1.split()

        try:
            if l2[0].endswith(':'):
                toggle_var_start = 0

                i1 = file_analysis(l2[1:])
                if i1 == 12:
                    toggle_second_part = 0
                    break
                if i1 == 0:
                    continue

            else:
                i1 = file_analysis(l2)
                if i1 == 12:
                    toggle_second_part = 0
                    break
                if i1 == 0:
                    continue

        except:
            i1 = file_analysis(l2)
            if i1 == 12:
                toggle_second_part = 0
                break
            if i1 == 0:
                continue




instr_list = []


for i in f1:
    i.replace('\t','')
    if i.endswith('\n'):
        s1 = i[:-1]
    else:
        s1 = i
    instr_list.append(s1)


line_count = len(instr_list)+1
last_line_idx = 0
instr_list.reverse()
if toggle_first_part==33 and toggle_second_part==33:
    for i in instr_list:
        line_count-=1
        l3 = i.split()
        if l3 == []:
            continue

        else:
            last_line_idx = line_count

        if len(l3)==2:
            if l3[1] != 'hlt':
                
                s2 = "Error on Line " + str(line_count) + ": Missing Hlt Instruction"
                toggle_second_part = 0
                f2.write(s2)
                
            break

        elif len(l3)==1:
            if l3[0] != 'hlt':
                
                s2 = "Error on Line " + str(line_count) + ": Missing Hlt Instruction"
                toggle_second_part = 0
                f2.write(s2)
                
            break

        else:
            
            s2 = "Error on Line " + str(line_count) + ": Missing Hlt Instruction"
            toggle_second_part = 0
            f2.write(s2)
            
        break

    instr_list.reverse()
    for i in range(1,len(instr_list)+1):
        l3 = instr_list[i-1].split()
        
        if i == last_line_idx:
            break

        if len(l3) == 2:
            if l3[0].endswith(":"):
                if l3[1] == 'hlt':
                    
                    toggle_second_part = 0
                    s2 = "Error on Line " + str(i) + ": Hlt not being used as the last instruction"
                    f2.write(s2)
                    
                    break

        if len(l3) == 1:
            if l3[0] == 'hlt':
                
                toggle_second_part = 0
                s2 = "Error on Line " + str(i) + ": Hlt not being used as the last instruction"
                f2.write(s2)
                
                break

if toggle_first_part==33 and toggle_second_part==33:
    main_string = main_string + '1101000000000000'
    
    f2.write(main_string)
    toggle_second_part=0

    
if toggle_first_part==33 and toggle_second_part==33:
    if mem_address >= 128:
        
        f2.write("Error on Line 129: More than 128 Memory Addresses")
