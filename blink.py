import explorerhat
from time import sleep


while True:

    on = explorerhat.analog.one.read()
    off = explorerhat.analog.one.read()
    if on == 0 and off == 0:
        on = .01
        off = .01

    explorerhat.output.one.on()
    sleep(on)
    explorerhat.output.one.off()
    sleep(off)
    print(on, off)
