from webbrowser import Grail
class grandfather():
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername


class father(grandfather):
    def __init__(self,fathername,grandfathername):
        self.fathername=fathername
        grandfather.__init__(self, grandfathername)

class son(father):
    def __init__(self,sonname,fathername,grandfathername):
        self.sonname=sonname

        father.__init__(self,fathername,grandfathername)

def print_name(self):
    print("grandfathername:",self.grandfathername)
    print("grandfathername:", self.fathername)
    print("grandfathername:", self.sonname)


s1=son("prince","rampi","lal mani")
print(s1.grandfathername)
print_name(s1)