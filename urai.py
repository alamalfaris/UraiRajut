def urai(teks):                     # Buat nama function dan parameter. Inputnya berupa string teks
    pecah = ''                      # Buat string kosong untuk menampung hasil looping
    for i in range(1):              # Buat loop i sebanyak 1x yg didalamnya memuat loop j
        for j in range(len(teks)):  # Buat loop j sebanyak range(len(teks))
            pecah += teks[i:j+1]    # Setiap looping j, akan ditambahkan nilai teks[i:j+1] dalam var pecah 
    return pecah                    # Mengembalikan nilai var pecah setelah looping selesai

print(urai('Python'))

#==============================================================================================================================================

# CORET-CORET
# i = 0
# j = 0
# [0:0+1] = k

# i = 0
# j = 1
# [0:1+1] = kka

# i = 0
# j = 2
# [0:2+1] = kkakam

# i = 0
# j = 3
# [0:3+1] = kkakamkamb

# i = 0
# j = 4
# [0:4+1] = kkakamkambkambi

# i = 0
# j = 5
# [0:5+1] = kkakamkambkambikambin

# i = 0
# j = 6
# [0:6+1] = kkakamkambkambikambinkambing