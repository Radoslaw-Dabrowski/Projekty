# open file:

name = input('Input filename: ')
handle = open(name)

# define counts as dictionary {key: value, key2: value2}
counts = dict()
for line in handle:
    # split each line (because of the for loop) into words - empty brackets means space as a separator
    words = line.split()
    for word in words:
        # add to each word seen in file value how many repeats are there, increment by one in every hit
        counts[word] = counts.get(word,0) + 1
        
# define some variables
biggestcount = None
biggestword = None

# go through dictionary and define biggest count and determine word for this biggest count
for word,count in counts.items():
    if biggestcount is None or count > biggestcount:
        biggestword = word
        biggestcount = count
        
# print everything into the screen
print(biggestword, biggestcount)