import streamlit as st
import random
import base64
import pandas as pd
from pathlib import Path
import copy
import numpy as np

def get_alphabet(size):
    if size == "min":
        alphabet = get_min_alphabet()
    elif size == "maj":
        alphabet = get_maj_alphabet()
    special_letters = ["â", "ç", "é", "è", "ê", "ë", "î", "ï", "ô", "û", "ü"]
    alphabet += special_letters
    return alphabet

def get_min_alphabet():
    min_alphabet = ["a", "b", "c", "d", "e", "f", "g",
                    "h", "i", "j", "k", "l", "m",
                    "n", "o", "p", "q","r", "s", "t",
                    "u", "v", "w", "x", "y", "z"] 
    return min_alphabet

def get_maj_alphabet():
    maj_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q","R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]
    return maj_alphabet



@st.cache
def clean_word_list(file):
    #read
    bytes = file.read()
    #decode into string
    string = bytes.decode("utf-8")
    #array
    word_list = string.split("\r\n")
    
    no_composed_words_on = True
    no_caps_on = True
    format_on = True
    deformat_on = False
    
    if no_composed_words_on:
     simple_word_list = remove_composed_words(word_list)
     
    if no_caps_on:
     no_caps_word_list = remove_caps(simple_word_list)
    
    if format_on:
        final_word_list = format_word_list(no_caps_word_list)
    
    if deformat_on:
        final_word_list = deformat_word_list(word_list)
    
    return final_word_list
    
def format_word_list(word_list):
    for i in range(len(word_list)):
        word = word_list[i]
        formated_word = " " + word + " "
        word_list[i] = formated_word
        
    formated_word_list = word_list
    return formated_word_list

def deformat_word_list(word_list):
    for i in range(len(word_list)):
        word = word_list[i]
        word_as_list = list(word)
        word_as_list.pop(0)
        word_as_list.pop(len(word_as_list)-1)
        formated_word = "".join(word_as_list)
        word_list[i] = formated_word
        
    deformated_word_list = word_list
    return deformated_word_list

def download_link(list):
    df = pd.DataFrame(list)
    # When no file name is given, pandas returns the CSV as a string, nice.
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="data.txt">Download cleaned text file</a>'
    st.markdown(href, unsafe_allow_html=True)

def remove_composed_words(word_list):
    number_of_words = len(word_list)
    print(number_of_words)
    for i in range(number_of_words):
        try:
            word = word_list[i]
            if is_composed_word(word):
                word_list.pop(i)
        except:
            pass
    simple_word_list = word_list
    return simple_word_list
    
def is_composed_word(word):
    word_as_list = string2list(word)
    word_length = len(word_as_list)
    for i in range(word_length):
        letter = word_as_list[i]
        if letter == " " or letter == "-" or letter == "'" or letter == "." or letter == "!":
            return True
    return False
    

def remove_caps(word_list):
    number_of_words = len(word_list)
    for i in range(number_of_words):
        word = word_list[i]
        print(i, word)
        first_letter = word[0]
        if not is_minuscule(first_letter):
            clean_word = minusculise_word(word)
            word_list[i] = clean_word
    clean_word_list = word_list
    return clean_word_list

def minusculise(letter):
    if is_minuscule(letter):
        return letter
    else:
        maj_letter = letter
        position = find_maj_alphabet_position(maj_letter)
        min_letter = get_min_letter(position)
    return min_letter
    
def is_minuscule(letter):
    min_alphabet = get_alphabet("min")
    for min_letter in min_alphabet:
        if letter == min_letter:
            return True
    return False
    
def find_maj_alphabet_position(maj_letter):
    maj_alphabet = get_alphabet("maj")
    alphabet_length = len(maj_alphabet)
    for i in range(alphabet_length):
        if maj_letter == maj_alphabet[i]:
            return i

def get_min_letter(position):
    min_alphabet = get_alphabet("min")
    return min_alphabet[position]
    
def minusculise_word(word):
    word_as_list = string2list(word)
    clean_word_as_list = minusculise_each_letter(word_as_list)
    clean_word = list2string(word_as_list)
    return clean_word

def minusculise_each_letter(word_as_list):
    word_length = len(word_as_list)
    for i in range(word_length):
        letter = word_as_list[i]
        min_letter = minusculise(letter)
        word_as_list[i] = min_letter
    
    clean_word_as_list = word_as_list
    return clean_word_as_list
    
def string2list(string):
    return list(string)

def list2string(array):
    string = "".join(array)
    return string
    
    

def pifometrus(word_length):
    random_word = create_random_word(word_length)
    return random_word

def create_random_word(word_length):
    word = ""
    for i in range(word_length):
        random_letter = create_random_letter()
        word += random_letter
    return word    
    
def create_random_letter():
    min_alphabet = get_min_alphabet()
    
    alphabet_length = len(min_alphabet)
    random_position = random.randrange(0, alphabet_length, 1)
    
    random_letter = min_alphabet[random_position]
    return random_letter
