ten = {}
class Tenant:
    def display_tenants():
    #Displays the dictionary that contains tenants' information
        if (len(ten) == 0):
            print("The list is empty.")
        else:
            for i in ten:
                print("Name:", i, ", Room number:", ten[i])

    def add_tenant(tname, troomnum):
    #Adds tenants' information to the tenant dictionary
        ten.update({tname: troomnum})

    def remove_tenant(remname):
    #Removes tenants' information from the tenant dictionary
        if (remname in ten):
            ten.pop(remname)
        else:
            print("Error: The tenant name you are looking for is not in the list.")
        
