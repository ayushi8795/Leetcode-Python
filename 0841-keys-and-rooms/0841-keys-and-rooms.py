class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keyAcq = []
        n = len(rooms)
        InitialRoom = 0
        visitedRoom = set()
        keyAcq.append(InitialRoom)

        while len(keyAcq) > 0:
            roomNumber = keyAcq.pop(0)
            visitedRoom.add(roomNumber)
            for key in rooms[roomNumber]:
                if key not in visitedRoom:
                    keyAcq.append(key)
        
        return len(visitedRoom) == len(rooms)
