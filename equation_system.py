import re
from sympy import solve, Symbol
from time import sleep


def resolver(txt):
    """
    Função para resolver funções simples e complexas
    :param txt: Título do projeto
    :return: Retorna o valor obtido da equação
    """
    print('-'*(len(txt)+25))
    print(txt.center(len(txt)+25))
    print('-' * (len(txt) + 25))
    sleep(.7)
    print('\033[31mRegras:'.center(len(txt)+25))
    sleep(1.1)
    print('1 - Digite a equação de forma correta, ou o sistema \nnão conseguirá dar uma resposta precisa;\n')
    sleep(1)
    print('2 - Não utilize vírgulas, pontos ou quaisquer outros \ntipos de pontuação;\n')
    sleep(1.2)
    print('3 - Utilize apenas UMA VARIÁVEL (X). Quaisquer outras \nvariáveis não permitirão a execução do programa.\n')
    sleep(1)
    print('4 - No caso de cálculos simples, como contas básicas, \nutilize uma variável para atribuir o resultado da conta.\033[m')
    print('-'*(len(txt)+25))
    sleep(0.6)
    while True:
        equacao = input('Digite uma equação: ')
        if re.search('[a-zA-Z]', equacao):
            if '=' in equacao:
                left, right = equacao.split('=')
                equacao = left + '-(' + right + ')'
            try:
                equacao = correct_equation(equacao)
                x = Symbol('x')
            except:
                print('\033[31mERRO! UTILIZE APENAS A VARIÁVEL VÁLIDA (x)!\033[m')
                continue
            else:
                return solve(equacao, x)[0]
        else:
            equacao = correct_equation(equacao)
            return solve(equacao)[0]


def correct_equation(equation):
    """
    Corrige a equação digitada pelo usuário
    :param equation: Recebe a equação
    :return: Retorna a equação com correções
    """
    equation = equation.replace(' ', '')
    equation = equation.replace('^', '**')
    equation = equation.replace('√', 'sqrt')
    if re.search('[a-zA-Z]', equation):
        for element in range(0, len(equation)):
            if element == 0:
                pass
            else:
                if ('x' in equation[element]) and equation[element - 1].isnumeric():
                    equation = replacer(equation, '*', element - 1)
    return equation


def replacer(string, newString, index, nofail=False):
    """
    Substitui e insere elementos em uma string determinada
    :param string: Recebe a string
    :param newString: String ou caractere a ser inserido na original
    :param index: index onde irá ocorrer a alteração
    :param nofail: Caso falso, permite com que haja a possibilidade de mostrar um erro
    :return: Retorna a string já formatada
    """
    if not nofail and index not in range(len(string)):
        raise ValueError("index outside given string")

    if index < 0:  # add it to the beginning
        return newString + string
    if index > len(string):  # add it to the end
        return string + newString

    return string[:index + 1] + newString + string[index + 1:]


resultado = resolver('SISTEMA DE RESOLUÇÃO DE EQUAÇÕES')
print(f'O resultado da equação é {resultado}')
