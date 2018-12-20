
import csv

def password_w():
    '''
    密码写入功能。
    '''
    pass_list = []
    pass_list.append(input('$ Website  : \n>>'))
    pass_list.append(input('$ Username : \n>>'))
    pass_list.append(input('$ Password : \n>>'))
    with open("password.csv","a",newline = "") as pass_file:
        file_writer = csv.writer(pass_file,dialect = 'excel')
        file_writer.writerow(pass_list)
        print("$ The password was writeen successfully!\n")

def password_r():
    '''
    密码读取功能。
    '''
    with open("password.csv","r",encoding = "utf-8") as pass_file:
        pass_reader = csv.reader(pass_file)
        pass_list = [password for password in pass_reader]    
    for pass1 in pass_list:
        print(pass1)
    print("$ The password read complete!\n")