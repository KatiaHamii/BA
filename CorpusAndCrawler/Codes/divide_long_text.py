with open('/Users/kateryna_hamii/Bachelorarbeit/university/WiSe2022-2023/Bachelorarbeit/CorpusAndCrawler/BR24/Korpus/Subcorpora/Hitze.txt', 'r') as f:
    text = f.read()

# Split the text into two parts
midpoint = len(text) // 2
part1 = text[:midpoint]
part2 = text[midpoint:]

# Write each part to a separate file
with open('../BR24/Korpus/Subcorpora/hitze_part1.txt', 'w') as f:
    f.write(part1)

with open('../BR24/Korpus/Subcorpora/hitze_part2.txt', 'w') as f:
    f.write(part2)