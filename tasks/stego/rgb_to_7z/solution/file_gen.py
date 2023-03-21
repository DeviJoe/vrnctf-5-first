import sys
import os
import random
import string

if len(sys.argv) != 4:
    print("Incorrect arguments count!")
    print("file_gen.py <Output dir> <Text length> <Count>")
    exit()

output_dir = sys.argv[1]
text_len = int(sys.argv[2])
files_count = int(sys.argv[3])

text_prefix = "Your flag is in another file! "
for i in range(0, files_count):
   random_text = text_prefix + ''.join(random.choice(string.ascii_lowercase) for i in range(text_len - len(text_prefix)))
   filepath = os.path.join(output_dir, f"flag_{i:02d}.txt")
   with open(filepath, 'w') as f:
    f.write(random_text)
   print(filepath)
    
print("Done")