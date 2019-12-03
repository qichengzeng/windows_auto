import os
srcpath=r"E:\study\a"
despath=r"E:\study\b"
def copy(srcpath,despath):
    if os.path.isdir(srcpath) and os.path.isdir(despath):
       name_list=os.listdir(srcpath)
       for file in name_list:
           if  not os.path.isdir(os.path.join(srcpath,file)):
               with open(os.path.join(os.path.join(srcpath,file)),"rb") as rstream:
                   text=rstream.read()
                   with open(os.path.join((os.path.join(despath,file))),"wb") as wstream:
                       wstream.write(text)
           else:
               os.mkdir(os.path.join(despath,file))
               chsrcpath=(os.path.join(srcpath,file))
               chdespath=(os.path.join(despath,file))
               copy(chsrcpath,chdespath)
       else:
           print("复制完成")
    else:
        print("请上传一个文件夹路径而不是文件")
def register():
    username=input("请输入用户名:")
    password=input("请输入密码:")
    re_password=input("请确认密码:")
    if username and password:
        if password==re_password:
            with open(r"E:\study\a\user.txt","a") as wstream:
                user_text="{} {}\n".format(username,password)
                wstream.write(user_text)
                print("注册成功")
        else:
            print("两次密码输入不一致")
    else:
        print("请输入用户名或密码")
def login():
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username and password:
            user_text = "{} {}\n".format(username,password)
            with open(r"E:\study\a\user.txt","r") as  rstream:
                read_text=rstream.readlines()
                for user in read_text:
                    if user==user_text:
                        print("登录成功")
                        return True,username
                else:
                    print("请先注册")

    else:
        print("请输入用户名或密码")
def do_books():
    islogin=False
    switch=input("如果已经注册，输入—登录—进入到登录界面，否则输入-注册-进入注册页面:")
    if switch=="登录":
        islogin=login()[0]
    elif switch=="注册":
        register()
        islogin=login()[0]
    else:
        print("输入错误")
    if islogin:
        with open("E:\study\\a\\books.txt","r") as wstream:
            global books
            books=wstream.readline()
            print(books)
        #     print("图书馆收藏的图片列表：")
        #     for book in books:
        #         print(book,end="")
        # book_name=input("\n请输入图书名字借走你想用的书本:")
        # new_boo_name=book_name
        # print(new_boo_name)
        # print(books)
        # for book in books:
        #     if book==new_boo_name:
        #         books.remove(new_boo_name)
        # else:
        #     print("图书馆中没有这本书")
        # with open(r"E:\study\a\books.txt", "w") as wstream:
        #     wstream.writelines(books)
with open(r"E:\study\a\books.txt","w") as rstream:
      a=["1\n"]
      rstream.writelines(a)
      print(rstream.tell())
