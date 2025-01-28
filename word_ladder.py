from typing import List
import unittest
from collections import deque


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    if endWord not in wordList:
        return 0

    wordList = list(set(wordList))
    if beginWord not in wordList:
        wordList.append(beginWord)

    graph = {word: [] for word in wordList}
    for i in range(len(wordList)):
        for j in range(i + 1, len(wordList)):
            if can_transform(wordList[i], wordList[j]):
                graph[wordList[i]].append(wordList[j])
                graph[wordList[j]].append(wordList[i])

    queue = deque([(beginWord, 1)]) 
    visited = set()

    while queue:
        current_word, steps = queue.popleft()

        if current_word == endWord:
            return steps

        if current_word not in visited:
            visited.add(current_word)
            for neighbor in graph[current_word]:
                if neighbor not in visited:
                    queue.append((neighbor, steps + 1))

    return 0

def can_transform(word1, word2, num_transformations=1) -> bool:
    differences = sum(1 for a, b in zip(word1, word2) if a != b)
    return differences == num_transformations

class TestLadderLength(unittest.TestCase):
    def test_ladder_length_possible(self):
        self.assertEqual(ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]), 5)
        self.assertEqual(ladderLength("hot", "dog", ["hot","dog","dot"]), 3)
        self.assertEqual(ladderLength("hot", "bat", ["hit","hat","bat"]), 3)
        self.assertEqual(ladderLength("teach", "place", ["peale","wilts","place","fetch","purer","pooch","peace","poach","berra","teach","rheum","peach"]), 4)

    def test_ladder_length_not_possible(self):
        self.assertEqual(ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]), 0)
        self.assertEqual(ladderLength("hit", "lid", ["dot","dog","dig","did","lid"]), 0)
        self.assertEqual(ladderLength("hit", "lid", ["lid", "hil"]), 0)


    def test_can_transform(self):
        self.assertEqual(can_transform("hit", "hap"), False)
        self.assertEqual(can_transform("aab", "add"), False)
        self.assertEqual(can_transform("aab", "add"), False)
        self.assertEqual(can_transform("hit", "dot"), False)

        self.assertEqual(can_transform("hot", "hit"), True)
        self.assertEqual(can_transform("cot", "bot"), True)



if __name__ == '__main__':
    unittest.main(verbosity=2)