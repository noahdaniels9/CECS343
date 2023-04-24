tenant_list = {}
class Tenant:
    def display_tenants():
    #Displays the dictionary that contains tenants' information
        if (len(tenant_list) == 0):
            print("The list is empty.")
        else:
            for i in tenant_list:
                print("Name:", i, ", Room number:", tenant_list[i])

    def add_tenant(self,name, roomnum):
        tenant_file = open(self.tenant_list_file, 'a')
        tenant_file.write(name + "\n")
        tenant_file.close()

        room_file = open(self.room_list_file, 'a')
        room_file.write(str(roomnum)+ "\n")
        room_file.close()

    def remove_tenant(self,name,room):
        with open("Tenantlist.txt", "r") as f:
            lines = f.readlines()
        with open("Tenantlist.txt", "w") as f:
            for line in lines:
                if line.strip() != name:
                    f.write(line)
        with open("Roomlist.txt", "r") as f:
            lines = f.readlines()
        with open("Roomlist.txt", "w") as f:
            for line in lines:
                if line.strip() != room:
                    f.write(line)
