import sys
from stats import count_words, calculate_char_stats, sorted_char_stats

def get_book_text(filepath):
    with open(filepath) as f:
        ret = f.read()
    return ret

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = count_words(text)
    char_stats = calculate_char_stats(text)
    sorted_stats = sorted_char_stats(char_stats)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for ch, count in sorted_stats:
        if not ch.isalpha():
            continue
        print(f"{ch}: {count}")
    

main()
