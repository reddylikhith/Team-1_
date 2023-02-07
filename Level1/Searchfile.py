import os
class Filefinder:
    def __init__(self):
        pass
    def find_file(self,filename,filepath):
        files=[]
        self.filename=filename
        self.filepath=filepath
        for root,dir,file in os.walk(filepath):
            if filename in file:
                files.append(os.path.join(root,filename))
        return files
if __name__=='__main__':
    obj=Filefinder()
    print(obj.find_file('SystemDriveFinder.py','C:/'))