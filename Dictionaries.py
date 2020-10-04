#https://www.hackerrank.com/challenges/sparse-arrays/problem

def matchingStrings(strings, queries):
    qdict = {}
    result = []
    for q in queries:
        qdict[q] = 0
        
    for s in strings:
        if s in qdict:
            qdict[s] +=1

    for q in queries:
        result.append(qdict[q])
    return result
