from docs import Document
class User:
    list_of_users=dict()
    def __init__(this,email,passwrd,name,age,mobile_no):
        'signs up a user'
        if email not in list_of_users.keys():
            this.email = email
            this.passwrd = passwrd
            this.name = name
            this.age = age
            this.mobile_no = mobile_n0
            this.status = 'Offline'
            this.files=[]
            list_of_users[email]=this
            this.viewing = []
        else:
            print("Already signed up")

    def login(this,passwrd):
        if this.passwrd==passwrd:
            this.status = 'Online'
            for i in viewing:
                i.count +=1 
            return True
        return False

    def logout(this):
        for i in viewing:
            i.count = max(0,i.count-1)
        viewing=[]
        this.status = 'Offline'

    def switch(this):
        this.status = 'Away'
        for i in viewing:
            i.count= max(0,i.count-1)
        
    def get_Email(this):
        return this.email
    
    def add_editors(this,file,client):
        if client not in list_of_users:
            return None
        if this.email == file.author:
            file.viewers.append(client)
            file.editors.append(client)

    def upload_file(this,file_name,shareable=False):
        file=Document(file_name,this,shareable)
        files.append(file)
        return file

    def add_viewers(this,file,client):
        if client not in list_of_users:
            return None
        if this.email == file.author:
            file.viewers.append(client)

    def open_file(this,file_name):
        if file_name not in all_files.keys():
            print("File not Found\n")
        if all_files[file_name].shareable or this in all_files[file_name].viewers:
            this.viewing.append(all_files[file_name])
        else:
            print("Not Authorized\n")

    def close_file(this,file_name):
        if file_name not in all_files.keys():
            print("File not Found\n")
        if all_files[file_name] in this.viewing:
            this.viewing.remove(all_files[file_name])
        else:
            print("File Not opened")
        
    
