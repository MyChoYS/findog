

class Member :
    def __init__(self, member_id, member_pwd, member_name, member_home, member_cellphone):
        self.member_id = member_id;
        self.member_pwd = member_pwd
        self.member_name = member_name
        self.member_home = member_home
        self.member_cellphone = member_cellphone

    def __str__(self):
        return self.member_id + ' ' + self.member_pwd + ' ' + self.member_pwd + ' ' + self.member_home + ' ' + self.member_cellphone
