import _winreg


def dump_sid_users():

    users = []
    query = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList', 0)
    i = 0

    try:
        while True:
            key = _winreg.EnumKey(query, i)
            query2 = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList' + '\\' + key, 0)
            profile = _winreg.QueryValueEx(query2, 'ProfileImagePath')[0].split('\\')
            user = [key, profile[len(profile) - 1]]
            users.append(user)
            i += 1

    except WindowsError, ex:
        pass

    return users


def find_username_by_sid(sid):

    users = dump_sid_users()
    username = ''
    try:
        for i in range(0, len(users)):
            if users[i][0] == sid:
                username = users[i][1]
    except WindowsError, ex:
        pass

    return username