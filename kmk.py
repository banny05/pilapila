#list
def lost_inventory(items):
    isi = []
    for i in range (items):
       return any(items in items)        
    
    
    
list_inp_user = eval(input())

import sys
input = sys.stdin.readline

#lupasoal
def selesaikan():
    p, r = map(int, input().split())
    k = list(map(int, input().split()))
    
    bagian = [L]
    
    for a in k:
        idx = a - 1
        stngh = bagian[idx] // 2
        bagian = bagian[:idx] + [stngh, stngh] + bagian[idx+1:]
    
    print(*bagian)

selesaikan()

#row
def decrypt_row_transposition_cipher(pesan, key):
    key = key.upper()
    sorted_key = sorted(key)
    
    char_to_rank = {}
    for i, char in enumerate(sorted_key):
        char_to_rank[char] = i
    
    result = sorted(pesan, key=lambda row: char_to_rank[row[0]])
    
    return result


pesan = eval(input())
key = input()
hasil = decrypt_row_transposition_cipher(pesan, key)
print(hasil)
