ten = {}
class Tenant:
    def display_tenants():
        if (len(ten) == 0):
            print("The list is empty.")
        else:
            for i in ten:
                print("Name:", i, ", Room number:", ten[i])

    def add_tenant(tname, troomnum):
        ten.update({tname: troomnum})

    def remove_tenant(remname):
        if (remname in ten):
            ten.pop(remname)
        else:
            print("Error: The tenant name you are looking for is not in the list.")
        
