#login
def login_akun() :
    import csv

    akun =[]
    with open('My-Property\perbarui_data\Akun.csv') as csv_file :
        csv_reader = csv.reader(csv_file, delimiter=';')
        for i in csv_reader:
            akun.append(i)
    label = akun.pop(0)

    username = input('Masukkan Username = ')
    password = input('Masukkan Password = ')

    for i in range(len(akun)) :
        if username == akun[i][0] :
            if password == akun[i][1] :
                print('Login Berhasil')
            else :
                print('Password Yang Anda Masukkan Salah')
        else :
            print('Username Tidak Tersedia')
        break
    return
