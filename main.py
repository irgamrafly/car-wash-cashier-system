print('===== SISTEM KASIR CUCI MOBIL =====')

jam_datang = int(input('Masukkan jam kedatangan (0-24): '))

if jam_datang < 8 or jam_datang > 17:
    print('Maaf, tempat cuci mobil sedang tutup.')

else:
    print('\nPilihan paket: VIP / KILAT')
    pilihan_paket = input('Masukkan paket cuci: ').lower()

    if pilihan_paket == 'vip':
        harga_paket = 70000
        nama_paket = 'Cuci VIP'

    elif pilihan_paket == 'kilat':
        harga_paket = 30000
        nama_paket = 'Cuci Kilat'

    else:
        print('Pilihan tidak dikenal, otomatis menggunakan paket standar.')
        harga_paket = 45000
        nama_paket = 'Cuci Standar'

    tambah_semir = input('Tambah semir ban? (y/t): ').lower()
    biaya_semir = 0

    if tambah_semir == 'y':
        biaya_semir = 10000

    total_bayar = harga_paket + biaya_semir

    print('\n===== STRUK PEMBAYARAN =====')
    print('Jam kedatangan :', jam_datang, ':00')
    print('Paket cuci     :', nama_paket)
    print('Harga paket    : Rp', harga_paket)
    print('Biaya semir    : Rp', biaya_semir)
    print('----------------------------')
    print('Total bayar    : Rp', total_bayar)
    print('Terima kasih telah menggunakan jasa kami!')
