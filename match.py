import copy

class Match:

    def __init__(self, person, listOfAllPeople):
        self.person = person
        self.people = listOfAllPeople

    # def __eq__(self, other):
    #     if not isinstance(other, Match):
    #         return NotImplemented

    #     return self.
    # 0<=i<len(points)

    def bubbleSort(self, points, copyPoints, copyPeople, recommended):
        for passnum in range(len(points)-1,-1,-1):
            for i in range(passnum):
                if points[i]<points[i+1]:
                    temp = points[i]
                    points[i] = points[i+1]
                    points[i+1] = temp

        for i in range(0, len(points)):
            for j in range(0, len(copyPoints)):
                if points[i] == copyPoints[j]:
                    recommended.append(copyPeople[j])
                    copyPoints[j] = -1
        
        return recommended

    def match(self):
        copyPeople = []
        counter = 0
        recommended = []
        pri = self.person.getPriority()

        for person in self.people:
            if person != self.person:
                copyPeople.append(person)
    
        copyPeople = copy.deepcopy(copyPeople)

        points = [0]*len(copyPeople)
        copyPoints = [0]*len(copyPeople)

        for indiv in copyPeople:
            if self.person.getYear() == indiv.getYear():
                if pri == 1:
                    points[counter] += 5
                    # copyPoints[counter] += 5
                else:
                    points[counter] += 1
                    # copyPoints[counter] += 1

            if self.person.getMajor() == indiv.getMajor():
                if pri == 2:
                    points[counter] += 5
                    # copyPoints[counter] += 5
                else:
                    points[counter] += 1
                    # copyPoints[counter] += 1

            if self.person.getConcen() == indiv.getConcen():
                if pri == 3:
                    points[counter] += 5
                    # copyPoints[counter] += 5
                else:
                    points[counter] += 1
                    # copyPoints[counter] += 1

            for course in self.person.getClasses():
                for coursee in indiv.getClasses():
                    if course == coursee:
                        if pri == 4:
                            points[counter] += 5
                            copyPoints[counter] += 5
                        else:
                            points[counter] += 1
                            # copyPoints[counter] += 1

            for interest in self.person.getInterests():
                for interestt in indiv.getInterests():
                    if interest == interestt:
                        if pri == 5:
                            points[counter] += 5
                            # copyPoints[counter] += 5
                        else:
                            points[counter] += 1
                            # copyPoints[counter] += 1

            counter += 1
        
        copyPoints = copy.deepcopy(points)
        return self.bubbleSort(points, copyPoints, copyPeople, recommended)