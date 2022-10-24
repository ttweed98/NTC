## This script demos input parameters as well as CLI parameters using sys.argv
import sys
import argparse

"""The next print is a global command Any time this file is imported into another script, the print output will be displayed"""
print("This line will always print- when called directly or imported")

"""Lines 9 thru 22 serve as a good function demo. Turn off return and observe output"""
def get_interface_type(interface):
    if interface.lower().startswith('et'):
        iftype = 'ethernet'
    elif interface.lower().startswith('vl'):
        iftype = 'vlan'
    elif interface.lower().startswith('lo'):
        iftype = 'loopback'
    elif interface.lower().startswith('po'):
        iftype = 'portchannel'
    else:
        iftype = 'unknown'
    

    return iftype



if __name__=="__main__":
    """simple function call"""
    # intf_type = get_interface_type('vlan200')
    # print(intf_type)

    """Function calls within a FOR loop"""
    # interfaces = ['GigabitEthernet2', 'loopback20', 'mgmt0']
    # for each_interface in interfaces:
    #     intf_type = get_interface_type(each_interface)
    #     print(intf_type)


    """Next 3 lines will accept interface name as input to the question upon execution"""
    # intf = input('Please enter the name of the interface: ') 
    # int_type = get_interface_type(intf)
    # print(int_type)
    
    """ Next 3 lines are used to show how we can get CLI arguments using sys.argv"""
    # intf = sys.argv[1]
    # int_type = get_interface_type(intf)
    # print(int_type)

    """These lines serve as a demo of argparse """
    # parser = argparse.ArgumentParser(description= 'DEMO for ARGPARSE')
    # parser.add_argument("-i", '--interface', help = 'Interface name', required = True)
    # parser.add_argument('-p','--print', help='specify if you want the interfacetype printed', type=bool, default = False)
    #parser.add_argument('-p','--print', action = 'store_true', help='specify if you want the interfacetype printed' )

    # args = parser.parse_args()

    # intf = args.interface # Gets the name of the interface from the interface argument
    # print(intf)
    # int_type = get_interface_type(intf)

    # printTrueorFalse = args.print # gets whether the print attribute is set to True or False
    # if printTrueorFalse:
    #     print(f' The interface type is {int_type}')

    

    


