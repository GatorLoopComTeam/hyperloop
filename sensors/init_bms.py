import socket
import constants
import re
import datetime


def init_bms(pod_data, sql_wrapper, logging):
    logging.debug("About to init BMS")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', constants.BMS_PORT))
    bms_v_val = 0
    bms_vs_val = 0
    while True:
        bms_recv = sock.recvfrom(1024)[0]

        if bms_recv[0:2] == 'V\t':
            bms_v_val = int(re.match('.*\t([0-9]*)', bms_recv).group(1))

        elif bms_recv[0:2] == 'VS':
            bms_vs_val = int(re.match('.*\t([0-9]*)', bms_recv).group(1))

        # TODO add the correct battery voltages as parameters
        if bms_v_val > 30000 and bms_v_val < 45000 and bms_vs_val > 30000 and bms_vs_val < 45000:
            pod_data.v_val = bms_v_val
            pod_data.vs_val = bms_vs_val
            logging.debug("BMS initialized with voltage %d and %d",(bms_v_val,bms_vs_val))
            sql_wrapper.execute("INSERT INTO bms VALUES (%s,%s,%s)", (datetime.datetime.now(), bms_v_val, bms_vs_val))
            return 1
        # compare to >1 to make sure it isn't just an uninitialized 0
        elif bms_v_val > 1 and bms_v_val <= 30000 and bms_vs_val > 1 and bms_vs_val <= 30000:
            logging.debug("FAULT: BMS initialized with voltage %d and %d" % (bms_v_val,bms_vs_val) )
            pod_data.state = 0


        # bms_recv = int(sock.recvfrom(1024)[0])
        # if bms_recv>12000 and bms_recv<18000:
        # 	pod_data.voltage = bms_recv
        # 	logging.debug("BMS initialized with voltage "+str(bms_recv))
        # 	return 1
        # elif bms_recv>5000 and bms_recv<=12000:
        # 	logging.debug("Potential low battery, BMS indicated voltage " + str(bms_recv))
