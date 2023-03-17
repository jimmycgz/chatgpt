import tokenize
from io import BytesIO

def count_tokens_by_syntax(code):
    tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)
    return sum(1 for _ in tokens)

f = open("BrainTrust-Transcript.txt", "r")
code = f.read() # read the file content as a string
print("Number of tokens by syntax:", count_tokens_by_syntax(code))