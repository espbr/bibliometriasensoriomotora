# Este programa utiliza um arquivo .csv (exportado pela base de dados
# Scopus, com apenas o autor, o título do documento, o ano, o DOI e 
# as palavras chaves do autor) para mostrar o DOI´s e os link dos artigos
# encontrados (eduardosouzapaula@gmail.com).


# This program uses a .csv file (exported by the Scopus database, with 
# only the author, the title of the document, the year, the DOI and the
# author's keywords) to show the DOI´s and the link of the articles 
# found (eduardosouzapaula @ gmail.com).


import re
import csv


def word_search(sentence):
    
    words = []
    
    for row in sentence:
        keyword = re.split(r'[;]+', row)
           
    return keyword


def clean_spaces(w_search):
    
    cleaned_list = []
    
    for i in w_search:
        element = i
        element = element.strip() # I clean the spaces       
        cleaned_list.append(element)
    
    return cleaned_list


def find_word(cleaned_spaces, keyword):
    if keyword in cleaned_spaces:
        return True
    

def main(reader, start_year, end_year, keyword):
    
    list_of_dictionaries = []
    
    for row in reader:
        if row[2] <= end_year and row[2] >= start_year:
            
            sentence = []
            sentence.append(row[5].lower())
            
            # I do a list with the words of this registry            
            w_search = word_search(sentence)
                        
            # I clean the spaces os the list
            cleaned_spaces = clean_spaces(w_search)
                        
            # I verify if the word is in the registry
            found_word = False
            found_word = find_word(cleaned_spaces, keyword)
            
            #Print the DOI of the keyword
            if found_word == True:
                print('\nDOI: ' + row[3])
                print('Link: ' + row[4])



filename = 'keys_words_articles.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    start_year = input('Digite o ano inicial: ')
    end_year = input('Digite o ano final: ')
    keyword = input('Digite a palavra chave que quer procurar: ')
    keyword = keyword.lower() # I leave the word in minuscule
    main(reader, start_year, end_year, keyword)

