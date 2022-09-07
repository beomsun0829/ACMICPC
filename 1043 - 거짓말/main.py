

from operator import truediv


people = []
PartySaver = []



def main():
    N,M = map(int,input().split())
    
    KnowTruthInput = list(map(int,input().split()))
    KnowTruthCnt = KnowTruthInput[0]
    KnowTruth = KnowTruthInput[1:]

    for _ in range(N + 1):
        people.append(False)

    for i in range(KnowTruthCnt):
        people[KnowTruth[i]] = True
        
    
    
    for _ in range(M):
        PartyInput = list(map(int,input().split()))
        PartyPeopleCnt = PartyInput[0]
        PartyPeople = PartyInput[1:]
        PartySaver.append(PartyPeople)
        
    
    
    
    for _ in range(M):
        for i in range(M):
            PartyShouldBeTrue = False
            for k in range(len(PartySaver[i])):
                if people[PartySaver[i][k]] == True:
                    PartyShouldBeTrue = True
                    break
            
            if PartyShouldBeTrue:
                for k in range(len(PartySaver[i])):
                    people[PartySaver[i][k]] = True
    
    
    
    ans = 0
    for i in range(M):
        partybreak = False
        for j in range(len(PartySaver[i])):
            if people[PartySaver[i][j]] == True:
                partybreak = True
            
        if partybreak == False:
            ans += 1
    
    print(ans)

main()