import pandas as pd

df = pd.read_csv('data.csv')


def repMaxList(lift:str)-> list:
    filtered_df = df[df.iloc[:, 2] == lift]
    weightReps = filtered_df.iloc[:, 3:5].values.tolist()
    
    # Reverse the lists so that the newest data is first
    weightReps = weightReps[::-1]

    
    formattedData = []
    for index, value in enumerate(weightReps):
        # NaN Check
        if repMax(value) == repMax(value):
            formattedData.append(repMax(value))

    return formattedData

def dateList(lift:str)-> list:
    filtered_df = df[df.iloc[:, 2] == lift]
    date = filtered_df.iloc[:, 0].values.tolist()
    
    # Reverse the lists so that the newest data is first
    date = date[::-1]

    return date

def repMax(weightReps:list)->int:
    return (0.033 * weightReps[0] * weightReps[1]) + weightReps[0]


print(dateList('Bench Press'))