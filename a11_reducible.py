# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime (n):
    if (n == 1):
        return False

    limit = int (n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_idx = 0
    for j in range (len(s)):
        letter = ord (s[j]) - 96
	    hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):

    ln = len(s)
    idx = 0
    for x in range(ln):
        let = (ord (s[j]) - 96)
        idx = (idx * 26 + let) % const
    ss = const - (idx % const)

    return ss

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):

    ht = hash_table
    ln = len(ht)
    
    if ((ht[hash_word(s, ln)]) != ' '):
        new = step_size(s, 13)
        x = 1
        while (ht[((hash_word(s, ln)) + new * x) % ln] != ' '):
            x = x + 1
        s = ht[((hash_word(s, ln)) + new * x) % ln]
    else:
        s = ht[hash_word(s, ln)]

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    ht = hash_table
    ln = len(ht)
    
    if (ht[hash_word(s, ln)] != ' '):
        new = step_size(s, 13)
        x = 1
        while (ht[((hash_word(s, ln)) + new * x) % ln] != ' '):
            if (s == ht[((hash_word(s, ln)) + new * x) % ln]):
                return True
            x = x + 1
    return False
    
    if (s == ht[hash_word(s, ln)]):
        return True


# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
    ht = hash_table
    hm = hash_memo
    ln = len(s)

    if find_word(s, hm):
        return True
    elif find_word(s, ht):
        for x in range(ln):
            y = s[i + 1:] + s[:i]
            if is_reducible(y, ht, hm):
                insert_word(s, hm)
                return True
    return False

    if (ln == 1) and (s == "a" or s == "i" or s == "o"):
        return True


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):

    sl = string_list
    mln = len(max(string_list, key = len))
    lon = []
    for x in sl:
        if (len(x) == mln):
            lon.append(x)
    return lon


def main():
  # create an empty word_list
    word_list = []
  # open the file words.txt
    in_file = open("words.txt", 'r')
  # read words from words.txt and append to word_list
    word = in_file.readlines()
    for x in range(len(word)):
        word[x] = word[x].strip()
        word_list.append(word[x])
  # close file words.txt
    in_file.close
  # find length of word_list
    ln = len(word_list)
  # determine prime number N that is greater than twice
  # the length of the word_list
    prime_num = ln * 2
    while (is_prime(prime_num) == False):
        prime_num = prime_num + 1

  # create an empty hash_list
    hash_list = []
  # populate the hash_list with N blank strings
    for x in range(prime_num):
        hash_list.append('')
  # hash each word in word_list into hash_list
  # for collisions use double hashing 
    for x in word_list:
        insert_word(word, hash_list)
  # create an empty hash_memo of size M
    hash_memo = []
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list

  # populate the hash_memo with M blank strings
    for x in range(prime_num):
        hash_memo.append('')
  # create an empty list reducible_words
    reducible_words = []
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
    for x in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)
  # find words of the maximum length in reducible_words
    longest = get_longest_words(reducible_words)
  # print the words of maximum length in alphabetical order
  # one word per line
    longest.sort()
    for x in longest:
        print(x)
# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()