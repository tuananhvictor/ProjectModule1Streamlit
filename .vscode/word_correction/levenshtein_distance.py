
import streamlit as st

def levenshtein_distance(str1, str2):
 

  m = len(str1) + 1  # Length of the first string + 1 (for empty string)
  n = len(str2) + 1  # Length of the second string + 1 (for empty string)

  # Create a matrix to store edit distances
  d = [[0 for _ in range(n)] for _ in range(m)]

  # Initialize base cases (empty strings)
  for i in range(m):
    d[i][0] = i  # Inserting all characters of str1

  for j in range(n):
    d[0][j] = j  # Deleting all characters of str1

  # Fill the remaining cells using the Levenshtein distance formula
  for i in range(1, m):
    for j in range(1, n):
      if str1[i - 1] == str2[j - 1]:
        cost = 0  # No edit needed if characters are the same
      else:
        cost = 1  # Cost of substitution

      d[i][j] = min(
          d[i - 1][j] + 1,  # Insertion
          d[i][j - 1] + 1,  # Deletion
          d[i - 1][j - 1] + cost  # Substitution
      )

  return d[m - 1][n - 1]  # Levenshtein distance at the bottom right corner

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
vocabs = load_vocab(file_path=r'C:/Users/HP/Downloads/word_correction/vocab.txt')

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
        
        # sorted by distance
        sorted_distences = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distences)
