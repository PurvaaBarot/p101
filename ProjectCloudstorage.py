import dropbox 
import os
from dropbox.files import WriteMode 

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        print("Files uploaded successfully")    


        for root , dirs , files in os.walk(file_from):

            for file in files:
                local_path=os.path.join(root,file_from)
            relative_path = os.path.relpath(local_path , file_from)
            dropbox_path = os.path.join(file_to , relative_path)

            with open(local_path , 'rb' ) as f:
                dbx.files_upload(f.read() , dropbox_path , mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.A_yRaxYw-QKm9u7Pam8rRE0XN0hfW696B8Z0oPyBADMFpYHuSWFuV45TZTOxNbjSrYqochisvMbUUw4NXj2Hvc_GCXmMagzW1qxajHdvpg2O1sc7UOghSZwt8A8Leq9re_Vm5U4'
    transferData = TransferData(access_token)

    file_from = 'c:/Users/Admin/Desktop/Purvaa coding folder/P97.py'
    file_to = '/test_dropbox/P97'  
    
    transferData.upload_file(file_from, file_to)

main()     