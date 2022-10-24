def verify_vlan(vlan_id, vlan_name):
    print(f' The vlan id is {vlan_id} and vlan_name is {str(vlan_name)}')

verify_vlan(10, 30) # Fn execution will return an error if vlan_name is not given

def verify_vlan1(vlan_id, vlan_name = 'PROD'):
    print(f' The vlan id is {vlan_id} and vlan_name is {vlan_name}')

verify_vlan1(10) # Fn executes successfully since vlan_name has a default value


