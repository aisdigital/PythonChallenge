import datetime
import os


def wirte_to_file(output_path, data):
    date = datetime.datetime.now().isoformat()
    folderPath = f'./{output_path}'
    filePath = f'{folderPath}/results-{date}.txt'

    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    with open(filePath, mode='w') as out:
        out.write(data)

    return filePath
