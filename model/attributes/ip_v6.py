"""
DCSO TIE2MISP Parser
Copyright (c) 2017, DCSO GmbH
"""
import datetime
from model import MISPAttribute


class IPv6(MISPAttribute):
    def __init__(self):
        MISPAttribute.__init__(self)
        self.data_type = "IPv6"

    def serialize(self):
        dt = datetime.datetime.now()
        json_object = dict()
        json_object['category'] = 'Network activity'
        json_object['comment'] = self.comment
        json_object['uuid'] = self.id
        json_object['timestamp'] = dt.strftime("%s")
        json_object['to_ids'] = True
        #json_object['value'] = self.value.replace('/32', '')
        json_object['value'] = self.value
        json_object['type'] = 'ip-dst'

        return json_object
        # return {'category': 'Network activity', 'comment': self.data_type + ' - Confidence: ' +
        #        self.confidence, 'uuid': self.id, 'timestamp': dt.strftime("%s"), 'to_ids': 'true',
        #        'value': self.value, 'type': 'ip-dst'}

    @staticmethod
    def parse(item):
        ipv6 = IPv6()
        ipv6.actors = item["actors"]
        ipv6.families = item["families"]
        ipv6.value = item["value"]
        ipv6.id = item["id"]
        ipv6.severity = item["max_severity"]
        ipv6.confidence = item["max_confidence"]
        return ipv6

    def upload(self, misp, event):
        misp.add_ipdst(event, self.value, self.category, True, self.comment, None, False)