@st.cache
def initialize_program():
    setup_word_list = get_setup_word_list()
    
    #st.write(setup_word_list)
    
    
    stats = get_stats(setup_word_list)
    sums_of_columns = get_sums_of_columns(stats)
    
    normalized_stats = copy.deepcopy(stats)
    
    for letter1 in stats: 
        sum_of_column = sums_of_columns[letter1]
        for letter2 in stats:
            normalized_stats[letter1][letter2] = normalized_stats[letter1][letter2] / sum_of_column
    
    
    return normalized_stats

def get_sums_of_columns(stats):
    sums_of_columns = initialize_sums_of_columns()
    fill_sums_of_columns(sums_of_columns, stats)
    return sums_of_columns

def fill_sums_of_columns(sums_of_columns, stats):
    for letter1 in stats:
        sum_of_the_column = 0
        for letter2 in stats[letter1]:
            sum_of_the_column += stats[letter1][letter2]
        
        sums_of_columns[letter1] += sum_of_the_column

def initialize_sums_of_columns():
    sums_of_columns = {}
    custom_alphabet = get_custom_alphabet()
    for letter in custom_alphabet:
        sums_of_columns[letter] = 0
    return sums_of_columns
    
@st.cache
def get_stats(setup_word_list):
    stats = initialize_stats()
    fill_stats(setup_word_list, stats)
    return stats

def fill_stats(setup_word_list, stats):
    for word in setup_word_list:
        count_word(word, stats)
    filled_stats = stats
    return filled_stats
    
def count_word(word, stats):
    for i in range(len(word)):
        if i < len(word) - 1:
            letter = word[i]
            next_letter = word[i+1]
            stats[letter][next_letter] += 1
    
def get_custom_alphabet():
    alphabet = get_alphabet("min")
    custom_alphabet = [" "] + alphabet
    return custom_alphabet

def initialize_stats():
    stats = {}
    custom_alphabet = get_custom_alphabet()
    for letter1 in custom_alphabet:
        stats[letter1] = {}
        for letter2 in custom_alphabet:
            stats[letter1][letter2] = 0
    return stats
            
def get_setup_word_list():
    setup_file_path = find_setup_file_path()
    setup_content = extract_file_content(setup_file_path)
    setup_word_list = txt_string2list(setup_content)
    return setup_word_list
    
def extract_file_content(file_path):
    file = open(file_path, "r", encoding="utf-8")
    file_content = file.read()
    return file_content

def find_setup_file_path():
    script_path = Path(__file__).absolute().parent
    setup_file_path = script_path / 'setup.txt'
    return setup_file_path

def txt_string2list(txt_string):
    list = txt_string.split("\n")
    return list
    
    
def prononciatus(stats):
    word_size = random.randrange(3, 10, 1)
    word = []
    associated_probas = []
    for i in range(word_size):
        if i == 0:
            next_letter = letter_after_letter(" ", stats)
            word.append(next_letter)
        else:
            
            last_letter = word[len(word)-1]
            next_letter = letter_after_letter(last_letter, stats)
            word.append(next_letter)
    word = "".join(word)
    return word
    
def letter_after_letter(letter, stats):
    letter_distribution = stats[letter]
    letter_distribution_list = list(letter_distribution.values())
    alphabet = get_custom_alphabet()
    next_letter = pick_a_letter(alphabet, letter_distribution_list)
    return next_letter

def pick_a_letter(alphabet, a_distribution_list):
    choice = np.random.choice(alphabet, p=a_distribution_list)
    return choice

def generate_word(yes, stats):
    if yes:
        word = prononciatus(stats)
        st.write(word)
###################################################### app
def app():
    #test zone
    #test zone
    st.markdown("""
    ## Le poete
    Le but est de génerer des mots qui sonnent bien en français.
    """)
    
    expander_pifometrus = st.beta_expander("Pifometrus")
    with expander_pifometrus:
        st.markdown("""
        Fonction qui génère des mots au pif.
        """)
        create_word = st.button("Créer un mot")
        if create_word:
            new_word = pifometrus(random.randrange(4, 10, 1))
            st.write(new_word)
    
    
    expander_prononciatus = st.beta_expander("Prononciatus")
    with expander_prononciatus:
        st.markdown("""
        Fonction qui génère des mots prononçables.
        
        """)
        
        default_setup_on = st.button("Démarer le générateur")
        stats = {}
        df = pd.DataFrame()
        if default_setup_on:
            stats = initialize_program()
            #df = pd.DataFrame(data=stats)
            #st.write(df)
            
            word = prononciatus(stats)
            st.write(word)
        
        #generate_word_on = st.button("Créer un mot prononçable")
        
            
        
    expander_sonnebientus = st.beta_expander("Sonnebientus")
    with expander_sonnebientus:
        st.markdown("""
        Fonction qui génère des mots qui sonnent bien.
        """)
    
        
    expander_clean_file = st.beta_expander("Clean txt file")
    with expander_clean_file:
        words_file = st.file_uploader("Fichier texte avec tous les mots", type=["txt"])
        if words_file: 
            clean_word_list_from_file = clean_word_list(words_file)
            st.write("remove the first 0 after download")
            download_link(clean_word_list_from_file)
    


        
    
    
    
    
