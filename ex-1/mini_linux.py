class Folder:

    def __init__(self, command, topfolder):
        topfolder =None
        self.command = command
        self.topfolder = topfolder
        self.sub_folders = [
            #  {
            #     mainfolder="s",  
            #  },
             
        ]
        self.sub_files=[]
        self.current_folder = "root"


    def mkdir(self, folder_name):
        if(self.command==
          'mkdir' ):
                
                if(folder_name in self.sub_folders):
                    self.folder_name =  folder_name
                    raise Exception("Folder Already Exists")
                else:
                        self.sub_folders += [folder_name]
        else:
            Exception("Invalid Command")
             
                                         

                    
                    
           


    def cd(self, folder_name):
        
        pass

    def touch(self, parent_file, file_name):
        pass

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

# test = Folder('hello','po')
# test.mkdir('tt')
# print(1 in [1,2,3])

# a = {"a"}