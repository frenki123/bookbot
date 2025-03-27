from stats import words_in_string, char_counter, sort_dict_by_val

def get_book_text(filepath:str)->str:
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(data:list[dict[str, str|int]], num:int):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for pair in data:
        char = pair.get("char")
        if isinstance(char, str) and char.isalpha():
            total = pair.get("num")
            if isinstance(total, int):
                print(f"{char}: {total}")
    print("============= END ===============")


def main():
    text = get_book_text("./books/frankenstein.txt")
    num = words_in_string(text)
    chars = char_counter(text)
    data = sort_dict_by_val(chars)
    print_report(data, num)

if __name__ == "__main__":
    main()
