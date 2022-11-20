import sys
import os
import shutil

##
# Prameters
# - Receiver number
# - Message file path
N = int(sys.argv[1])
message_path = sys.argv[2]

# Parse message 
sentences = list()
with open(message_path) as f:
    message = f.read()
    sentences = message.split(" ")
    f.close()
sentence_N = len(sentences)

# Make a directory for output
name = "out"
if(os.path.exists(name)):
    shutil.rmtree(name)
os.makedirs(name)

# Generate unique messages from original
for i in range(N):
    out = ""
    _unique_id = format(i, f"0{sentence_N - 1}b")
    unique_id = [*_unique_id]
    for j in range(sentence_N):
        if(sentence_N - 1 == j):
            out += f"{sentences[j]}"
        elif(unique_id[j] == "0"):
            out += f"{sentences[j]} "
        elif(unique_id[j] == "1"):
            out += f"{sentences[j]}  "
    with open(f"./out/{_unique_id}.txt","x") as f:
        f.write(out)
        f.close()

print("complete.")