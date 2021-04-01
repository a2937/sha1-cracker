import hashlib
import fileinput
def crack_sha1_hash(hash, use_salts=False):
    if(use_salts == True): 
       for line in fileinput.input(['top-10000-passwords.txt']):
          with open("known-salts.txt") as salts:
            for salt in salts:  
              for i in (0,1,2):
                safeLine = line.strip() 
                sha1 = hashlib.sha1()
                safeSalt = salt.strip()
                if i == 0:
                  toHash = "".join((safeSalt,safeLine,safeSalt))
                elif i == 1:
                  toHash = "".join((safeLine,safeSalt))
                elif i == 2: 
                   toHash = "".join((safeSalt,safeLine))
                sha1.update(toHash.encode("utf-8")) 
                digest = sha1.hexdigest(); 
                if(digest == hash) :
                  fileinput.nextfile()
                  return safeLine
    else: 
      with open("top-10000-passwords.txt") as passwords:
        for line in passwords:
          sha1 = hashlib.sha1()
          safeLine = line.strip() 
          sha1.update(safeLine.encode('utf-8')) 
          digest = sha1.hexdigest(); 
          if(digest == hash) :  
            return safeLine
    return "PASSWORD NOT IN DATABASE"