#!/usr/bin/env python

#---------------------------------------------------------------------#
# Project : Obfuscating Python Code                                   #
# Script  : Obfuscator                                                #
# Author  : Mrinal Wahal                                              #
# Website : http://www.dynacrux.de.vu/                                #
#---------------------------------------------------------------------#

print "-"*60
print "            Obfuscator"
print "-"*60

infile_input = raw_input("Enter The Host File : ")

import random, os

print "\n[+]Initializing Malicious Code..."

code = [
    "if 64 - 64: i11iIiiIii",
    "if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi",
    "if 73 - 73: II111iiii",
    "if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i",
    "if 48 - 48: oO0o / OOooOOo / I11i / Ii1I",
    "if 48 - 48: iII111i % IiII + I1Ii111 / ooOoO0o * Ii1I",
    "if 46 - 46: ooOoO0o * I11i - OoooooooOO",
    "if 30 - 30: o0oOOo0O0Ooo - O0 % o0oOOo0O0Ooo - OoooooooOO * O0 * OoooooooOO",
    "if 60 - 60: iIii1I11I1II1 / i1IIi * oO0o - I1ii11iIi11i + o0oOOo0O0Ooo",
    "if 94 - 94: i1IIi % Oo0Ooo",
    "if 68 - 68: Ii1I / O0",
    "if 46 - 46: O0 * II111iiii / IiII * Oo0Ooo * iII111i . I11i",
    "if 62 - 62: i11iIiiIii - II111iiii % I1Ii111 - iIii1I11I1II1 . I1ii11iIi11i",
    "if 61 - 61: oO0o / OoOoOO00 / iII111i * OoO0O00 . II111iiii",
    "if 1 - 1: II111iiii - I1ii11iIi11i % i11iIiiIii + IiII . I1Ii111",
    "if 55 - 55: iIii1I11I1II1 - I1IiiI . Ii1I * IiII * i1IIi / iIii1I11I1II1"
    ]

print "[+]Code Initialized."

def insert_code(outputfile):
    for x in range (3):
        rand = random.choice(code)
        outputfile.write(rand + "\n")
    
infile = open(infile_input + ".py","r+")
outfile = open(infile_input + " - Obfuscated.py","w")

outfile.write("#!/usr/bin/env python" + "\n")

try:
    for line in infile.readlines():
        line_parts = line.strip(":")
        if not line.strip(): insert_code(outfile)
        elif line[0] == "#": insert_code(outfile)
        elif line_parts[-1] == "": insert_code(outfile), outfile.write(line)
        else: outfile.write(line)
    insert_code(outfile)
    print "[+]Operation Completed."
    infile.close()
    outfile.close()
    
except Exception, e:
    print "[-]Error Detected." + str(e)
    print "[-]Operation Completed With Errors."
    
print
os.system("pause")