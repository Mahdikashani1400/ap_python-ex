class Folder:

    def __init__(self, command, topfolder=None):
        # topfolder =None
        self.topfolder = topfolder
        self.sub_folders = []
        self.sub_files=[]
        self.current_folder = "root"
        self.command = command


    def mkdir(self, folder_name):
      if(self.command.split()[0]!="mkdir" or len(self.command.split())>2):
          raise Exception("Invalid Command")
      else:
          if folder_name in self.sub_folders:
              raise Exception("Folder Already Exists")
          else:
           
              self.sub_folders.append(folder_name)
          
              

    def cd(self, folder_name):
        if self.command.split()[0]!="cd":
             raise Exception("Invalid Command") 
        
        if folder_name == '..':
            self.current_folder = self.sub_folders[self.sub_folders.index(self.current_folder) - 1]
        elif folder_name not in self.sub_folders:
                raise Exception('Folder Does Not Exist')
        else:
                self.current_folder = folder_name
                





        

    def touch(self, parent_folder, file_name):
      if self.command.split()[0]!="touch":
          raise Exception("Invalid Command")
  
    #   elif parent_folder not in self.sub_folders:
    #           raise Exception("Folder Does Not Exist")
    #   elif file_name in self.sub_folders:
    #       raise Exception("File Already Exists")
          
    #   else:
    #       self.sub_folders[self.sub_folders.index(parent_folder)+1] = file_name                         

    def ls(self):
        pass

    def pwd(self, folders, aim):
        pass

    def vi(self, file_name):
        pass

    def rn(self, old_name, new_name):
        pass

    def rmdir(self, folders, folder_name):
        pass

    def rm(self, folders, file_name):
        pass

    def mv(self, folders, name, destination_folder):
        pass

