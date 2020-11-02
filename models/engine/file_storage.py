#!/usr/bin/python3
'''module used to store data'''

class FileStorage:
  '''class for serialization and deserialization'''
  __file_path = "file.json" ##this have to be a string variable type
  __object = {} ### disctionary type object
  
  def all:
    '''returns objects'''
    return self.object

  def new(self, obj):
  '''method to set new object in __object vriable'''
  self.__object["{}.{}".format(obj.__class__.__name__, obj.id)] = obj
