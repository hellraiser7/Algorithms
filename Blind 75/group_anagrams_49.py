from collections import defaultdict

def groupAnagrams(strs):
    # first approach
    # sorting each element
    sortedStr = []
    for s in strs:
        sortedStr.append(''.join(sorted(s)))
    innerElements = []
    result = []
    freq = set()
    for i in range(len(strs)):
        if sortedStr[i] in freq:
            continue
        freq.add(sortedStr[i])
        innerElements.append(strs[i])
        for j in range(i+1, len(strs)):
            if sortedStr[i] == sortedStr[j]:
                innerElements.append(strs[j])
                freq.add(sortedStr[j])
        result.append(innerElements)
        innerElements = []
    return result

def groupAnagramsOptimized(strs):
    # use of a hashmap and some ascii shit
    frequency = defaultdict(list)
    for s in strs:
        countArray = [0]*26 # for all 16 alphabet counting
        for char in s:
            # make the frequency chart
            countArray[ord(s) - ord('a')] += 1
        frequency[tuple(countArray)].append(s) # if abc, then countArray = [1,1,1,0,0,0....0] till 26 
    return frequency.values() # same value tuples will get clubbed into one value array. Return all those strings
if __name__ == "__main__":
    strs = ["end","ned", "gone", "nope", "hope","succulent", "den", "pone","luccusent"]
    print("Anagrams grouping: ", groupAnagrams(strs))