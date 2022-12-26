
scp -r -i ./putty_keys/privateopen ./project pi@ISCPowertrain.local:ISC/project

scp -i ./putty_keys/privateopen ./files/config.txt pi@ISCPowertrain.local:
PAUSE

ssh -i ./putty_keys/privateopen pi@ISCPowertrain.local sudo cp config.txt /boot
PAUSE

ssh -i ./putty_keys/privateopen pi@ISCPowertrain.local sudo rm config.txt
PAUSE