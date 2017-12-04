instruction_array = []
lable_dict = {}
def parse(input_lines):
    for line_i,line in enumerate(input_lines):
        if ':' in line:
            lable = line.split(':')[0]
            lable_dict[lable]=line_i
            line = line[3:]
            # print(lable_dict)
        instruction = line.strip().replace(' ',',',1).replace(')','').replace('(',',')
        instruction = instruction.replace(' ','').split(',')
        instruction_array.append(instruction)
    return instruction_array