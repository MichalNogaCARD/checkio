 Your task is to decrypt the secret message using the Morse code .
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

example

Input: The secret message.

Output: The decrypted text.

Example:
morse_decoder("... --- -- .   - . -..- -") == "Some text"
morse_decoder("..--- ----- .---- ---..") == "2018"
morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

 How it is used: For cryptography and spy work.

Precondition :
0 < len(message) < 100
The message will consists of numbers and English letters only. 