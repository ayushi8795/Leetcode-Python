import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    colums = ['student_id','age']
    df = pd.DataFrame(student_data, columns = ['student_id','age'])
    return df