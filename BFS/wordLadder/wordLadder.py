# Input processing
beginWord = input().strip()
endWord = input().strip()
wordList = input().strip().split()

# Check if endWord is not in wordList, return 0 immediately
if endWord not in wordList:
    print(0)
    exit()

# Class definition for word states
class WordState:
    def __init__(self, word, length):
        self.word = word
        self.length = length

# Function to check if a transformation is valid
def is_valid_transform(from_word, to_word):
    diff = sum(1 for a, b in zip(from_word, to_word) if a != b)
    return diff == 1

# Initialize the queue with the beginWord
Q = [WordState(beginWord, 1)]

# Set to keep track of visited words
visited = set([beginWord])

# BFS to find the shortest path
while Q:
    current_state = Q.pop(0)
    current_word = current_state.word
    current_length = current_state.length

    if current_word == endWord:
        print(current_length)
        exit()

    for word in wordList:
        if word not in visited and is_valid_transform(current_word, word):
            visited.add(word)
            Q.append(WordState(word, current_length + 1))

# If the loop ends without finding the endWord, no transformation is possible
print(0)
