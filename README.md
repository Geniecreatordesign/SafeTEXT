
              SafeText  -  SecureText

                   R E A D M E


SafeText - Secure Text Encryption and Decryption Tool

SafeText adalah alat untuk mengenkripsi dan mendekripsi teks secara aman menggunakan enkripsi AES-256, yang dilengkapi dengan kode unik untuk setiap proses enkripsi. Alat ini juga menyediakan fungsionalitas untuk mengatur sandi yang aman menggunakan PBKDF2.

Fitur

Enkripsi dan dekripsi teks menggunakan AES-256.

Menyediakan kode unik untuk setiap teks yang dienkripsi.

Memastikan keamanan dengan penggunaan password untuk enkripsi dan dekripsi.

Dapat digunakan di terminal atau command prompt.



---

Instalasi

1. Pastikan Anda memiliki Python 3.x terinstal di sistem Anda.

2. Instal dependensi

SafeText membutuhkan beberapa pustaka Python. Untuk menginstalnya, jalankan perintah berikut:

pip install cryptography colorama

3. Jalankan SafeText

Setelah instalasi, Anda dapat menjalankan SafeText melalui terminal dengan perintah berikut:

python safetext.py


---

Penggunaan

Enkripsi Teks

1. Pilih menu 1 untuk mengenkripsi teks.


2. Masukkan teks yang ingin dienkripsi.


3. Masukkan kata sandi untuk enkripsi.


4. SafeText akan menghasilkan teks terenkripsi beserta kode unik yang dapat digunakan untuk dekripsi nanti.



Dekripsi Teks

1. Pilih menu 2 untuk mendekripsi teks.


2. Masukkan teks terenkripsi dan kode unik yang diberikan pada saat enkripsi.


3. Masukkan kata sandi untuk dekripsi.


4. SafeText akan menampilkan teks asli setelah dekripsi berhasil.



Keluar

1. Pilih menu 3 untuk keluar dari aplikasi.




---

Detail Fungsionalitas

1. Fungsi adjust_border()

Fungsi ini menyesuaikan panjang border berdasarkan lebar terminal.

2. Fungsi generate_unique_code()

Fungsi ini menghasilkan kode unik 5 karakter untuk setiap proses enkripsi.

3. Fungsi derive_key()

Fungsi ini menggunakan PBKDF2 untuk menghasilkan kunci AES-256 berdasarkan kata sandi dan garam yang dihasilkan secara acak.

4. Fungsi encrypt_text()

Fungsi ini mengenkripsi teks menggunakan AES-256 dalam mode CFB dan menghasilkan teks terenkripsi yang dapat dibagikan bersama dengan kode unik untuk dekripsi.

5. Fungsi decrypt_text()

Fungsi ini mendekripsi teks yang terenkripsi dengan menggunakan kata sandi dan kode unik yang benar.


---

Pesan Penutupan

Terima kasih telah menggunakan SafeText! Berikut adalah pesan terjemahan dalam beberapa bahasa:

Indonesia: Terima Kasih! 🐱

Chinese: 谢谢! 🐼

Russian: Спасибо! 🐶

French: Merci! 🐰

Arabic: شكراً! 🦊

Portuguese: Obrigado! 🐨

Dutch: Dank je wel! 🦋

Japanese: ありがとうございます! 🐥

Spanish: ¡Gracias! 🐢



---

License

ITS FREE, no charge necessary.- see the LICENSE file for details.


---


English (default language)

SafeText is a tool to encrypt and decrypt text securely using AES-256 encryption, with a unique code for every encryption process. It also ensures password security using PBKDF2 to derive AES keys.


---

Español (Spanish)

SafeText es una herramienta para cifrar y descifrar texto de forma segura utilizando cifrado AES-256, con un código único para cada proceso de cifrado. También asegura la seguridad de las contraseñas utilizando PBKDF2 para derivar claves AES.


---

中文 (Chinese)

SafeText 是一个使用 AES-256 加密安全地加密和解密文本的工具，每个加密过程都有一个唯一的代码。它还通过使用 PBKDF2 来确保密码的安全，以派生 AES 密钥。


---

Русский (Russian)

SafeText - это инструмент для безопасного шифрования и дешифрования текста с использованием AES-256, с уникальным кодом для каждого процесса шифрования. Он также гарантирует безопасность паролей, используя PBKDF2 для получения ключей AES.


---

日本語 (Japanese)

SafeText は、AES-256 暗号化を使用してテキストを安全に暗号化および復号化するツールであり、各暗号化プロセスに一意のコードを提供します。また、PBKDF2 を使用して AES キーを導出することでパスワードの安全性を確保します。


---

Ini adalah dokumentasi dasar untuk proyek SafeText yang dapat Anda sesuaikan lebih lanjut sesuai kebutuhan.

