# Import needed modules
import sys
import csv

def main():
    # Do sanity check for only three command-line arguments
    if len(sys.argv) != 3:
        print('Usage: python dna.py database.csv sequences.txt')
        sys.exit(1)

    # Extract files path from user input
    csvPath = sys.argv[1]
    seqPath = sys.argv[2]

    # Open the CSV file database for read
    with open(csvPath) as csvFile:
        # Use reader method provided by CSV module to return an object
        reader = csv.reader(csvFile)
        # Modify the CSV file by eliminating the header row and the names column
        justValues = next(reader)[1:]

        # Open the text sequence file for read
        with open(seqPath) as seqFile:
            s = seqFile.read()
            # Compare each return values from (max_consecutive_str) function with the modified CSV numbers
            tmp = [max_consecutive_str(s, seq) for seq in justValues]
        # Call fuction to do the last check for each name and its consecutive STRs
        ismatch(reader, tmp)


def max_consecutive_str(s, sub):
    # Initialize a list full of zeros to match the same number of sequnce file
    tmp = [0] * len(s)
    # Iterate through the list backward, and calculate  number of consecutive STR based upon CSV column
    for i in range(len(s) - len(sub), -1, -1):
        if s[i: i + len(sub)] == sub:
            if i + len(sub) > len(s) -1:
                tmp[i] = 1
            else:
                tmp[i] = 1 + tmp[i + len(sub)]
    # Using max bulid-in function to find the maximum number
    return max(tmp)


def ismatch(reader, tmp):
    for line in reader:
        # Extract only names from each row and save it into variable
        being = line[0]
        # Extracting str values then converting it into integer
        values = [int(val) for val in line[1:]]
        if values == tmp:
            # Returns peson's name if each STRs are matched
            print(being)
            return
    print('No match')

main()
