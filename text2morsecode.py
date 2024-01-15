# =============================================================================
# Text to Morse Code Converter
# Author: Michael Sumaya
# !Spacing rules from https://future-seafarer.com/morse-code/
# 1. Space between letters of a word = 3 dots (spaces in this program)
# 2. Space between words = 7 dots (spaces in this program)
#
# Original GitHub URL: https://github.com/makolas2k20/text2morsecode.git
# =============================================================================
from text2morsecode_lib import MORSE_CODES

print("Text to Morse Codes!")
input_str = input("Enter string to convert:\n").lower()

converted_str = ""
for c in input_str:
    converted_str += "   " + MORSE_CODES[c]

print("Morse code is:\n")
print(f"{converted_str.strip()}")
