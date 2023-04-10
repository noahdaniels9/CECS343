tenant_list = {}
class Tenant:
    def display_tenants():
    #Displays the dictionary that contains tenants' information
        if (len(tenant_list) == 0):
            print("The list is empty.")
        else:
            for i in tenant_list:
                print("Name:", i, ", Room number:", tenant_list[i])

    def add_tenant(tname, troomnum):
    #Adds tenants' information to the tenant dictionary
        tenant_list.update({tname: troomnum})

    def remove_tenant(remname):
    #Removes tenants' information from the tenant dictionary
        if (remname in tenant_list):
            tenant_list.pop(remname)
        else:
            print("Error: The tenant name you are looking for is not in the list.")
        
