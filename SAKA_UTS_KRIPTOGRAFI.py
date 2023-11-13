import sys
import numpy as np #berfungsi untuk memproses komputasi numerik


def cipher_encryption():
    msg = input("Enter message: ").upper()
    msg = msg.replace(" ", "")

    # jika msg tersebut merupakan angka ganjil, maka menambahkan x di akhir
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "x"
        len_chk = 1

    # msg ke matriks
    row = 2
    col = int(len(msg)/2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i])-65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i])-65)
            itr2 += 1
    # for

    key = input("Enter 4 letter Key String: ").upper()
    key = key.replace(" ", "")

    # key ke matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3])-65
            itr3 += 1

    # melakukan pengecekan validitas terhadap key
    # kemudian mencari determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # cara mencari invers perkalian
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    if mul_inv == -1:
        print("Invalid key")
        sys.exit()
    # if

    encryp_text = ""
    itr_count = int(len(msg)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    else:
        for i in range(itr_count-1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            encryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            encryp_text += chr((temp2 % 26) + 65)
        # for
    # if else

    print("Encrypted Text: {}".format(encryp_text))
    #mencetak enkripsi text


def cipher_decryption():
    msg = input("Enter message: ").upper()
    msg = msg.replace(" ", "")

    # jika msg tersebut merupakan angka ganjil, maka menambahkan 0 di akhir
    len_chk = 0
    if len(msg) % 2 != 0:
        msg += "x"
        len_chk = 1

    # msg ke matriks
    row = 2
    col = int(len(msg) / 2)
    msg2d = np.zeros((row, col), dtype=int)

    itr1 = 0
    itr2 = 0
    for i in range(len(msg)):
        if i % 2 == 0:
            msg2d[0][itr1] = int(ord(msg[i]) - 65)
            itr1 += 1
        else:
            msg2d[1][itr2] = int(ord(msg[i]) - 65)
            itr2 += 1
    # for

    key = input("Enter 4 letter Key String: ").upper()
    key = key.replace(" ", "")

    # key  ke matriks 2x2
    key2d = np.zeros((2, 2), dtype=int)
    itr3 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr3]) - 65
            itr3 += 1
    # for

    # mencari determinan
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26

    # mencari invers perkalian
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    # for

    # adjugate matrix
    # swapping
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]

    # changing signs pada matriks
    key2d[0][1] *= -1
    key2d[1][0] *= -1

    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    # mengkalikan invers perkalian matriks dengan adjugate matriks
    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv

    # modulo
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    # cipher to plaintext
    decryp_text = ""
    itr_count = int(len(msg) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    else:
        for i in range(itr_count - 1):
            temp1 = msg2d[0][i] * key2d[0][0] + msg2d[1][i] * key2d[0][1]
            decryp_text += chr((temp1 % 26) + 65)
            temp2 = msg2d[0][i] * key2d[1][0] + msg2d[1][i] * key2d[1][1]
            decryp_text += chr((temp2 % 26) + 65)
            # for
    # if else

    print("Decrypted Text: {}".format(decryp_text))
    #mencetak decrypt pada hill cipher


def main():
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        print("---Encryption---")
        cipher_encryption()
    elif choice == 2:
        print("---Decryption---")
        cipher_decryption()
    else:
        print("Invalid Choice")

if __name__ == "__main__":
    main()

#############################################################################################################
#Enkripsi
#1. Ubah pesan menjadi pasangan 2 baris dan beberapa kolom, jumlah kolom adalah total panjang pesan dibagi 2
#2. Ambil kunci 4 huruf dan ubah menjadi matriks 2x2
#3. Lakukan perkalian matriks antara setiap baris dan kolom pasangan pesan dan matriks kunci 2x2
#4. Ambil modulo 26 dari hasil untuk mendapatkan cipher teks

#Dekripsi
#1. Ubah pesan menjadi pasangan 2 baris dan beberapa kolom, jumlah kolom adalah total panjang pesan dibagi 2
#2. Ambil 4 huruf kunci dan ubah menjadi matriks 2x2
#3. Cari determinan dari matriks kunci
#4. cari invers perkalian dari determinan matriks kunci
#5. cari matriks ajugat dari matriks kunci
#6. kalikan invers perkalian dari determinan dengan matriks ajugasi dan ambil mod 26 dari hasil
#7 Lakukan perkalian matriks antara setiap baris dan kolom pasangan pesan dan matriks kunci 2x2
#8. Ambil modulo 26 dari hasil untuk mendapatkan cipher teks
#############################################################################################################