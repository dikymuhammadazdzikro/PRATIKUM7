class Person:
    def __init__(self, nama, alamat=""):
        self.nama = nama
        self.alamat = alamat
        self.__umur = 0

    @property
    def umur(self):
        return self.__umur

    @umur.setter
    def umur(self, value):
        self.__umur = value

    def cetak_data(self):
        print(f"Nama  : {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Umur  : {self.__umur}")


class Mahasiswa(Person):
    def __init__(self, nim, nama, alamat=""):
        super().__init__(nama, alamat)
        self.nim = nim
        self.__nilai = 0

    @property
    def nilai(self):
        return self.__nilai

    @nilai.setter
    def nilai(self, value):
        self.__nilai = value

    def cetak(self, tampil_nama=False, tampil_alamat=False):
        print(f"NIM: {self.nim}")
        if tampil_nama:
            print(f"Nama: {self.nama}")
        if tampil_alamat:
            print(f"Alamat: {self.alamat}")

    def cetak_data(self):
        print("\n--- Data Mahasiswa ---")
        print(f"NIM   : {self.nim}")
        print(f"Nama  : {self.nama}")
        print(f"Alamat: {self.alamat}")
        print(f"Umur  : {self.umur}")
        print(f"Nilai : {self.nilai}")


class DaftarNilai:
    def __init__(self):
        self.data = []

    def tambah(self, nim, nama, alamat, umur, nilai):
        mhs = Mahasiswa(nim, nama, alamat)
        mhs.umur = umur
        mhs.nilai = nilai
        self.data.append(mhs)
        print(f"Data mahasiswa '{nama}' berhasil ditambahkan.")

    def tampilkan(self):
        if not self.data:
            print("Belum ada data mahasiswa.")
            return
        for mhs in self.data:
            mhs.cetak_data()

    def hapus(self, nama):
        awal = len(self.data)
        self.data = [mhs for mhs in self.data if mhs.nama != nama]
        akhir = len(self.data)
        if akhir < awal:
            print(f"Data mahasiswa dengan nama '{nama}' berhasil dihapus.")
        else:
            print(f"Data dengan nama '{nama}' tidak ditemukan.")

    def ubah(self, nama, nama_baru=None, alamat=None, umur=None, nilai=None):
        ditemukan = False
        for mhs in self.data:
            if mhs.nama == nama:
                ditemukan = True
                if nama_baru:
                    mhs.nama = nama_baru
                if alamat:
                    mhs.alamat = alamat
                if umur is not None:
                    mhs.umur = umur
                if nilai is not None:
                    mhs.nilai = nilai
        if ditemukan:
            print(f"Data mahasiswa dengan nama '{nama}' berhasil diubah.")
        else:
            print(f"Data dengan nama '{nama}' tidak ditemukan.")


if __name__ == "__main__":
    daftar = DaftarNilai()
    daftar.tambah("1234", "Ari", "Bekasi", 20, 90)
    daftar.tambah("5678", "Dina", "Bandung", 21, 85)
    print("\n== DATA AWAL ==")
    daftar.tampilkan()
    daftar.ubah("Ari", nilai=95)
    print("\n== SETELAH DIUBAH ==")
    daftar.tampilkan()
    daftar.hapus("Dina")
    print("\n== SETELAH DIHAPUS ==")
    daftar.tampilkan()
