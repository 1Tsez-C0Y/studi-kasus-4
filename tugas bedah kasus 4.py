produk = {
    'nama' : 'mizone',
    'harga' : '5.000',
    'stok' : '15'
    }


while True :
    print('==sistem manajemen stok produk==')
    print('1. tampilkan data')
    print('2. tambah kategori')
    print('3. ubah harga')
    print('4. hapus kategori')
    print('5. leave')
    
    pil = input('pilih menu :')
    
    if pil == '1' :
        print('nama  :', produk['nama'])
        print('harga :', produk['harga'])
        print('stok  :', produk['stok'])
        if 'kategori' in produk:
            print('kategori :', produk['kategori'])
        
    elif pil == '2' :
        kategorinew = input('masukan kategori :',)
        produk ['kategori'] = kategorinew
        print('kategori sudah ditambah')
        print('data diperbarui :', produk)
        
    elif pil == '3' :
        harganew = input('masukan harga :')
        produk ['harga'] = harganew
        print('data dperbarui', produk)
        
    elif pil == '4' :
        produk.pop('kategori')
        print('kategori berhasil dihapus')
        print('data diperbarui :', produk)
        
    elif pil == '5' :
        print('keluar dari sistem')
        break
    else :
        print('pilihan tidak valid')
