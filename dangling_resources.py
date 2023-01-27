import elb
import ebs
import sg
import eip
import eni

def principal():
    elb.elb()
    ebs.ebs()
    sg.sg()
    eip.eip()
    eni.eni()
