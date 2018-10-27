from easysnmp import Session
import sqlite3
ip='192.168.184.98'
vl=10
session=Session(hostname=ip,community='public',version=2)
macs=session.walk(".1.3.6.1.2.1.17.4.3.1.1")
ports=session.walk(".1.3.6.1.2.1.17.4.3.1.2")
connection = sqlite3.connect(':memory')
cursordata=connection.cursor()
createtable="CREATE TABLE IF NOT EXISTS project(PORTS, VLAN, MACS,IP)"
cursordata.execute(createtable)
for x,y in zip(ports,macs):
    oid=y.oid
    oid_index=y.oid_index
    snmp_type=y.snmp_type
    mac=y.value
    port=x.value
    print ip, mac, port
    cursordata.execute("INSERT INTO project(PORTS,VLAN,MACS,IP) VALUES(?,?,?,?)",(port,vl,mac,ip)
    connection.commit()
connection.close()
