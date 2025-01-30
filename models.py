from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    roles = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
class Bidang(db.Model):
    __tablename__ = 'bidang'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_bidang = db.Column(db.String(100), nullable=False)
    nama_produk = db.Column(db.String(100), nullable=False)
    deskripsi_produk = db.Column(db.Text)
    spesifikasi = db.Column(db.String(255))
    kegiatan = db.Column(db.String(100))
    kode_produksi = db.Column(db.String(50))
    harga = db.Column(db.Integer)
    jumlah = db.Column(db.Integer)
    status = db.Column(db.String(50))
    pesan_status = db.Column(db.Text)
    tanggal_pengajuan = db.Column(db.Date)
    tanggal_respon = db.Column(db.Date)

    def __repr__(self):
        return f'<Bidang {self.nama_bidang}>'

class Sekretariat(db.Model):
    __tablename__ = 'sekretariat'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_sekretariat = db.Column(db.String(100), nullable=False)
    nama_produk = db.Column(db.String(100), nullable=False)
    deskripsi_produk = db.Column(db.Text)
    spesifikasi = db.Column(db.String(255))
    kegiatan = db.Column(db.String(100))
    kode_produksi = db.Column(db.String(50))
    harga = db.Column(db.Integer)
    jumlah = db.Column(db.Integer)
    status = db.Column(db.String(50))
    pesan_status = db.Column(db.Text)
    tanggal_pengajuan = db.Column(db.Date)
    tanggal_respon = db.Column(db.Date)

    def __repr__(self):
        return f'<Sekretariat {self.nama_bidang}>'

class Pesan(db.Model):
    __tablename__ = 'pesan'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_bidang = db.Column(db.String(100))
    perihal = db.Column(db.String(100))
    deskripsi = db.Column(db.Text)
    status = db.Column(db.String(50))

    def __repr__(self):
        return f'<Pesan {self.perihal}>'

class StokBarang(db.Model):
    __tablename__ = 'stok_barang'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nama_gudang = db.Column(db.String(100))
    nama_produk = db.Column(db.String(100))
    deskripsi_produk = db.Column(db.Text)
    spesifikasi = db.Column(db.String(255))
    kegiatan = db.Column(db.String(100))
    kode_produksi = db.Column(db.String(50))
    harga = db.Column(db.Integer)
    jumlah = db.Column(db.Integer)

    def __repr__(self):
        return f'<StokBarang {self.nama_gudang}>'
