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

if __name__ == "__main__":
    strs = ["end","ned", "gone", "nope", "hope","succulent", "den", "pone","luccusent"]
    print("Anagrams grouping: ", groupAnagrams(strs))