#!/usr/bin/python
# conding = utf-8

import boto.ec2
from ec2info import instance
import os

###SET ENV
ELB_INSTANCE_NAME = 'docker-instance'
WORKDIR = '/data/html/'
S3 = 'add'
Pattern = 'code'

def list_elb_name():
    names = {}
    elb_names_ = instance.get_ec2_instacnces()
    elb_names = elb_names_.get_all_elb()
    lenth = len(elb_names)
    for i in range(lenth):
        names[i] = elb_names[i]
    for i in range(lenth):
        print i, '=', names[i]
    return names


def input_num():
    names = list_elb_name()
    names
    try:
        argv = int(raw_input('Please input the num: '))
        lenth = range(len(names.keys()))
        if argv not in lenth:
            print "Please Input correct number! "
            print lenth
            exit(8)
        print "You Input %d,chose elb_instance name is %s" % (argv, names[argv])
    except ValueError as e:
        print "Please In put over num !!! "

    return names[argv]


def get_elb_instance_member():
    retries_nums = 0
    elb_name = input_num()
    ids = []
    mem_info = {}
    elb_name_attrs = instance.get_ec2_instacnces()
    elb_name_attr = elb_name_attrs.get_elb_instacne_attr(elb_name)
    for i in elb_name_attr[0][2]:
        ids.append(i.id)
    mem_info[elb_name] = ids
    print elb_name_attr
    while retries_nums < 3:
        data = raw_input("Please Input (Y|y/N|n) to make sure you want to update the ELB-INSTANCE: ")
        if data in ['Y', 'y']:
            return mem_info
        elif data in ['N', 'n']:
            print "exit!"
            exit(8)
        else:
            retries_nums += 1

def upgrate():
    print "Start upgrate.......!"
    member_info = get_elb_instance_member()
    fa = instance.get_ec2_instacnces()
    ip_id = fa.instance_ip_id()
    #print ip_id
    elb_name = member_info.keys()
    ids = member_info.values()[0]
    start = instance.get_ec2_instacnces()
    for i in ids:
        print "Start Upgrate %s" % (i,)
        print "IP Address is %s" % (ip_id[i],)
        #start.deregister_elb_instance(elb_name, i)
        cmd = 'ansible %s -m ping ' % (ip_id[i],)
        result = os.system(cmd)
        print result













if __name__ == '__main__':
    upgrate()
