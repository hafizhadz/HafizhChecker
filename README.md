# HafizhChecker

A simple checker/tool project by MhafizhA.

## Description

HafizhChecker is a personal utility project designed for checking and validation purposes.

## Features

- ✔️ Simple combo file usage
- ✔️ Login with Email
- ✔️ Login with Username
- ✔️ Bypassing captcha verification (sometimes)

## Cara Pakai di Termux

1. **Install Termux** dari F-Droid atau Google Play.

2. **Update package** (pertama kali saja):
   ```bash
   pkg update && pkg upgrade -y
   ```

3. **Install Git dan Python** (jika belum ada):
   ```bash
   pkg install git python -y
   ```

4. **Clone repositori ini:**
   ```bash
   git clone https://github.com/hafizhadz/HafizhChecker.git
   cd HafizhChecker
   ```

5. **Jalankan project** (sesuaikan perintah dengan file utama yang ada):
   ```bash
   python main.py
   ```

### Edit `combo.txt` di Termux

**Pakai nano** (recommended):
```bash
pkg install nano -y
nano combo.txt
```
Simpan: `Ctrl+X`, lalu `Y`, lalu `Enter`.

**Pakai echo** (tambah isi):
```bash
echo "email:password" >> combo.txt
```

**Pakai cat** (timpa isi file):
```bash
cat > combo.txt
email:password
username:password
# Ctrl+D untuk selesai
```

## Usage

```bash
python main.py
```

## License

This project is for personal use.
