import os

def reverse_string(file_path):
    # må ha enconding som støtter æ ø og å
    with open(file_path, 'r', encoding='utf-8') as file:
        # leser tekst filen og splitter ordene i strenger inn i en liste
        read_text_file = file.read().split()
        
        reversed_list = []
        
        # går gjennom alle ord i listen og legger de reversert i en ny liste
        for word in read_text_file:
            reversed_list.append(word[::-1])
        
        return reversed_list

reversed_words = reverse_string(r"Oppgave 1\file.txt")

for word in reversed_words:
    print(word)

