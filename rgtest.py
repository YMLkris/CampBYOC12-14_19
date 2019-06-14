import explorerhat
from time import sleep

while True:
    explorerhat.output.one.on()
    explorerhat.output.two.off()
    sleep(1)
    explorerhat.output.one.off()
    explorerhat.output.two.on()
    sleep(1)