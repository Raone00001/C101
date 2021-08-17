import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A2uiLovCC43K-2p_LwxV8dTA2tj-uXT4H2XKMZmvvLF-KAGKpg7QU_wtfxJ59bK49U7WF5opqVOqS2sqLEp7ao566a3HQ6DPpnw5jWvo53B-uljw5d2t9inYjoQjvtgIutbcfvE'
    transferData = TransferData(access_token)

    #file_from = input("Enter the file path to transfer : -")
    #file_to = input("Enter the full path to upload to dropbox: -")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    file_from = 'C:/Users/Rajjo/OneDrive/Desktop/test.txt'
    file_to =  '/cuttingSound/test.txt'
    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()