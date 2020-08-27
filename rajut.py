def rajut(teks, key):                  # Buat nama function dan parameter, inputnya berupa string teks dan key yg menjadi target rajut
    if (key in teks):                  # Buat kondisi jika nilai key berada dlm teks 
        index_rajut = teks.index(key)  # Maka cari index awal dari key, simpan dlm var index_rajut
    return teks[index_rajut:]          # Mengembalikan nilai slicing dri teks[index_rajut:]
    
teks = 'PPyPytPythPythoPython'
key = 'Python'
print(rajut(teks, key))