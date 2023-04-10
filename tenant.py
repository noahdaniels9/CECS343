tenant = {}
class Tenant:
    def display_tenants():
    #Displays the dictionary that contains tenants' information
        if (len(tenant) == 0):
            print("The list is empty.")
        else:
            for i in tenant:
                print("Name:", i, ", Room number:", tenant[i])

    def add_tenant(tname, troomnum):
    #Adds tenants' information to the tenant dictionary
        tenant.update({tname: troomnum})

    def remove_tenant(remname):
    #Removes tenants' information from the tenant dictionary
        if (remname in tenant):
            tenant.pop(remname)
        else:
            print("Error: The tenant name you are looking for is not in the list.")
        
