import os


# Dechiffrer mon fichier avec la cle privee

def main() :
    os.system('openssl rsautl -decrypt -inkey privkey.pem -in file.enc -out file.out')