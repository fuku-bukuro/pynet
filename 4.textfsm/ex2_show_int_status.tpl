Value PORT_NAME (\S+)
Value STATUS (\S+)
Value VLAN (\d+)
Value DUPLEX (\S+)
Value SPEED (auto|\d+)
Value PORT_TYPE (\S+)

Start
  ^Port.*Type$$ -> SearchPattern

SearchPattern
  ^${PORT_NAME}\s+${STATUS}\s+${VLAN}\s+${DUPLEX}\s+${SPEED}\s+${PORT_TYPE}\s*$$ -> Record
#Port Name Status Vlan Duplex Speed Type
#Gi0/1/0 notconnect 1 auto auto 10/100/1000BaseTX
#Gi0/1/1 notconnect 1 auto auto 10/100/1000BaseTX
#Gi0/1/2 notconnect 1 auto auto 10/100/1000BaseTX
#Gi0/1/3 notconnect 1 auto auto 10/100/1000BaseTX

