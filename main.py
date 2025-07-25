
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        num_words = len(f.read().split())
        return f"{num_words} words found in the document"


def main():
    text_len = get_book_text("./books/frankenstein.txt")
    print(text_len)

main()

