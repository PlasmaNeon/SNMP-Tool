import os

def main():
    host = '192.168.233.129'
    oid = input('Please input OID:\n')
    result=os.popen('snmpwalk -v 2c -c public '+host+' '+oid).read()
    print(result)


if __name__=='__main__':
    main()
