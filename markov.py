import markovify
import sys
import array

if len(sys.argv) > 1:
    with open(sys.argv[1]) as f:
        text = f.read()
else:
    with open("petke.txt") as f:
        text = f.read()

text_model = markovify.Text(text, state_size=1)

for i in range(5):
    print(text_model.make_short_sentence(240, tries=1000))
