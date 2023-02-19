# 111.444.777-05

# 1 1 1 4 4 4 7 7 7     - 0 5 
# 0 1 2 3 4 5 6 7 8
def cpf_validator(cpf: str):
    
    cpf_only_numbers = cpf.replace('.', '').replace('-', '')
    
    if isinstance(cpf, str):
        new_cpf = cpf_only_numbers[:9]
        
    if not new_cpf.isnumeric():
        return False
    
    elif isinstance(cpf, int):
        raise TypeError("O Cpf não pode ser um inteiro")
    
    
    # Calculus of first digit
    
    rest_first_division = get_sum(10, new_cpf) % 11
    
    if rest_first_division < 2:
        new_cpf += '0'
    else: 
        new_cpf += str(11 - rest_first_division)
    
    # Calculus of second digit
    
    rest_second_division = get_sum(11, new_cpf) % 11
    
    if rest_second_division < 2:
        new_cpf += '0'
    else:
        new_cpf += str(11 - rest_second_division)
        
    # Is cpf valid ?
    
    if new_cpf == cpf_only_numbers:
        return (new_cpf, True)
    else:
        return (new_cpf, False)
    
    
            

def get_sum(start: int, cpf: str):
    """
    Function to multiple the numbers with the start integer
    """
    sum_ = 0
    m = start
    
    for number in cpf:
        sum_ += int(number) * m
        m -= 1
    
    return sum_
    

result_cpf, is_valid = cpf_validator("111.444.777-05")

print(result_cpf, is_valid)