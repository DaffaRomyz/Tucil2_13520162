# Tucil2_13520162
Tugas Kecil 2 IF2211 Strategi Algoritma
Semester 2 tahun 2021/2022
Implementasi Convex Hull untuk Visualisasi Tes Linear Separability Dataset dengan Algoritma Divide and Conquer

## Deskripsi Program
Program menerima data 2 dimensi dari packages `sklearn` dan mengembalikan _convex hull_.
Himpunan titik pada bidang planar disebut _convex_ jika untuk sembarang dua titik pada bidang tersebut (misal p dan q), seluruh segmen garis yang berakhir di p dan q berada pada himpunan tersebut.
Program akan mengembalikan convex hull dari setiap label berupa list data pembentuk convex hull, 
lalu menampilkannya dengan warna yang berbeda.

## Requirements
* Packages :
	* numpy
	* pandas
	* sklearn
	* matplotlib
	* math

## Langkah Menggunakan Program
1. Install seluruh Requirements
2. Pada directory src lakukan perintah `python main.py`
3. Program akan meminta pilihan data `1` untuk iris, `2` untuk wine, `3` untuk breast_cancer
4. Program akan meminta pilihan untuk menyimpan grafik data pada folder bin. `y` untuk iya. `n` untuk tidak
5. Program akan meminta pilihan untuk menunjukan grafik pada layar.  `y` untuk iya. `n` untuk tidak
 
## Author
| Nama | NIM | Email |
| ----- | --- | ----------|
|Daffa Romyz Aufa | 13520162 | <13520162@std.stei.itb.ac.id> |