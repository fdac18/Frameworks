from io import IOBase


class GitLineReader:

    def __init__(self, filename: str = '') -> 'Initializes a Class of Type DataReader from a filename':
        assert isinstance(filename, str)
        self.linecount = 0
        self.filename = filename
        self.blob: str = ''
        self.commithash: str = ''
        self.repo: str = ''
        self.time: str = ''
        self.author: str = ''
        self.dependencies: list = ()
        try:
            self.datafile: IOBase = open(filename, 'r')
        except IOError:
            print('Bad File given to DataReader!')
            self.error: int = 1
            self.active: bool = False
            return
        self.error: int = 0
        self.active: bool = True

    def get_new_line(self):
        assert isinstance(self.datafile, IOBase)
        if not self.active:
            print('Data Reader is out of lines')
            return
        try:
            fileline = self.datafile.readline()
            if not fileline:
                print('Empty line encountered')
                self.datafile.close()
                self.active = False
                return
            linetokens = fileline.split(';')
            self.commithash = linetokens[0]
            self.blob = linetokens[1]
            self.repo = linetokens[2]
            self.time = linetokens[3]
            self.author = linetokens[4]
            if linetokens[5]:
                self.dependencies = linetokens[5:]
            self.linecount += 1
            return
        except Exception as err:
            print(err)
            self.datafile.close()
            self.active = False
            return


thefile = input('Select a file to parse: ')
thereader = GitLineReader(thefile)
while thereader.active:
    thereader.get_new_line()
    if not thereader.active:
        break
    print(thereader.repo, '\n\t', thereader.time, '\n\t', thereader.author)
    for dependant in thereader.dependencies:
        print('\t\t', dependant)
print('Total data lines read: ', thereader.linecount)
exit(0)
