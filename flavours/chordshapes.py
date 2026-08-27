from typing import List

class Solution:
    def countShapes(self, chords: List[List[int]]) -> int:
        hashmap = {}

        for chord in chords:
            label = []
            for note in chord:
                label.append(note - chord[0])
            
            index = tuple(label)
            if index in hashmap:
                hashmap[index].append(chord)
            else:
                hashmap[index] = [label]
        
        return len(hashmap)