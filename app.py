from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import flash
from models import db, User, Bidang, Sekretariat, Pesan, StokBarang
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = 'eperkap'

# Konfigurasi Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dbeperkap'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi SQLAlchemy dengan aplikasi Flask
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

       # Validasi pengguna
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['loggedin'] = True
            session['id'] = user.id
            session['username'] = user.username
            session['roles'] = user.roles
            return redirect('/home')
        else:
            return render_template('index.html', error="Username atau password salah.")

    return render_template('index.html')

@app.route('/home')
def home():
    if 'loggedin' in session:
        roles = session['roles']
        if roles == 'Subbag Peralatan dan Perlengkapan':
            return render_template('home-admin.html', roles=roles)
        else:
            return render_template('home.html', roles=roles)
    return redirect('/')


@app.route('/homeadmin')
def homeadmin():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')
        return render_template('home-admin.html', roles=roles)
    return redirect('/')

@app.route('/produkditerima')
def produk_diterima():
    if 'loggedin' in session and session.get('roles') == 'Subbag Peralatan dan Perlengkapan':
        # Ambil data dari tabel bidang dan sekretariat
        bidang_data = db.session.query(Bidang).filter_by(status="Diterima").all()
        sekretariat_data = db.session.query(Sekretariat).filter_by(status="Diterima").all()
        
        # Gabungkan data bidang dan sekretariat
        produk_diterima_data = bidang_data + sekretariat_data

        # Daftar nama_bidangs tetap untuk filter
        nama_bidangs = [
            "Bidang Ketentraman dan Ketertiban Umum",
            "Bidang Pengawasan dan Pengendalian Tempat Usaha",
            "Bidang Perlindungan Masyarakat",
            "Bidang Penegakan Perdan dan Perkada",
            "Bidang PPNS"
        ]

        # Kirim data ke template
        return render_template(
            'produkditerima.html', 
            roles=session.get('roles'), 
            produk_diterima_data=produk_diterima_data,
            nama_bidangs=nama_bidangs
        )
    return redirect('/')


@app.route('/produkditolak')
def produk_ditolak():
    if 'loggedin' in session and session.get('roles') == 'Subbag Peralatan dan Perlengkapan':
        # Fetch data from 'bidang' and 'sekretariat' with status "Ditolak"
        bidang_data = db.session.query(Bidang).filter_by(status="Ditolak").all()
        sekretariat_data = db.session.query(Sekretariat).filter_by(status="Ditolak").all()

        # Combine data for rendering
        produk_ditolak_data = bidang_data + sekretariat_data

        # Predefined bidang names for filter
        nama_bidangs = [
            "Bidang Ketentraman dan Ketertiban Umum",
            "Bidang Pengawasan dan Pengendalian Tempat Usaha",
            "Bidang Perlindungan Masyarakat",
            "Bidang Penegakan Perdan dan Perkada",
            "Bidang PPNS"
        ]

        # Pass data to template
        return render_template(
            'produkditolak.html',
            roles=session.get('roles'),
            produk_ditolak_data=produk_ditolak_data,
            nama_bidangs=nama_bidangs
        )
    return redirect('/')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/unauthorized')
def unauthorized():
    return render_template('unauthorized.html'), 403


@app.route('/bidang')
def bidang():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')

        if roles != 'Subbag Peralatan dan Perlengkapan':
            return redirect(url_for('bidangrequest'))
    
    # Menghitung jumlah pending requests untuk setiap bidang
        nama_bidangs = [
            "Bidang Ketentraman dan Ketertiban Umum",
            "Bidang Pengawasan dan Pengendalian Tempat Usaha",
            "Bidang Perlindungan Masyarakat",
            "Bidang Penegakan Perdan dan Perkada",
            "Bidang PPNS"
        ]
        pending_requests = {
            nama_bidang: Bidang.query.filter_by(nama_bidang=nama_bidang, status='Diproses').count()
            for nama_bidang in nama_bidangs
        }

        return render_template('main-bidang.html', roles=roles, pending_requests=pending_requests, enumerate=enumerate)

    return redirect('/')

