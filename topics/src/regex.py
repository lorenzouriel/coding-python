import re

# Test the functions
cpf = '123.456.789-09'
cpf1 = str(input('Digite um CPF (com pontos):'))


def validate_cpf(cpf):
    # Remove non-digit characters
    cpf = re.sub(r'\D', '', cpf)
    
    # Check if the CPF has 11 digits
    if len(cpf) != 11:
        return False
    
    # Check for repeated digits
    if len(set(cpf)) == 1:
        return False
    
    # Calculate the verification digits
    total1 = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digit1 = (total1 * 10) % 11
    if digit1 == 10:
        digit1 = 0
    
    total2 = sum(int(cpf[i]) * (11 - i) for i in range(9))
    total2 += digit1 * 2
    digit2 = (total2 * 10) % 11
    if digit2 == 10:
        digit2 = 0
    
    # Check if the verification digits match
    return cpf[-2:] == f'{digit1}{digit2}'

print(f'CPF {cpf} is valid: {validate_cpf(cpf)}')
print(f'CPF {cpf1} is valid: {validate_cpf(cpf1)}')