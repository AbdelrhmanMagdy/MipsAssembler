from tables import instruction_table, register_table
from binHex_converter import hex2bin, bin2hex, intTo16Bin
from assembly_parser import lable_dict

word_array = []
def assemble(instruction_array):
    for word_i,word in enumerate(instruction_array):
        for element_i,element in enumerate(word):
            instruction = instruction_array[word_i] 
            # print(element)
            if element in register_table:
                instruction[element_i]=register_table[element]
            elif element in instruction_table:
                instruction[element_i]=instruction_table[element]['opcode']
                # print(hex2bin(instruction_table[element]['opcode'],6))
                if element=='sub' or element=='add' or element=='and' or element=='or' or element=='sub':  
                    # print(element)              
                    instruction.insert(len(instruction),'00') #add shamt
                    instruction.insert(len(instruction),instruction_table[element]['func'])
                elif element=='sll' or element=='sll''srl':
                    instruction.insert(1,'00') #add shamt
                    instruction.insert(len(instruction),instruction_table[element]['func'])
                elif element=='beq' or element=='bne':
                    instruction[3]=lable_dict[instruction[3]]-word_i-1 #add shamt
                # elif element=='sw' or element=='lw':
                    # instruction.insert(len(instruction),instruction_table[element][''])
                    # print(instruction)
                    # print(lable_dict[instruction[3]])
            else :
                # print('not foundeeeeeeeeed')
                pass
    # print(instruction_array)
    for word in instruction_array:
        output = ''
        print(word)
        if  (word[0] == '0x00') and (len(word)>4):            
            if (word[5]=='0x00' or word[5]=='0x02'): # sll / srl
                # print('here')
                output += hex2bin(word[0],6)
                output += hex2bin(word[1],5)
                output += hex2bin(word[3],5)
                output += hex2bin(word[2],5)
                output += '{0:05b}'.format(int(word[4]))
                output += hex2bin(word[5],6)
                word_array.append(output)
            else: #least of R format
                output += hex2bin(word[0],6)
                output += hex2bin(word[2],5)
                output += hex2bin(word[3],5)
                output += hex2bin(word[1],5)
                output += hex2bin(word[4],5)
                output += hex2bin(word[5],6)
                word_array.append(output)
        
        elif  word[0]=='0x23' or word[0]=='0x2B': # lw / sw
            output += hex2bin(word[0],6)
            output += hex2bin(word[3],5)
            output += hex2bin(word[1],5)
            output += intTo16Bin(str(word[2]))
            word_array.append(output)
            # print('output')
        elif  word[0]=='0x04' or word[0]=='0x05' : # beq and bne
            output += hex2bin(word[0],6)
            output += hex2bin(word[1],5)
            output += hex2bin(word[2],5)
            output += intTo16Bin(str(word[3]))
            # print(hex2bin(word[2],5))
            word_array.append(output)
     
        else:
            print('not provided: %s',word)
       
    # print(word_array)
    while '' in word_array:
        word_array.remove('')
    return word_array