# Cypher-cracker

This project is a simple Python-based tool designed to help crack password hashes using a wordlist. It supports popular hashing algorithms like MD5, SHA1, SHA256, SHA512, SHA3-512, SHA384, and SHA224. The tool works by taking a hash input from the user, then comparing it to the hashes of words from a wordlist until it finds a match.

How It Works:

1.Choose a Hash Algorithm: Select the algorithm used to generate the hash.

2.Provide the Hash: Enter the hash value you want to crack.

3.Use a Wordlist: The tool will download a wordlist if it’s not available locally. It then hashes each word and compares it to the provided hash.

4.Crack the Hash: If a match is found, the corresponding word is displayed as the cracked password. If no match is found, it lets you know.
