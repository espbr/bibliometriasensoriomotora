'''
Este programa utiliza um arquivo .csv (exportado pela base de dados
Scopus, com apenas o ano e as palavras chaves do autor selecionados) 
para calcular o número de palavras chaves únicas de dois períodos e 
para comparar esses perídos a fim de identificar o número de palavras
chaves em comum (palavras idênticas). (eduardosouzapaula@gmail.com)
'''


import re
import csv


def separa_sentencas(a_keywords):
    total = []
    for row in a_keywords:
        pal_chave = re.split(r'[;]+', row)
        total.append(pal_chave)   
 
    return total

    
def cria_lista(reader, ano_inicial, ano_final):
    a_keywords = []
    for row in reader:
        if row[0] <= ano_final and row[0] >= ano_inicial:
            a_keywords.append(row[2])
   
    return a_keywords


def cria_lista_unica(total):
    lista_unica = []
    for i in range(len(total)):
        tam = len(total[i])
        for j in range(tam):
            if total[i][j] != '': # Retiro palavras em branco
                elemento = total[i][j]
                elemento = elemento.strip() # Limpo espaços
                elemento = elemento.lower() # Deixo em minúsculo
                lista_unica.append(elemento)
    
    return lista_unica
    

def remove_repetidos(lista_unica):
    lista = lista_unica[:]
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[j] == lista[i]:
                del(lista[j])
            else:
                j = j + 1
        i = i + 1

    return lista
    
    
def conta_repetidos(l_palavras_final_1, l_palavras_final_2):
    cont = 0
    i = 0
    while i < len(l_palavras_final_1):
        j = i
        while j < len(l_palavras_final_2):
            if l_palavras_final_1 [i] == l_palavras_final_2 [j]:
                cont = cont + 1
                j = j + 1
            else:
                j = j + 1
        i = i + 1

    return cont
    
    
def mensagem(l_palavras_final_1, l_palavras_final_2, ano_ini_ant,
    ano_fim_ant, ano_ini_novo, ano_fim_novo):
    # Total de palavras chaves do periodo mais antigo
    msg_1 = ('\nO total de palavras chaves entre o ano de ' + ano_ini_ant +
    ' e ' +  ano_fim_ant + ' (excluíndo as repetidas) é de: ' + 
    str(len(l_palavras_final_1)))
    print(msg_1)
    
    # Total de palavras chaves do periodo mais antigo
    msg_2 = ('O total de palavras chaves entre o ano de ' + ano_ini_novo +
    ' e ' +  ano_fim_novo + ' (excuíndo as repetidas) é de: ' + 
    str(len(l_palavras_final_2)))
    print(msg_2)
     
    #Compara o perido mais antigo com o mais novo e conta as palavras repetidas
    conta_rep = conta_repetidos(l_palavras_final_1, l_palavras_final_2)
    msg_3 = ('\nOs periodos têm ' + str(conta_rep) + 
    ' palavras chaves em comum') 
    print(msg_3)


def main(reader, ano_inicial, ano_final):
    # Crio uma lista com todas as palavras-chaves
    a_keywords = cria_lista(reader, ano_inicial, ano_final)
        
    # Separo todas as palavras chaves, retirando o ';'
    total = separa_sentencas(a_keywords)
    
    # Crio um lista única, retirando as listas dentro das listas
    lista_unica = cria_lista_unica(total)  
    
    # Lita final sem elementos repetidos
    l_final = remove_repetidos(lista_unica)

    return l_final


# Lista final (mais antiga)
filename = 'key_words.csv'
with open(filename) as f:
    reader_1 = csv.reader(f)
    header_row = next(reader_1)
    ano_ini_ant = input('Digite o ano inicial do perído mais antigo: ')
    ano_fim_ant = input('Digite o ano final do período mais antigo: ')
    l_palavras_final_1 = main(reader_1, ano_ini_ant, ano_fim_ant)


# Lista final (mais nova)
filename = 'key_words.csv'
with open(filename) as f:
    reader_2 = csv.reader(f)
    header_row = next(reader_2)
    ano_ini_novo = input('\nDigite o ano inicial do período mais atual: ')
    ano_fim_novo = input('Digite o ano final do período mais atual: ')
    l_palavras_final_2 = main(reader_2, ano_ini_novo, ano_fim_novo)
    
 
# Envio mensagem para o usuário    
mensagem(l_palavras_final_1, l_palavras_final_2, ano_ini_ant,
 ano_fim_ant, ano_ini_novo, ano_fim_novo)
