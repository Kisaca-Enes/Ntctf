import os
import time
import curses

print('Kullanabileceğiniz komutlar: nmap, john --wordlist=/usr/share/wordlists/rockyou.txt dosya.txt, enum4linux, ftp, ssh, exit, cat')

def execute_command(command, stdscr):
    stdscr.clear()
    stdscr.border()
    command = command.lower()
    output = ""

    # Komutlara göre çıktı oluşturuluyor
    if "nmap" in command:
        output = """
# Nmap 7.94 scan report for 1.0.1.0.1
PORT     STATE SERVICE      VERSION
21/tcp   open  ftp          vsftpd 3.0.3
22/tcp   open  ssh          OpenSSH 8.2p1
445/tcp  open  smb          Windows 10 Pro
80/tcp  open  http     Apache httpd 2.4.41 (Ubuntu)
"""
    elif "enum4linux" in command:
        output = """
# Enum4Linux Çıktısı
Kullanıcılar:
- Administrator
- Guest
- ali
Paylaşılan Klasörler:
- ADMIN$
- ali_files (özel)
"""
    elif "ftp" in command:
        os.system('start %USERPROFILE%\\Desktop\\ctf\\fftp.py') 
        # Burada os.open yerine uygun bir işlem kullanmalıyız.
        output = "FTP bağlantısı başlatıldı."
    elif "http://1.0.1.0.1" in command:
        os.system('start %USERPROFILE%\\Desktop\\ctf\\idex.html') 
        # Burada os.open yerine uygun bir işlem kullanmalıyız.
    elif "cat password.txt" in command:
        output = '8350e5a3e24c153df2275c9f80692773'  # Dosyadan okuma yapılacak
    elif "john --wordlist=/usr/share/wordlists/rockyou.txt password.txt" in command:
        output = 'Çözülmüş hash: Ali123'
    elif "ssh" in command:
        output = "SSH bağlantısı başlatıldı."
        os.system('start %USERPROFILE%\\Desktop\\ctf\\ssh.py') 
    elif "exit" in command:
        exit()
    else:
        output = "Bilinmeyen komut."

    # Terminal boyutlarını alıyoruz
    height, width = stdscr.getmaxyx()

    # Komut çıktısını ekrana yazdırıyoruz
    stdscr.addstr(2, 2, f"[ {command} Çıktısı ]", curses.A_BOLD)
    stdscr.addstr(4, 2, output)

    # Komut bekleyen satır için ekranın altına uygun bir satır ekliyoruz
    stdscr.addstr(height - 2, 2, "Komut bekleniyor...")
    stdscr.refresh()

    # 2 saniye bekleyip işlemi sonlandırıyoruz
    time.sleep(2)

def hacker_terminal(stdscr):
    curses.curs_set(1)
    stdscr.clear()
    stdscr.border()

    # ASCII banner ve komutlar
    ascii_banner = """
██╗  ██╗ █████╗ ██╗     ██╗     
██║ ██╔╝██╔══██╗██║     ██║     
█████╔╝ ███████║██║     ██║     
██╔═██╗ ██╔══██║██║     ██║     
██║  ██╗██║  ██║███████╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
Kali Linux Terminal Emulator
"""

    stdscr.addstr(1, 2, ascii_banner, curses.A_BOLD)
    stdscr.refresh()

    # Sonsuz döngü ile komutları alıyoruz
    while True:
        stdscr.addstr(10, 2, "┌──(root@kali)-[~]")
        stdscr.addstr(11, 2, "└─# ")
        stdscr.refresh()

        curses.echo()
        command = stdscr.getstr(11, 5, 1000).decode("utf-8").strip()
        curses.noecho()

        # Komutu işleyip ekrana yazdırıyoruz
        execute_command(command, stdscr)

if __name__ == "__main__":
    curses.wrapper(hacker_terminal)
