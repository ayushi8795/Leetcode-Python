class Solution:
    def uniqueEmailGroups(self, emails: list[str]) -> int:
        
        unique = set()

        for em in emails:
            normalised, domainname = em.split('@')
            normalised = normalised.replace(".","")
            if "+" in normalised:
                indexofSymbol = normalised.index("+")
                normalised = normalised[:indexofSymbol]
            unique.add(normalised.lower()+"@"+domainname.lower())
        print(unique)
        return len(unique)