@app.route('/bidangchecking/<nama_bidang>')
def bidangchecking(nama_bidang):
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')
        if roles == 'Subbag Peralatan dan Perlengkapan':
            # Filter data berdasarkan nama_bidang dan status 'Diproses'
            assets = Bidang.query.filter_by(nama_bidang=nama_bidang, status='Diproses').all()
            return render_template('bidang-checking.html', roles=roles, assets=assets, nama_bidang=nama_bidang, enumerate=enumerate)
    return redirect('/')

@app.route('/update_status/<int:id>', methods=['POST'])
def update_status(id):
    asset = Bidang.query.get(id)
    if asset:
        asset.status = request.form['status']
        asset.pesan_status = request.form['pesan_status']
        asset.tanggal_respon = datetime.now().strftime('%Y-%m-%d')
        db.session.commit()
        
        #  Ambil nama_bidang dari form untuk redirect
        nama_bidang = request.form.get('nama_bidang')
        if not nama_bidang:
            flash("Gagal mengupdate status, nama_bidang tidak ditemukan.", "danger")
            return redirect('/')
        return redirect(url_for('bidangchecking', nama_bidang=nama_bidang))
    flash("Data aset tidak ditemukan.", "danger")
    return redirect('/')

@app.route('/bidangrequest', methods=['GET', 'POST'])
def bidangrequest():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')

        # Ambil data aset yang sesuai dengan nama_bidang
        assets = Bidang.query.filter_by(nama_bidang=roles).all()

        if request.method == 'POST':
            # Tambah Produk Baru
            nama_produk = request.form['nama_produk']
            deskripsi_produk = request.form['deskripsi_produk']
            spesifikasi = request.form['spesifikasi']
            kegiatan = request.form['kegiatan']
            kode_produksi = request.form['kode_produksi']
            harga_raw = request.form['harga']
            harga = int(harga_raw.replace(',', ''))
            jumlah = request.form['jumlah']

            # Buat record baru
            new_asset = Bidang(
                nama_bidang=roles,
                nama_produk=nama_produk,
                deskripsi_produk=deskripsi_produk,
                spesifikasi=spesifikasi,
                kegiatan=kegiatan,
                kode_produksi=kode_produksi,
                harga=harga,
                jumlah=jumlah,
                status="Diproses",
                tanggal_pengajuan=datetime.now(),
                tanggal_respon=None
            )
            db.session.add(new_asset)
            db.session.commit()
            return redirect(url_for('bidangrequest'))

        return render_template('bidang-request.html', roles=roles, assets=assets)

    return redirect('/')

@app.route('/update_produk/<int:id>', methods=['POST'])
def update_produk(id):
    asset = Bidang.query.get(id)
    if asset:
        asset.nama_produk = request.form['nama_produk']
        asset.deskripsi_produk = request.form['deskripsi_produk']
        asset.spesifikasi = request.form['spesifikasi']
        asset.kegiatan = request.form['kegiatan']
        asset.kode_produksi = request.form['kode_produksi']
        harga_raw = request.form['harga']
        asset.harga = int(harga_raw.replace(',', ''))
        asset.jumlah = request.form['jumlah']
        db.session.commit()
    return redirect(url_for('bidangrequest'))

@app.route('/delete_produk/<int:id>', methods=['POST'])
def delete_produk(id):
    asset = Bidang.query.get(id)
    if asset:
        db.session.delete(asset)
        db.session.commit()
    return redirect(url_for('bidangrequest'))

@app.route('/sekretariat')
def sekretariat():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')

        if roles != 'Subbag Peralatan dan Perlengkapan':
            return redirect(url_for('sekretariatrequest'))

        nama_sekretariats = [
            "Subbagian Umum",
            "Subbagian Program, Pelaporan, dan Keuangan",
            "Subkelompok Kepegawaian"
        ]

        pending_requests = {
            nama_sekretariat: Sekretariat.query.filter_by(nama_sekretariat=nama_sekretariat, status='Diproses').count()
            for nama_sekretariat in nama_sekretariats
        }
        return render_template('main-sekretariat.html', roles=roles, pending_requests=pending_requests, enumerate=enumerate)
    return redirect('/')

