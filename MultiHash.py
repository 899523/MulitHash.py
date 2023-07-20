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

print(color("Current version: Multi-Hash v2.0", fore='orange', style='bright'))

print(color("""
Supported Algorithms
--------------
1: md5
2: sha256
3: sha512
--------------
""", fore='green', style='bright'))

def main():
    file_name = str(input("Enter file path: "))
    md5(file_name)
    sha256(file_name)
    sha512(file_name)
    reup()

def md5(file_name):
    BLOCKSIZE = 65536
    md5 = hashlib.md5()
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            md5.update(buf)
            buf = afile.read(BLOCKSIZE)
    print("md5     : ", color(md5.hexdigest(), fore='green'))

def sha256(file_name):
    BLOCKSIZE = 65536
    sha256 = hashlib.sha256()
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            sha256.update(buf)
            buf = afile.read(BLOCKSIZE)
    print("sha256  : ", color(sha256.hexdigest(), fore='green'))

def sha512(file_name):
    BLOCKSIZE = 65536
    sha512 = hashlib.sha512()
    with open(file_name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            sha512.update(buf)
            buf = afile.read(BLOCKSIZE)
    print("sha512  : ", color(sha512.hexdigest(), fore='green'))

def reup():
    reup = input("Would you like to hash something else? (y or n): ")
    if reup.upper() == "Y":
        main()
    elif reup.upper() == "N":
        exit()
        
main()
