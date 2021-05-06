import time
import hashlib
from colr import color
from colr import Colr as C

print(C("""

===========================================================================

  MM     MM  U   U  L    TTTTT  III         H   H      A      SSSS  H   H
  M M   M M  U   U  L      T     I          H   H     A A     S     H   H
  M  M M  M  U   U  L      T     I   -----  HHHHH    A   A    SSSS  HHHHH
  M   M   M  U   U  L      T     I          H   H   A AAA A      S  H   H
  M       M  UUUUU  LLLLL  T    III         H   H  A       A  SSSS  H   H

===========================================================================

""").rainbow(rgb_mode=True))

print(color("""
Algorithm List
--------------
1: md5 Hash
2: sha256 Hash
3: sha512 Hash
--------------
""", fore='green', style='bright'))

def main():
    file_name = str(input("Enter file path: "))
    method = int(input("Enter hashing algorithm(1-3): "))
    algorithm(file_name, method)

def algorithm(file_name, method):
    if method == 1:
        md5(file_name)
        
    elif method == 2:
        sha256(file_name)

    elif method == 3:
        sha512(file_name)
    else:
        print(color("Please select valid method.", fore='red', style='bright'))
        main()

def md5(file_name):
    print("Hashing with md5")
    BLOCKSIZE = 65536
    md5 = hashlib.md5()
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            md5.update(buf)
            buf = afile.read(BLOCKSIZE)
    print("Your md5 hash is: " + color(md5.hexdigest(), fore='green'))
    reup()

def sha256(file_name):
    print("Hashing with sha256")
    BLOCKSIZE = 65536
    sha256 = hashlib.sha256()
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            sha256.update(buf)
            buf = afile.read(BLOCKSIZE)
    print("Your sha256 hash is: " + color(sha256.hexdigest(), fore='green'))
    reup()

def sha512(file_name):
    print("Hashing with sha512")
    BLOCKSIZE = 65536
    sha512 = hashlib.sha512()
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            sha512.update(buf)
            buf = afile.read(BLOCKSIZE)
    print("Your sha512 hash is: " + color(sha512.hexdigest(), fore='green'))
    reup()

def reup():
    reup = input("Would you like to hash something else? (y or n): ")
    if reup.upper() == "Y":
        main()
    elif reup.upper() == "N":
        print(color("Thank you for using MULIT-HASH! Come back soon!", fore='blue', style='bright'))
        time.sleep(2)
        exit()
        
main()
