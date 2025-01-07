# Goal of this project is to print out a book report containing the book name, number of words, and the sorted dictionary
# of characters in the book along with their counts.

def open_book(filepath):
    with open(filepath) as file:
        text = file.read()
        return text

def count_words(text):
    words_counts = 0
    for word in text.split():
        words_counts += 1

    return words_counts

def dict_charac(text):  
    text_lower = text.lower()
    dict_charac = {}
    for charac in text_lower:
        if charac not in dict_charac:
            dict_charac[charac] = 1
        else:
            dict_charac[charac] += 1

    return dict_charac

def main():
    print(f'Book Report of the Book: {filepath}')

    text = open_book(filepath)
    words_counts = count_words(text)
    print(f"Total words in the book {filepath}: {words_counts}")
    
    dict_book = dict_charac(text)

    for w in (sorted(dict_book, key = dict_book.get, reverse = True)):
        if w.isalpha():
            print(f'The character "{w}" appears {dict_book[w]} times in the book')
        else:
            continue


filepath = "books/frankenstein.txt"

main()