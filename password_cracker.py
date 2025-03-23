import hashlib
import os
import urllib.request

HASH_FUNCTIONS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
    "sha3_512": hashlib.sha3_512,
    "sha384": hashlib.sha384,
    "sha224": hashlib.sha224
}

def main():
    while True:
        print_ascii_cat("Hash Cracker")
        print("1. Crack a hash\n2. Exit")
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == "1":
            hash_to_crack = input("Enter the hash to crack: ")
            hash_function = select_hash_function()
            wordlist_path = download_wordlist()
            if not wordlist_path:
                continue
            encoding = input("Enter the character encoding of the wordlist (press Enter for default latin-1): ") or "latin-1"

            try:
                with open(wordlist_path, "r", encoding=encoding) as f:
                    for word in f:
                        word = word.strip()
                        hashed_word = hash_function(word.encode(encoding)).hexdigest()
                        if hashed_word == hash_to_crack:
                            print(f"Hash cracked: {word}")
                            break
                    else:
                        print("Hash not found in wordlist.")
            
            except Exception as e:
                print(f"An error occurred: {e}")
                if input("Press 'Enter' to return to the main menu or 'q' to quit: ") == 'q':
                    break
                
        elif choice == "2":
            break
            
        else:
            print("Invalid choice. Please enter 1 or 2.")
            
    print("Goodbye!")

def print_ascii_cat(tool_name):
    print(r'''
 /\_/\  
( o.o ) 
 > ^ <  ''', tool_name, "\n")

def select_hash_function():
    while True:
        print("Select the hash function to use:")
        for i, function_name in enumerate(HASH_FUNCTIONS):
            print(f"{i+1}. {function_name}")
        choice = input(f"Enter your choice (1-{len(HASH_FUNCTIONS)}): ")
        try:
            index = int(choice) - 1
            function_name = list(HASH_FUNCTIONS.keys())[index]
            return HASH_FUNCTIONS[function_name]
        except (IndexError, ValueError):
            print(f"Invalid choice. Please enter a number from 1 to {len(HASH_FUNCTIONS)}.")

def download_wordlist():
    if os.path.exists("wordlist.txt"):
        return "wordlist.txt"
    url = "https://raw.githubusercontent.com/Shresth2610/Password-cracker/main/wordlists.txt"
    print("Downloading wordlist...")
    try:
        urllib.request.urlretrieve(url, "wordlist.txt")
    except Exception as e:
        print(f"Failed to download wordlist: {e}")
        return None
    print("Wordlist downloaded.")
    return "wordlist.txt"

if __name__ == "__main__":
    main()
