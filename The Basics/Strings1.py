# Strings are texts

fred = "Why do gorillas have big nostrils? Big fingers!!"
#use the print function to see what is inside of fred
print(fred)
#result = Why do gorillas have big nostrills? Big fingers!!

# Creating single quote strings
fred = 'What is pink and fluffy? Pink fluff!!'
print(fred)
#result = What is pink and fluffy? Pink fluff!

# ERROR messages - AVOID making these mistakes!!
fred = "How do dinosaurs pay their bills?
#result = SyntaxError: EOL while scanning string literal

# Strings w/ more than one line
fred = '''How do dinosaurs pay their bills?
With tyrannosaurus checks!'''

print(fred)
#result = How do dinosaurs pay their bills?
          With tyrannosaurus checks!

# Handling problems w/ strings
silly_string = 'He said, "Aren't can't shouldn't wouldn't."'
#result = SyntaxError: invalid syntax

silly_string = "He said, "Aren't can't shouldn't wouldn't.""
#result = SyntaxError: invalid syntax

#Error-free version
silly_string = '''He said, "Aren't can't shouldn't wouldn't."'''
