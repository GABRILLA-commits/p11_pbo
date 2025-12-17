# Analisis Pelanggaran Prinsip SOLID  
## Praktikum 11 – Refactoring Struktur Kode

## Deskripsi Singkat
analisis pelanggaran prinsip SOLID pada kode awal (sebelum refactoring)
dalam studi kasus Sistem Validasi Registrasi Mahasiswa. Analisis difokuskan pada
pelanggaran Single Responsibility Principle (SRP), Open/Closed Principle (OCP),
dan Dependency Inversion Principle (DIP).

---

## Pelanggaran Single Responsibility Principle (SRP)
Pada kode ini sebelum refactoring, class ValidatorManager menangani lebih dari satu
tanggung jawabb, yaitu validasi jumlah SKS dan validasi prasyarat mata kuliah dalam satu
method. Hal ini melanggar prinsip SRP karena satu class seharusnya hanya memiliki satu
alasan untuk berubah. kalau salah satu aturan validasi berubah, maka class yang sama
harus dimodifikasi, sehingga kode menjadi sulit dirawat dan dikembangkan.

---

## Pelanggaran Open/Closed Principle (OCP)
Kode awal menggunakan struktur if/else untuk menentukan aturan validasi.
Ketika kita ingin menambahkan aturan validasi baru, seperti validasi IPK, maka method
validate() harus diubah dengan menambahkan kondisi baru. Hal ini melanggar prinsip OCP
karena class tidak tertutup terhadap modifikasi dan tidak terbuka untuk ekstensi.

---

## Pelanggaran Dependency Inversion Principle (DIP)
Class ValidatorManager pada kode awal bergantung langsung pada implementasi konkret
aturan validasi, bukan pada abstraksi ya. Tidak terdapat interface atau abstract class
sebagai kontrak validasi. Akibatnya, modul tingkat tinggi bergantung pada modul tingkat
rendah, sehingga sistem menjadi kaku dan sulit dikembangkan.

---

## Kesimpulan
Kode sebelum refactoring ini mengandung Code Smell berupa penggabungan tanggung jawab
dalam satu class dan penggunaan if/else yang berlebihan. nah Pelanggaran terhadap prinsip
SRP, OCP, dan DIP ini menjadi alasan utama dilakukannya refactoring menggunakan prinsip
SOLID dan Dependency Injection agar kode menjadi lebih modular, fleksibel, dan mudah
dipelihara.

---

## Identitas Mahasiswa
Nama  : Gabrilla aszahra samad 
NIM   : 2411102441174
Kelas : B
