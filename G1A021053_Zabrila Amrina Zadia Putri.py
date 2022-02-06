def pertama():
  print("=======================================")
  print("SELAMAT DATANG DI APLIKASI SHOPEE ")
  print("=======================================")
  
  def welcome():
    print("\nApakah Anda Ingin Melakukan pembelian Secara Online ? ")
    print("1.Ya" "\n2.Tidak")
    awal =input("\nPilihan Anda : ")
    if awal=="1" :
      print("\nSelamat Datang di Aplikasi Shopee ")
    elif awal=="2":
      print("Silahkan meninggalkan Aplikasi Shopee")
      quit()
    else:
      print("input yang anda masukkan salah")
      welcome()
  welcome()
  
  print('')
  Nama=input("Silahkan Masukkan Nama Anda:") 
  Kontak=int(input("Masukkan No HP/WA Anda:"))
 
  
  print("\nPembelian")
  pilihan_pembelian=["1.Elektronik","2.Olahraga",]
  for menu1 in pilihan_pembelian:
    print(menu1,end="\n")

  def pembelian ():
    pembelian =int(input("MASUKAN PILIHAN ANDA :"))
    print("1.KULKAS\n","2.TELEVISI\n","3.SETRIKA\n",)
    pembelian =int(input("MASUKAN PILIHAN ANDA :"))
    if pembelian ==1:
      print("\nSELAMAT ANDA SUDAH MEMESAN PEMBELIAN KULKAS")
    elif pembelian ==2:
      print("\nSELAMAT ANDA SUDAH MEMESAN PEMBELIAN TELEVISI")
    elif pembelian ==3:
      print("\nSELAMAT ANDA SUDAH MEMESAN PEMBELIAN SETRIKA")
    else:
      print("Silahkan Melakukan Pembatalan Pembelian")
      pembelian ()
  pembelian ()
  
  print('')
  print("PILIHAN Pembayaran :")
  pilihan_pembayaran=["1.CASH ON DELIVERY","2.SHOPPE PAY","3.SHOPPE PAY LATER"]
  for menu2 in pilihan_pembayaran:
    print(menu2,end="\n")

  def pembayaran ():
    Pilihan_pembayaran=int(input("\nSilahkan Memasukkan Pembayaran Pilihan Anda :"))
    if Pilihan_pembayaran==1:
      print("=============================")
      print("Anda telah Melakukan Pembayaran Secara Cash On Delivery")
      print("Silahkan Lanjutkan Proses Pembayaran")
      print("=============================")
    elif Pilihan_pembayaran==2:
      print("===============================")
      print("Anda telah Melakukan Pembayaran Secara Shoppe Pay")
      print("Silahkan Lanjutkan Proses Pembayaran")
      print("===============================")
    elif Pilihan_pembayaran==3:
      print("===============================")
      print("Anda telah Melakukan Pembayaran Secara Shoppe Pay Later")
      print("Silahkan Lanjutkan Proses Pembayaran")
      print("===============================")
    else:
      print("Input yang anda masukkan salah")
      pembayaran ()
  pembayaran ()

  def last():
    print("")
    print("Silahkan Melakukan Proses Pembayaran")
    print("1.Ya \n2.Tidak")
    Again =input("\nPilihan Anda : ")
    if Again=="1":
      print("\n=======TERIMA KASIH TELAH MELAKUKAN PEMESANAN SECARA ONLINE=======")
      quit()
    elif Again=="2":
      pertama()
      
    else:
      print("input yang anda masukkan salah")
      last()
  last()

pertama()