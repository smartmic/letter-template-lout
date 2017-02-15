#!/usr/bin/env python3
"""Provides pre-filled letter sources files with dummy content

This scripts generates two files which serve as templates for the
letter system 'brief-template-*'. The random content is a placeholder
for ones personal letters and was sourced with the help of `Elizabeth
<http://elizabeth.readthedocs.io/en/latest/#>`_ """

from string import Template
from random import getrandbits
from elizabeth import *

__author__ = "Martin Michel"
__copyright__ = "Copyright 2017"

p = Personal('de')
a = Address('de')
b = Business('de')
#d = Datetime('de') 
t = Text('de')

with open ("brief-template.lout", "r") as letterfile:
    dummyletter=Template(letterfile.read())
with open ("mybrief-template", "r") as layoutfile:
    mylayout=Template(layoutfile.read())

sender_name = p.full_name(gender='female')
sender_street = a.address()
sender_postal_code = a.postal_code()
sender_city = a.city()

with open('../brief.lout', 'w', encoding='latin1') as out0:
    out0.write(dummyletter.substitute(
    sender_name = sender_name,
    sender_street = sender_street,
    sender_postal_code = sender_postal_code,
    sender_city = sender_city,
    company = b.company(),
    addresee_name = p.full_name(gender='male'),
    addresee_street = a.address(),
    addresee_postal_code = a.postal_code(),
    addresee_city = a.city(),
    number = getrandbits(16),
    first_paragraph = t.text(quantity=2),
    second_paragraph =  t.text(quantity=5),
    subject = t.quote()))

with open('../mybrief', 'w', encoding='latin1') as out1:
    out1.write(mylayout.substitute(
    sender_name = sender_name,
    sender_street = sender_street,
    sender_postal_code = sender_postal_code,
    sender_city = sender_city,
    sender_email = p.email(),
    sender_phone0 = p.telephone(),
    sender_phone1 = p.telephone(),
    sender_phone2 = p.telephone(),
    sender_credit_card = p.credit_card_number(card_type='visa')))
