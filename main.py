from stats import get_num_words
from stats import get_num_char
from stats import get_report
import sys

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

if(len(sys.argv)<2):
    raise Exception("Usage: python3 main.py <path_to_book>")
else:
    content_string = get_book_text(sys.argv[1])
    num = get_num_words(content_string)
    print(f"{num} words found in the document")
    print(get_report(sys.argv[1],get_num_char(content_string), num))


