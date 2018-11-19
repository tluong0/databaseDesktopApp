import backend

from datetime import datetime as dt


today = dt.today()

current_test_files = backend.search("", "", "Test")


def get_info():
    files_need_updated = []
    for file in current_test_files:
        file_date = dt.strptime(file[4], "%m/%d/%y")
        if (abs(today - file_date)).days==0:
            files_need_updated.append(file)
    return files_need_updated




