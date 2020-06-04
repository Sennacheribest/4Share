import re
import sys
import time

from dictionary import check, load, size, unload

# maximum length of a word
# e.g.,pneumonoultramicroscopicsilicovolcanoconiosis
LENGTH = 45

# default dictionary
WORDS = "dictionaries/large"

# check for the correct number of args
if len(sys.argv) != 2 and len(sys.argv) != 3:
    print("Usage: speller [dictionary] text")
    sys.exit(1)

# benchmarks
time_load, time_check, time_size, time_unload = 0.0, 0.0, 0.0, 0.0

# determine dictionary to use
dictionary = sys.argv[1] if len(sys.argv) == 3 else WORDS

# load dictionary
before = time.process_time()
loaded = load(dictionary)
after = time.process_time()

# exit if dictionary not loaded
if not loaded:
    print(f"Could not load {dictionary}")
    sys.exit(1)

# calculate time to load the dictionary
time_load = after - before

# try to open text
text = sys.argv[2] if len(sys.argv) == 3 else sys.argv[1]
file = open(text, "r", encoding="latin_1")
if not file:
    print("Could not open {}".format(text))
    unload()
    sys.exit(1)

# prepare to report misspelling
print("\nMISSPELLED WORDS\n")

# prepare to spell-check
word = ""
index, misspellings, words = 0, 0, 0

# spell-check each word in file
while True:
    c = file.read(1)
    if not c:
        break

    # allow alphabetical characters and apostrophes (for possessives)    -- ASSISTED BY DEVELOPER --
    if re.match(r"[A-Za-z]", c) or (c == "'" and index > 0):

        # append character to word
        word += c
        index += 1

    # ignore alphabetical strings too long to be word
    if index > LENGTH:

        # consume reminder of alphabetical string
        while True:
            c = file.read(1)
            if not c or not re.match(r"[A-Za-z]", c):
                break

        # prepare for new word
        index, word = 0, ""

    # ignore words with number
    elif c.isdigit():

        # consume remider of alphabetical string
        while True:
            c = file.read(1)
            if not c or (not c.isalpha() and not c.isdigit()):
                break

        # prepare for new word
        index, word = 0, ""

    # we must have found a whole word
    elif index > 0:

        # update counter
        words += 1

        # check words's spelling
        before = time.process_time()
        misspelled = not check(word)
        after = time.process_time()

        # update benchmark
        time_check += after - before

        # print word if misspelled
        if misspelled:
            print(word)
            misspellings += 1

        # prepare for new word
        index, word = 0, ""

# close file
file.close()

# determine dictionary's size
before = time.process_time()
n = size()
after = time.process_time()

# calculate time to determine dictionary's size
time_size = after - before

# unload dictionary
before = time.process_time()
unloaded = unload()
after = time.process_time()

# abort if dictionary not unloaded
if not unloaded:
    print(f"Could not unload {dictionary}.")
    sys.exit(1)

# calculate time to unload dictionary
time_unload = after - before

# report benchmark
print(f"\nWORDS MISSPELLED: \t {misspellings}")
print(f"WORDS IN DICTIONARY: \t {n}")
print(f"WORDS IN TEXT: \t {words}")
print(f"TIME IN LOAD: \t {time_load:.2f}")
print(f"TIME IN CHECK: \t {time_check:.2f}")
print(f"TIME IN SIZE: \t {time_size:.2f}")
print(f"TIME IN UNLOAD: \t {time_unload:.2f}")
print(f"TOTAL TIME: \t {time_load + time_check + time_size + time_unload:.2f}\n")
# success
exit(0)





















