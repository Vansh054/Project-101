import dropbox
import os

os.system('cls')

class Uploading :
    def __init__(self,token):
        self.token = token
    
    def uploadData(self,fileFrom,fileTo):
        dbs = dropbox.Dropbox(self.token)
        f = open(fileFrom,"rb")
        dbs.files_upload(f.read(),fileTo)
        print("upload succesfully")

def main():
    acessToken = "sl.AzfbvIlyctH7SWeRpN8Di9cfwwoptaLQtQtYWEuYe4EEiED5WdBlkJQ6E6V6yEF_Khfp_Hobd-m6DWyWar9RqvY9OYnRnWlJLWVLi4opbePRBGAOnXH0wPfCLqeVNUF6NPrytqjt-3c"
    upload = Uploading(acessToken)
    ##myfile = open("C:/Users/BindassVansh/Downloads/PPTGame.pptx")
    myfile = "C:/Users/BindassVansh/Downloads/PPTGame.pptx"
    fileTo = "/Test@101/PPTGame.pptx"
    upload.uploadData(myfile,fileTo)

main()

 