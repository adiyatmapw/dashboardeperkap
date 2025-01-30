-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2025 at 11:16 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbeperkap`
--

-- --------------------------------------------------------

--
-- Table structure for table `bidang`
--

CREATE TABLE `bidang` (
  `id` int(11) NOT NULL,
  `nama_bidang` varchar(100) NOT NULL,
  `nama_produk` varchar(100) NOT NULL,
  `deskripsi_produk` longtext DEFAULT NULL,
  `spesifikasi` varchar(255) DEFAULT NULL,
  `kegiatan` varchar(100) DEFAULT NULL,
  `kode_produksi` varchar(50) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `pesan_status` longtext DEFAULT NULL,
  `tanggal_pengajuan` date DEFAULT NULL,
  `tanggal_respon` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bidang`
--

INSERT INTO `bidang` (`id`, `nama_bidang`, `nama_produk`, `deskripsi_produk`, `spesifikasi`, `kegiatan`, `kode_produksi`, `harga`, `jumlah`, `status`, `pesan_status`, `tanggal_pengajuan`, `tanggal_respon`) VALUES
(5, 'Bidang Ketentraman dan Ketertiban Umum', 'PC', 'PC ini digunakan untuk operasional Satpol PP DKI Jakarta', 'ACER VERITON X - CORE I7 (VX/0037)', 'Operasional', 'PC001', 24220000, 10, 'Diproses', NULL, '2024-12-14', NULL),
(6, 'Bidang Ketentraman dan Ketertiban Umum', 'Meja', 'Meja untuk operasional office Satpol PP DKI Jakarta', 'MEJA KERJA UPT 1-000-0231-24', 'Operasional', 'OFTBL001', 15847000, 30, 'Diproses', NULL, '2024-12-14', NULL),
(9, 'Bidang Pengawasan dan Pengendalian Tempat Usaha', 'PC', 'PC digunakan untuk operasional Satpol PP DKI Jakarta', 'ACER VERITON X - CORE I7 (VX/0037)', 'Operasional', 'PC002', 24220000, 10, 'Diproses', NULL, '2024-12-16', NULL),
(10, 'Bidang Perlindungan Masyarakat', 'Printer', 'Printer digunakan untuk operasional Satpol PP DKI Jakarta', 'CANON MF 643CDW', 'Operasional', 'PRINTER002', 10060000, 15, 'Diproses', NULL, '2024-12-16', NULL),
(11, 'Bidang Penegakan Perdan dan Perkada', 'PC', 'Lorem Ipsum', 'ACER VERITON X - CORE I7 (VX/0037)', 'Operasional', 'PC003', 24220000, 10, 'Diproses', NULL, '2024-12-16', NULL),
(12, 'Bidang Penegakan Perdan dan Perkada', 'Printer', 'lOREM IPSIUM', 'CANON MF 643CDW', 'Operasional', 'PRINTER003', 10060000, 20, 'Diproses', NULL, '2024-12-16', NULL),
(13, 'Bidang Penegakan Perdan dan Perkada', 'Meja', 'Lorem Ipsum', 'MEJA KERJA UPT 1-000-0231-24', 'Operasional', 'OFTBL002', 15847000, 30, 'Diterima', 'sudah oke', '2024-12-16', '2024-12-16'),
(14, 'Bidang PPNS', 'PC', 'Lorem Ipspum', 'ACER VERITON X - CORE I7 (VX/0037)', 'Operasional', 'PC005', 24220000, 10, 'Diproses', NULL, '2024-12-16', NULL),
(15, 'Bidang PPNS', 'Printer', 'Lorem ipsuhm', 'CANON MF 643CDW', 'Operasional', 'PRINTER005', 10060000, 20, 'Diproses', NULL, '2024-12-16', NULL),
(16, 'Bidang PPNS', 'Meja', 'lorem ipsum', 'MEJA KERJA UPT 1-000-0231-24', 'Operasional', 'OFTBL003', 15847000, 30, 'Diproses', NULL, '2024-12-16', NULL),
(18, 'Bidang Ketentraman dan Ketertiban Umum', 'veleg mobil', 'ban untuk bergerak', 'm160x75', 'Ambil massa', '120', 13000, 1, 'Diproses', NULL, '2025-01-13', NULL),
(19, 'Bidang Ketentraman dan Ketertiban Umum', 'timur', 'berguna', 'flesibel', 'kuliah', '0021', 50000, 1, 'Diproses', NULL, '2025-01-13', NULL),
(20, 'Bidang Ketentraman dan Ketertiban Umum', 'tongkat listrik', 'tongkat unt strum maling', 'mudah di bawa', 'menangkap maling', '0205022', 1000000, 1, 'Diproses', NULL, '2025-01-13', NULL),
(21, 'Bidang Ketentraman dan Ketertiban Umum', 'tongkat listrik', 'tongkat unt strum maling', 'mudah di bawa', 'menangkap maling', '0205022', 1000000, 1, 'Diproses', NULL, '2025-01-13', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `pesan`
--

CREATE TABLE `pesan` (
  `id` int(11) NOT NULL,
  `nama_bidang` varchar(100) DEFAULT NULL,
  `perihal` varchar(100) DEFAULT NULL,
  `deskripsi` longtext DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pesan`
--

INSERT INTO `pesan` (`id`, `nama_bidang`, `perihal`, `deskripsi`, `status`) VALUES
(1, 'Bidang Ketentraman dan Ketertiban Umum', 'Permintaan', 'Just wanna saying Hi!', 'Ditolak'),
(2, 'Bidang Ketentraman dan Ketertiban Umum', 'Permintaan', 'Hiii again', 'Selesai'),
(3, 'Bidang Ketentraman dan Ketertiban Umum', 'Permintaan', 'hi lagi', 'Diproses'),
(4, 'Bidang Ketentraman dan Ketertiban Umum', 'komputer', 'komputer kurang', 'Ditolak');

-- --------------------------------------------------------

--
-- Table structure for table `sekretariat`
--

CREATE TABLE `sekretariat` (
  `id` int(11) NOT NULL,
  `nama_sekretariat` varchar(100) NOT NULL,
  `nama_produk` varchar(100) NOT NULL,
  `deskripsi_produk` longtext DEFAULT NULL,
  `spesifikasi` varchar(255) DEFAULT NULL,
  `kegiatan` varchar(100) DEFAULT NULL,
  `kode_produksi` varchar(50) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `pesan_status` longtext DEFAULT NULL,
  `tanggal_pengajuan` date DEFAULT NULL,
  `tanggal_respon` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sekretariat`
--

INSERT INTO `sekretariat` (`id`, `nama_sekretariat`, `nama_produk`, `deskripsi_produk`, `spesifikasi`, `kegiatan`, `kode_produksi`, `harga`, `jumlah`, `status`, `pesan_status`, `tanggal_pengajuan`, `tanggal_respon`) VALUES
(1, 'Subbagian Umum', 'PC', 'Lorem ipsum loreap simasum', 'ACER VERITON X - CORE I7 (VX/0037)', 'Operasional', '2020', 24220000, 10, 'Diproses', NULL, '2024-12-17', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `stok_barang`
--

CREATE TABLE `stok_barang` (
  `id` int(11) NOT NULL,
  `nama_gudang` varchar(100) DEFAULT NULL,
  `nama_produk` varchar(100) DEFAULT NULL,
  `deskripsi_produk` longtext DEFAULT NULL,
  `spesifikasi` varchar(255) DEFAULT NULL,
  `kegiatan` varchar(100) DEFAULT NULL,
  `kode_produksi` varchar(50) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  `jumlah` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stok_barang`
--

INSERT INTO `stok_barang` (`id`, `nama_gudang`, `nama_produk`, `deskripsi_produk`, `spesifikasi`, `kegiatan`, `kode_produksi`, `harga`, `jumlah`) VALUES
(4, 'Gudang Basement 2', 'Tinta/Toner Printer', 'Lorem ipsum lorem ipsum Tinta warna hitam, biru, merah, dan putih', 'HP 26A [CF226A]', 'Operasional', '2018', 5000000, 10),
(5, 'Gudang Basement 2', 'Printer', 'lorem ipsunm printer adalah barang untuk mencetak sesuatu.', 'CANON MF 643CDW', 'Operasional', '2020', 10060000, 20),
(6, 'Gudang Basement 2', 'Meja', 'Meja adalah barang untuk meletakkan benda atau kebutuhan operasional lainnya.', 'MEJA LERJA UPT 1-000-0231-24', 'Operasional', '2022', 25034000, 30),
(7, 'Gudang Cakung', 'Tinta/Toner Printer', 'Lorem ipsum lorem ipsum Tinta warna hitam, biru, merah, dan putih', 'HP 26A [CF226A]', 'Operasional', '2018', 5000000, 10),
(8, 'Gudang Cakung', 'Printer', 'lorem ipsunm printer adalah barang untuk mencetak sesuatu.', 'CANON MF 643CDW', 'Operasional', '2020', 10060000, 20),
(9, 'Gudang Cakung', 'Meja', 'Meja adalah barang untuk meletakkan benda atau kebutuhan operasional lainnya.', 'MEJA LERJA UPT 1-000-0231-24', 'Operasional', '2022', 25034000, 30),
(11, 'Gudang Basement 1', 'Sofa Ruang Tunggu', 'Sofa yang diperuntukan untuk tamu yang sedang menunggu', 'Sofa untuk 4 orang', 'Untuk tamu menunggu', '2023', 13000000, 2);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `roles` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `roles`) VALUES
(1, 'admin', 'admin123', 'Subbag Peralatan dan Perlengkapan'),
(2, 'user1', 'user123', 'Bidang Ketentraman dan Ketertiban Umum'),
(3, 'user2', 'user123', 'Bidang Pengawasan dan Pengendalian Tempat Usaha'),
(4, 'user3', 'user123', 'Bidang Perlindungan Masyarakat'),
(5, 'user4', 'user123', 'Bidang Penegakan Perdan dan Perkada'),
(6, 'user5', 'user123', 'Bidang PPNS'),
(7, 'user6', 'user123', 'Subbagian Umum'),
(8, 'user7', 'user123', 'Subbagian Program, Pelaporan, dan Keuangan'),
(9, 'user8', 'user123', 'Subkelompok Kepegawaian');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bidang`
--
ALTER TABLE `bidang`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pesan`
--
ALTER TABLE `pesan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sekretariat`
--
ALTER TABLE `sekretariat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stok_barang`
--
ALTER TABLE `stok_barang`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bidang`
--
ALTER TABLE `bidang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `pesan`
--
ALTER TABLE `pesan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `sekretariat`
--
ALTER TABLE `sekretariat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `stok_barang`
--
ALTER TABLE `stok_barang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
