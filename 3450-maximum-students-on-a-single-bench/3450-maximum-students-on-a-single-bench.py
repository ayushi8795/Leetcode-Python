class Solution:
    def maxStudentsOnBench(self, students: List[List[int]]) -> int:
        has = {}

        for stu in students:
            stu_id = stu[0]
            bench_id = stu[1]

            if bench_id in has and stu_id not in has.values():
                has[bench_id].add(stu_id)
            elif bench_id not in has and stu_id not in has.values():
                has[bench_id] = {stu_id}

        maxlen = 0
        if has:
            for key, value in has.items():
                maxlen = max(maxlen,len(value))
        return maxlen

