def filerd():
    try:
        f=open('E:\pavan\Sonatatraining-python\pavan.txt','r')
        print(f.read())
    except(FileNotFoundError):
        return "File not exists"


