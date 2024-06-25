import os

class Cluttermanagement:
    def __init__(self, v, r, t, s):
        self._v = v
        self._r = r
        self._t = t
        self._s = s

    def comp(self):
        # Source file path
        source = f'{self._t}/{self._r[self._v]}'
        # destination file path
        dest = f'{self._t}/{self._v}.{self._s}'
        # Now rename the source path
        os.rename(source, dest)
        print("Source path renamed to destination path successfully.")


def current_path():
    print("currently working path")
    print(os.getcwd())
    print()


def forimages():
    pass


current_path()
os.chdir("./testing")
current_path()
path = current_path()
dir_list = os.listdir(path)
print("files and directories in '", path, "' :")
print(dir_list)
for_image = "jpg"

for_video = "mp4"

for_pdf = "pdf"
v = len(dir_list)
print(v)
for i in range(v):
    if ".jpg" in dir_list[i]:
        maint = Cluttermanagement(i, dir_list, os.getcwd(), for_image)

        print("yes")
        maint.comp()
        i = i + 1


    elif".mp4" in dir_list[i]:

        maint = Cluttermanagement(i, dir_list, os.getcwd(), for_video)

        print("done")
        maint.comp()
        i = i + 1

    elif ".pdf" in dir_list[i]:

        maint = Cluttermanagement(i, dir_list, os.getcwd(), for_pdf)

        print("done")
        maint.comp()
        i = i + 1

    else:
        print("not done")
    #
