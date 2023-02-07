import pytest
from Level1.SystemDriveFinder import SystemDriveFinder
from Level1.Searchfile import Filefinder
class Test_Drive:
    def test_Drivecase(self):
        obj=SystemDriveFinder()
        self.expected=obj.find_drives()
        self.actual=['C']
        assert self.expected==self.actual
    def test_searchfiles(self):
        obj=Filefinder()
        d = obj.find_file('SystemDriveFinder.py','C:/')
        act=['C:/Users\\user785\\PycharmProjects\\Team-1\\Level1\\SystemDriveFinder.py']
        self.expected_filename = act
        self.actual_res=d
        assert self.expected_filename==self.actual_res

