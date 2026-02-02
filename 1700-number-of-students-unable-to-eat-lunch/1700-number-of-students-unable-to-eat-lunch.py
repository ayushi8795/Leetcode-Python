class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        unableToServe = 0
        
        while len(students) > 0 and len(students) > unableToServe:
            # reset unableToServe because we served the student because top of sandwiche matched the student's preference
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                unableToServe = 0
            else:
                # Increment unableToServe to keep traack of how many students we offered the top of sandwhich
                students.append(students.pop(0))
                unableToServe = unableToServe+1
    
        return len(students)