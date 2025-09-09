import time
import sys
from colorama import Fore, Style, init

# aktifkan colorama
init(autoreset=True)

def loading(text, delay=0.1, dots=3):
    """Animasi loading kecil"""
    for _ in range(dots):
        sys.stdout.write(text + "." * (_ + 1) + "\r")
        sys.stdout.flush()
        time.sleep(delay)
    print(" " * 30, end="\r")  # bersihkan baris

print(Fore.CYAN + Style.BRIGHT + "===== SAYANG DAPOLL?? =====")
time.sleep(1)

pertanyaan_tudei = input(Fore.YELLOW + "👉 apa kamu sayang dapoll? (sayang/GA): ")

loading("memproses jawaban", delay=0.4)

if pertanyaan_tudei.lower() == "sayang":
    print(Fore.GREEN + "LOVEE BANYAKK BANYAKKKK")
    time.sleep(1)
    print(Fore.MAGENTA + "I LOVEE UU SAYANGGGG<3")
else:
    print(Fore.RED + "eek mogu💔")
    time.sleep(1)
    print(Fore.BLUE + "kamu melukai hati mungilku :(")
