from model.contact import Contact
import pytest
import random
import string
import os.path
import jsonpickle
import sys
import getopt

try:
      opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
      getopt.usage()
      sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(name="", lastname="")] +[
    Contact(name=random_string("name", 10), lastname=random_string("lastname", 10))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open (file, "w") as out:
    out.write(jsonpickle.encode(testdata, indent=2))