def number_of_words(text):
    return len(text.split())

def count_letters(text):
    dico = {}
    for char in text.lower():
        if char.isalpha(): 
            dico[char] = dico[char] + 1 if char in dico else 1

    return dico

def printReport(text):
    words = number_of_words(text)
    letter_count = count_letters(text)

    print("--- Begin report of books/frankenstein.txt---")
    print(f"{words} words found in the document")
    print()

    for k, v in sorted(letter_count.items(), key=lambda x : x[1], reverse=True):
        print(f"The '{k}' character was found {v} times")

    print("--- End of report---")


with open("books/frankenstein.txt") as f:
    file_content = f.read()
    printReport(file_content)