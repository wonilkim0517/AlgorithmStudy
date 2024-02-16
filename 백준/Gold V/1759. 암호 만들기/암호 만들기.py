import sys
from itertools import combinations

input = sys.stdin.readline

L, C = map(int, input().split())
alphaList = sorted(input().split())

vowels = set('aeiou')
consonants = set('bcdfghjklmnpqrstvwxyz')
def has_vowel_and_consonant(code):
    vowel_count = sum(char in vowels for char in code)
    consonants_count = len(code) - vowel_count
    return vowel_count >= 1 and consonants_count >= 2

def is_in_order(code):
    return ''.join(sorted(code)) == code

for codePrint in combinations(alphaList, L):
    code = ''.join(codePrint)
    if has_vowel_and_consonant(code) and is_in_order(code):
        print(code)