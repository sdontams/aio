import os
import platform 



class OsData:
    def __init__(self):
        if "posix" in os.name:
            self.name= 'Linux'
            self.version = platform.platform()
            self.distribution =  platform.release()
            self.arc = platform.machine()
            print ('linux os ', self.name, self.version, self.distribution, self.arc)
        else:
            self.name= 'Windows'
            self.version = platform.platform()
            self.distribution =  platform.release()
            self.arc = platform.machine()
            print ('Windows OS', self.name, self.version, self.distribution, self.arc)

    def getOs(self):
        return self.name

    def isSupported(self):
        if "x86" not in self.arc:
            return False
        return True 

os = OsData()


print os.isSupported()
print os.getOs()

