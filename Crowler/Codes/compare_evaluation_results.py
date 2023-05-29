def read_words_from_txt(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return set([word.split('\t')[0].lower() for word in words])

def main():
    # Read the words from the TXT files
    words1 = read_words_from_txt('/Users/kateryna_hamii/Bachelorarbeit_v2_fromGit/Organisatorisch/Graph_final/results_evaluation_im_fokus.txt')
    words2 = read_words_from_txt('/Users/kateryna_hamii/Bachelorarbeit_v2_fromGit/Organisatorisch/Graph_final/results_individuelles_Verhalten_evaluation.txt')
    words3 = read_words_from_txt('/Users/kateryna_hamii/Bachelorarbeit_v2_fromGit/Organisatorisch/Graph_final/results_Wirbelstürme,Beben,Vulkanausbrüche_evaluation.txt')

    # Find the common words among the text files
    common_words = words1.intersection(words2, words3)

    # Print the common words
    if common_words:
        print("Common words found:")
        for word in common_words:
            print(word)
    else:
        print("No common words found.")

    print("Number of common words:", len(common_words))


if __name__ == '__main__':
    main()
