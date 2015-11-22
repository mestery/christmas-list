#!/usr/bin/python
#
# Copyright 2012-2013 Kyle Mestery
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

# vim: tabstop=4 shiftwidth=4 softtabstop=4
#

import random
import six
import sys

name_map = {0: 'Kyle',
            1: 'Sue',
            2: 'Al',
            3: 'Susan',
            4: 'Joe',
            5: 'Kim',
            6: 'John',
            7: 'Natalie'}

buy_list = {'Kyle': ('Sue'),
            'Sue': ('Kyle'),
            'Al': ('Susan'),
            'Susan': ('Al'),
            'Joe': ('Kim'),
            'Kim': ('Joe'),
            'John': ('Natalie'),
            'Natalie': ('John')}

kids_name_map = {0: 'Halle',
                 1: 'Tyler',
                 2: 'Gavin',
                 3: 'Andrew',
                 4: 'Erica',
                 5: 'Kayla',
                 6: 'Michael',
                 7: 'Matthew',
                 8: 'Katelyn',
                 9: 'Sarah'}

kids_buy_list = {'Halle': ('Tyler', 'Gavin', 'Andrew'),
                 'Tyler': ('Halle', 'Gavin', 'Andrew'),
                 'Gavin': ('Halle', 'Tyler', 'Andrew'),
                 'Andrew': ('Halle', 'Tyler', 'Gavin'),
                 'Erica': ('Kayla'),
                 'Kayla': ('Erica'),
                 'Michael': ('Matthew'),
                 'Matthew': ('Michael'),
                 'Katelyn': ('Sarah'),
                 'Sarah': ('Katelyn')}


def check_if_buy_ok(person, buyfor, plist=kids_buy_list):
    # Pull out the name
    if person not in plist:
        sys.stderr.write('Warning, %s not in list\n' + person)

    skip = plist[person]
    if buyfor in skip:
        return False
    else:
        return True


def find_random_name(person1, nmap):
    rand = random.randint(0, 1000000)
    randname = nmap[rand % len(nmap)]
    while randname == person1:
        rand = random.randint(0, 1000000)
        randname = nmap[rand % len(nmap)]
    return randname


def setup_random(x):
    if not x:
        random.seed(None)
    else:
        random.seed(x)


def check_name_in_dict(named, name):
    for key in named:
        if named[key] == name:
            return True
    return False

# Setup our random number generator
setup_random

# Our return dictionary
result_dict = {}
kids_result_dict = {}
# How man times to loop?
loopcount = len(name_map) - 1
kidsloopcount = len(kids_name_map) - 1
# Detect a failing loop
failloop = 100

while loopcount >= 0:
    rnum = random.randint(0, 1000000)
    lname = name_map[loopcount]
    while True:
        failloop = failloop - 1
        # Get a random name
        randname = find_random_name(name_map[loopcount], name_map)
        # Check if it's ok to buy for this person
        if check_if_buy_ok(name_map[loopcount], randname, buy_list):
            # Check if we've already bought for this person
            if not check_name_in_dict(result_dict, randname):
                break
            # Check if we need to start over
            if loopcount == 0 or failloop <= 0:
                failloop = 100
                # Reset things and start over
                setup_random
                loopcount = len(name_map) - 1
                result_dict.clear()

    result_dict[name_map[loopcount]] = randname
    loopcount = loopcount - 1

print('=== Adult Output list ===')
for key, value in six.iteritems(result_dict):
    print("%s will buy for %s" % (key, value))

while kidsloopcount >= 0:
    rnum = random.randint(0, 1000000)
    lname = kids_name_map[kidsloopcount]
    while True:
        failloop = failloop - 1
        # Get a random name
        randname = find_random_name(kids_name_map[kidsloopcount],
                                    kids_name_map)
        # Check if it's ok to buy for this person
        if check_if_buy_ok(kids_name_map[kidsloopcount], randname):
            # Check if we've already bought for this person
            if not check_name_in_dict(kids_result_dict, randname):
                break
            # Check if we need to start over
            if kidsloopcount == 0 or failloop <= 0:
                failloop = 100
                # Reset things and start over
                setup_random
                kidsloopcount = len(kids_name_map) - 1
                kids_result_dict.clear()

    kids_result_dict[kids_name_map[kidsloopcount]] = randname
    kidsloopcount = kidsloopcount - 1

print('\n')
print('=== Kids Output list ===')
for key, value in six.iteritems(kids_result_dict):
    print("%s will buy for %s" % (key, value))
