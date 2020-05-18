


from Crypto.PublicKey import RSA
import os 
import gmpy


def main():
    keygen()
    getPublicKey()
    chiffreRSA()
    getEandN()
        
    
    
# gen pair of keys pem
def keygen():

    nbBits = 200
    os.system('openssl genrsa -out keys.pem '+str(nbBits))
    

# dump public key
def getPublicKey():
    os.system('openssl rsa -in keys.pem -outform PEM -pubout -out public.pem')

# chiffrer message de file.txt dans file.enc
def chiffreRSA():
    os.system('openssl rsautl -encrypt -pubin -inkey public.pem -in file.txt -out file.enc')

# recuperer N et E dans la cle publique
def getEandN():
    os.system('openssl rsa -in public.pem -pubin -text -modulus')

def getModulus():
    os.system('openssl rsa  -pubout -in file.pem')

def getPrivateKey():
    n = 99990849789899199981998409908829996923940929649099
    p = 2351377476303203
    q = 25332115927327163
    e = long(65537)
    d = long(((gmpy.invert(e, (p-1)*(q-1)))))
    
    key = RSA.construct((n,e,d))
    print key.exportKey()




if __name__ == '__main__':
    main()
