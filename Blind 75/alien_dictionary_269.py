from collections import defaultdict
class Solution:
    def alienOrder(self, words):
        # Step 1: Make the adjacency list for the characters in words
        adjacencyList = defaultdict(set)

        for word in words:
            for character in word:
                adjacencyList[character] = set()
        # Step 2: Create the graph for the alien dict
        # Take pairs of words and compare them to see what is the first differing character
        # Such that we get the information about which letter comes after which
        # So if s = "wrf" and t = "wrt", make the connection f --> t (f comes before t in that dictionary)
        for i in range(len(words)-1):
            # take pairs of words
            s, t = words[i], words[i+1]
            prefixLength = min(len(s), len(t))
            prefix_s, prefix_t = s[:prefixLength], t[:prefixLength]
            # check if two strings are almost equal, do we get a null case
            # if the input isn't valid when two strings are almost equal, it means that
            # the bigger word comes before in the pairing (s,t) and the prefixes are equal
            if (len(s) > len(t)) and prefix_s == prefix_t:
                return ""
            # continue with making the graph if not null
            # find first differing character through a loop, break when found, and then make the connection
            for j in range(prefixLength):
                if s[j] != t[j]:
                    adjacencyList[s[j]].add(t[j])
                    break
        # Step 3: Topological sort using DFS which returns bool depending on cycle detection
        visited = defaultdict(bool) # visited dictionary char: True/False
        finishTimes = [] # for storing result in stack
        def DFS_Util(character):
            if character in visited:
                return visited[character]
            visited[character] = True
            for neighbor in adjacencyList[character]:
                if DFS_Util(neighbor):
                    return True # cycle found
            finishTimes.append(character)
            visited[character] = False
        
        for character in adjacencyList:
            if DFS_Util(character):
                return "" # no order possible
        finishTimes.reverse()
        return "".join(finishTimes)

if __name__ == "__main__":
    S = Solution()
    print(S.alienOrder(["wrt","wrf","er","ett","rftt"]))