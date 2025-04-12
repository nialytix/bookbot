
def get_num_words(content):
    str = content.split()
    return len(str)

def get_num_char(content):
    content = content.lower()
    num_char = {}
    for c in content:
        if c in num_char:
            num_char[c] += 1
        else:
             num_char[c] = 1
    return num_char

def get_report(book, my_dict, num):
    report = f"============ BOOKBOT ============\nAnalyzing book found at books/{book}...\n----------- Word Count ----------\nFound {num} total words\n--------- Character Count -------\n"
    for n in my_dict:
        report = report + (f"{n}: {my_dict[n]}\n")
    report = report + "============= END ==============="
    return report