#!/usr/bin/python
# coding=utf-8
import boto
import boto.ec2
from boto.ec2 import elb

class get_ec2_instacnces():
    """docstring for get_ec2_instacnces"""

    def __init__(self):
        self.conn = boto.ec2.connect_to_region('cn-north-1')
        self.elb = elb.connect_to_region('cn-north-1')

    def instance_id(self):
        ids = []
        instance_lists = self.conn.get_only_instances()
        for i in instance_lists:
            ids.append(i.id)
        return ids

    def instace_ip(self):
        ips = []
        instance_ip_list = self.conn.get_only_instances()
        for i in instance_ip_list:
            private_ip = i.private_ip_address
            public_ip = i.ip_address
            ips.append([private_ip, public_ip])
        return ips

    def instance_ip_id(self):
        ip_id = {}
        instance_ip_id = self.conn.get_only_instances()
        for i in instance_ip_id:
            private_ip = i.private_ip_address
            inst_id = i.id
            ip_id[inst_id] = private_ip
        return ip_id

    def get_all_elb(self):
        names = []
        elb_lists = self.elb.get_all_load_balancers()
        for i in elb_lists:
            names.append(i.name)
        return names

    def get_elb_instacne_attr(self, elb_name):
        elb_name_attr = []
        elb_lists = self.elb.get_all_load_balancers()
        for i in elb_lists:
            if i.name == elb_name:
                dns_name = i.dns_name
                listeners = i.listeners
                instances = i.instances
                health_check = i.health_check
                vpc_id = i.vpc_id
                subnets = i.subnets
                elb_name_attr.append([dns_name, listeners, instances, health_check, vpc_id, subnets])
        return elb_name_attr

    def deregister_elb_instance(self, elb_name, instance_id):
        elb_name.deregister_instances(instance_id)

    def register_elb_instances(self, elb_name, instance_id):
        elb_name.register_instances(instance_id)



#abc = get_ec2_instacnces()
#cc = abc.get_all_elb()
#print cc










