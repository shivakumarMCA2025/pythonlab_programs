class organization:
    def org_name(self):
        self.organization_name=input("enter organization name:")


class security_team(organization):
    def sec_name(self):
        self.security_name=input("enter security team name:")

class security_analyst(security_team):
    def display(self):
        print("organization name:",self.org_name)
        print("security team name:",self.sec_name)
        print("security analyst name:",self.ana_name)
        print("role",self.role)


s=security_analyst