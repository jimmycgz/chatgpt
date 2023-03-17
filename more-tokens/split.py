import tokenize
from io import BytesIO

def count_tokens_by_syntax(code):
    # This function counts the number of tokens in a string based on python syntax
    tokens = tokenize.tokenize(BytesIO(code.encode('utf-8')).readline)
    count = 0
    for token in tokens:
        count += 1
    return count

def count_tokens_by_words(code):
    # This function counts the number of tokens in a string based on words
    words = code.split()
    count = len(words)
    return count

def count_tokens_by_chars(code):
    # This function counts the number of tokens in a string based on characters
    chars = len(code)
    count = chars // 4 # one token is roughly four characters in English
    return count

def split_file_by_tokens(input_content, max_tokens):
    # This function splits a file into smaller parts with a maximum number of tokens each
    input = open(filename, 'r')
    outputBase = 'output' # output.1.txt, output.2.txt, etc.
    
    part = 0 # the current part number
    dest = None # the current output file
    code = "" # the current code string
    
    for line in input:
        code += line
        
        if count_tokens_by_syntax(code) >= max_tokens: # you can use any of the other functions here instead
            if dest: dest.close()
            dest = open(outputBase + str(part) + '.txt', 'w')
            part += 1
            
            dest.write(code)
            code = ""
    
    if code: # write the remaining code if any
        if dest: dest.close()
        dest = open(outputBase + str(part) + '.txt', 'w')
        part += 1
        
        dest.write(code)

if __name__ == "__main__":
    filename = "BrainTrust-Transcript.txt" # change this to your input file name
    with open(filename, 'r') as f:
      code = f.read()

    # test the count_tokens_by_syntax function
    # code = "grammar = grammar_path.read_text (encoding=\"UTF-8\")"
    print("Number of tokens by syntax:", count_tokens_by_syntax(code))
    
    # test the count_tokens_by_words function
    print("Number of tokens by words:", count_tokens_by_words(code))
    
    # test the count_tokens_by_chars function
    print("Number of tokens by chars:", count_tokens_by_chars(code))
    
    # test the split_file_by_tokens function
    
    max_tokens = 2048 # change this to your desired maximum number of tokens per part
    split_file_by_tokens(filename, max_tokens)        