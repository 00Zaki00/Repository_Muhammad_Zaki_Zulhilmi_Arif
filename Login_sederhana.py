def login():
    valid_username = "Zaki"
    valid_NIM = "2309116077"

   
    username = input("Masukkan username: ")
    password = input("Masukkan NIM: ")

    
    if username == valid_username and password == valid_NIM:
        print("Login berhasil!")
    else:
        print("Login gagal. Username atau NIM salah.")

login()
