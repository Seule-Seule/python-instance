import csv

def init():
    '''
    系统启动页面，包括logo 、 注册 、登录功能。
    '''
    print(" _____ _____ _   _ _      _____                                           ")
    print("/  ___|  ___| | | | |    |  ___|    * This code is o word for Password.   ")
    print("\ `--.| |__ | | | | |    | |__          * auother : seule                 ")
    print(" `--. \  __|| | | | |    |  __|             * Email : 2809713313@qq.com   ")
    print("/\__/ / |___| |_| | |____| |____                 * Blog : www.seule.cn    ")
    print("\____/\____/ \___/\_____/\_____/                     * Veision : SEULE-2.0")
    print("$ Welcome to word,you will never forget Password.")
    while True: 
        while True:       
            flag = input("$ Please Sign in(0) or Sign up(1):\n>>")
            if int(flag) == 1 or int(flag) == 0:
                break

        # 注册功能
        if int(flag) == 1:
            print("[ Sign up ]")
            user_list = []
            user_check = 1
            while user_check == 1:
                username = input("$ Please input username:\n>>")
                userpass = input("$ Plesae input password:\n>>")
                userpass2 = input("$ Please input password again:\n>>")
                if userpass != userpass2:
                    print("$ The password are diffent,please try again:")
                user_list.append(username)
                user_list.append(userpass)
                user_check = 0

            with open("user.csv","a",newline = "") as user_file:
                file_writer = csv.writer(user_file,dialect = 'excel')
                file_writer.writerow(user_list) 
      
        # 登录功能
        if int(flag) == 0:
            print("[ Sign in ]")
            while True:
                username0 = input("$ Login : ")
                password0 = input("$ password : ")
                with open("user.csv","r",encoding = "utf-8") as user_file:
                    user_reader = csv.reader(user_file)
                    user_list = [user for user in user_reader] 
                    for user1 in user_list:
                        if username0 == user1[0] and password0 == user1[1]:
                            print("$ Hello " + username0 + ", Login succ!")
                            return 
                print("$ Logon filure! Plese try again.")