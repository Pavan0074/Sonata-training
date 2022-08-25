def filerd():
    try:
        f=open('/pavan.txt', 'r')
        print(f.read())
    except(FileNotFoundError):
        return "File not exists"


