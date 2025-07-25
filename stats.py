
def get_num_words(path_to_file):
    with open(path_to_file) as f:
        num_words = len(f.read().split())
        return f"{num_words} words found in the document"


