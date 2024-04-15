"""
Write sentence 10 times with each line indentend by 1 more space than above 

The Flintstones Rock!
 The Flintstones Rock!
  The Flintstones Rock!
   ...
   """

SENTENCE = 'The Flintstones Rock'
REPEAT_TIMES = 10

for i in range(REPEAT_TIMES + 1):
    print(f"{' ' * i} {SENTENCE}") 