@app.route('/sekretariatrequest', methods=['GET', 'POST'])
def sekretariatrequest():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')

        # Ambil parameter nama_sekretariat dari URL
        nama_sekretariat = request.args.get('nama_sekretariat', roles)

        # Query data berdasarkan nama_sekretariat
        assets = Sekretariat.query.filter_by(nama_sekretariat=nama_sekretariat).all()

        if request.method == 'POST':
            # Tambah Produk Baru
            nama_produk = request.form['nama_produk']
            deskripsi_produk = request.form['deskripsi_produk']
            spesifikasi = request.form['spesifikasi']
            kegiatan = request.form['kegiatan']
            kode_produksi = request.form['kode_produksi']
            harga_raw = request.form['harga']
            harga = int(harga_raw.replace(',', ''))
            jumlah = request.form['jumlah']

            # Buat record baru
            new_asset = Sekretariat(
                nama_sekretariat=roles,
                nama_produk=nama_produk,
                deskripsi_produk=deskripsi_produk,
                spesifikasi=spesifikasi,
                kegiatan=kegiatan,
                kode_produksi=kode_produksi,
                harga=harga,
                jumlah=jumlah,
                status="Diproses",
                tanggal_pengajuan=datetime.now(),
                tanggal_respon=None
            )
            db.session.add(new_asset)
            db.session.commit()
            return redirect(url_for('sekretariatrequest', nama_sekretariat=roles))
        
        return render_template('sekretariat-request.html', roles=roles, assets=assets)
    return redirect('/')

@app.route('/update_produk_sekre/<int:id>', methods=['POST'])
def update_produk_sekre(id):
    asset = Sekretariat.query.get(id)
    if asset:
        asset.nama_produk = request.form['nama_produk']
        asset.deskripsi_produk = request.form['deskripsi_produk']
        asset.spesifikasi = request.form['spesifikasi']
        asset.kegiatan = request.form['kegiatan']
        asset.kode_produksi = request.form['kode_produksi']
        harga_raw = request.form['harga']
        asset.harga = int(harga_raw.replace(',', ''))
        asset.jumlah = request.form['jumlah']
        db.session.commit()
    return redirect(url_for('sekretariatrequest'))

@app.route('/delete_produk_sekre/<int:id>', methods=['POST'])
def delete_produk_sekre(id):
    asset = Sekretariat.query.get(id)
    if asset:
        db.session.delete(asset)
        db.session.commit()
    return redirect(url_for('sekretariatrequest'))

@app.route('/sekretariatchecking/<nama_sekretariat>')
def sekretariatchecking(nama_sekretariat):
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')
        if roles == 'Subbag Peralatan dan Perlengkapan':
            assets = Sekretariat.query.filter_by(nama_sekretariat=nama_sekretariat, status='Diproses').all()
            return render_template('sekretariat-checking.html', roles=roles, assets=assets, nama_sekretariat=nama_sekretariat, enumerate=enumerate)
    return redirect('/')

@app.route('/update_status_sekre/<int:id>', methods=['POST'])
def update_status_sekre(id):
    asset = Sekretariat.query.get(id)
    if asset:
        asset.status = request.form['status']
        asset.pesan_status = request.form['pesan_status']
        asset.tanggal_respon = datetime.now().strftime('%Y-%m-%d')
        db.session.commit()
        
        #  Ambil nama_bidang dari form untuk redirect
        nama_sekretariat = request.form.get('nama_sekretariat')
        if not nama_sekretariat:
            flash("Gagal mengupdate status, nama_sekretariat tidak ditemukan.", "danger")
            return redirect('/')
        return redirect(url_for('sekretariatchecking', nama_sekretariat=nama_sekretariat))
    flash("Data aset tidak ditemukan.", "danger")
    return redirect('/')

