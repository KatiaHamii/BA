import glob

# get a list of all .txt files in the current directory
txt_files = glob.glob('*.txt')

# create an empty string to store the combined text
all_text = ""

# loop through each file and append its contents to the all_text string
for file in txt_files:
    with open(file, 'r', encoding='utf-8') as f:
        all_text += f.read()

# write the combined text to a new file
with open('combined_text.txt', 'w', encoding='utf-8') as f:
    f.write(all_text)