@app.route('/pesan', methods=['GET', 'POST'])
def pesan():
    if 'loggedin' in session and session['roles'] == 'Subbag Peralatan dan Perlengkapan':
        roles = session.get('roles', 'Pengguna')

        if request.method == 'POST':
            # Ambil data dari form
            row_id = request.form.get('rowId')
            new_status = request.form.get('status')

            # Update status pada database
            pesan_to_update = Pesan.query.get(row_id)
            if pesan_to_update:
                pesan_to_update.status = new_status
                db.session.commit()
                flash('Status berhasil diperbarui!', 'success')
            else:
                flash('Data tidak ditemukan.', 'danger')

        # Ambil semua data pesan dari database
        daftar_pesan = Pesan.query.all()
        return render_template('pesan.html', roles=roles, daftar_pesan=daftar_pesan, enumerate=enumerate)
    
    return redirect('/')


@app.route('/stok-barang')
def stok_barang():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')
        return render_template('stokbarang.html', roles=roles)
    return redirect('/')

@app.route('/stokbarang_detail/<string:nama_gudang>', methods=['GET', 'POST'])
def stokbarang_detail(nama_gudang):
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')

        # Tambahkan stok barang baru
        if request.method == 'POST':
            action = request.form.get('action')
            if action == 'add':
                new_stok = StokBarang(
                    nama_gudang=nama_gudang,
                    nama_produk=request.form['nama_produk'],
                    deskripsi_produk=request.form['deskripsi_produk'],
                    spesifikasi=request.form['spesifikasi'],
                    kegiatan=request.form['kegiatan'],
                    kode_produksi=request.form['kode_produksi'],
                    harga=request.form['harga'],
                    jumlah=request.form['jumlah']
                )
                db.session.add(new_stok)
                db.session.commit()
                flash("Stok barang berhasil ditambahkan!", "success")

            # Edit stok barang
            elif action == 'edit':
                stok_id = request.form['stok_id']
                stok = StokBarang.query.get(stok_id)
                if stok:
                    stok.nama_produk = request.form['nama_produk']
                    stok.deskripsi_produk = request.form['deskripsi_produk']
                    stok.spesifikasi = request.form['spesifikasi']
                    stok.kegiatan = request.form['kegiatan']
                    stok.kode_produksi = request.form['kode_produksi']
                    stok.harga = request.form['harga']
                    stok.jumlah = request.form['jumlah']
                    db.session.commit()
                    flash("Stok barang berhasil diperbarui!", "success")

            # Hapus stok barang
            elif action == 'delete':
                stok_id = request.form['stok_id']
                stok = StokBarang.query.get(stok_id)
                if stok:
                    db.session.delete(stok)
                    db.session.commit()
                    flash("Stok barang berhasil dihapus!", "success")

        # Ambil stok berdasarkan gudang
        stok_list = StokBarang.query.filter_by(nama_gudang=nama_gudang).all()
        return render_template('stokbarang-detail.html', roles=roles, stok_list=stok_list, nama_gudang=nama_gudang)

    return redirect('/')


@app.route('/hubungiperkap')
def hubungiperkap():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')
        return render_template('main-hubungiperkap.html', roles=roles)
    return redirect('/')

@app.route('/kirim_aduan', methods=['POST'])
def kirim_aduan():
    if 'loggedin' in session:
        nama_bidang = request.form.get('nama_bidang')
        perihal = request.form.get('perihal')
        deskripsi = request.form.get('deskripsi')

        if nama_bidang and perihal and deskripsi:
            # Simpan data ke database
            aduan = Pesan(
                nama_bidang=nama_bidang,
                perihal=perihal,
                deskripsi=deskripsi,
                status='Diproses'  # Default status
            )
            db.session.add(aduan)
            db.session.commit()

            flash('Aduan berhasil dikirim.', 'success')
            return redirect(url_for('hubungiperkap'))
        else:
            flash('Semua kolom harus diisi.', 'danger')
            return redirect(url_for('hubungiperkap'))

    flash('Anda harus login terlebih dahulu.', 'danger')
    return redirect('/')

@app.route('/daftar-aduan')
def daftar_aduan():
    if 'loggedin' in session:
        roles = session.get('roles', 'Pengguna')
        daftar_pesan = Pesan.query.filter_by(nama_bidang=roles).all()
        return render_template('daftar_aduan.html', roles=roles, daftar_pesan=daftar_pesan, enumerate=enumerate)
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Membuat tabel jika belum ada
    app.run(debug=True)
