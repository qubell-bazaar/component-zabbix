import os
import requests

from qubell.api.testing import *

destroy_interval = int(os.environ.get('DESTROY_INTERVAL', 1000*60*60*2))

class ZabbixServerTestCase(BaseComponentTestCase):
    meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml'))

    @classmethod
    def timeout(cls):
        return 120 

    def call_zabbix_agent_host_screen(self, instance):
        host = instance.returnValues['endpoints.agent-screens'][0]
        resp = requests.get(host, verify=False)
        assert resp.status_code == 200

class ZabbixAgentLinuxTestCase(ZabbixServerTestCase):
    name = "Zabbix Agent App"
    apps = [
        {"name": name,
         "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../zabbix-agent-app.yml')),
	 "settings": {"destroyInterval": destroy_interval},
         "parameters": { "input.image": { "ami": "us-east-1/ami-8997afe0", "user": "root", "type": "linux", "hw": "m1.small" }} 
        },
        {"name": "Zabbix Server",
         "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../component-zabbix.yml'))}
    ]

    @instance(byApplication=name)
    def test_zabbix_agent_host_screen(self, instance):
        self.call_zabbix_agent_host_screen(instance)

class ZabbixAgentWindowsTestCase(ZabbixServerTestCase):
    name = "Zabbix Agent App"
    apps = [
        {"name": name,
         "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../zabbix-agent-app.yml')),
	 "settings": {"destroyInterval": destroy_interval},
         "parameters": { "input.image": { "ami": "us-east-1/ami-31620c54", "user": "Administrator", "type": "windows", "hw": "m3.large"  }}
        },
        {"name": "Zabbix Server",
         "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../component-zabbix.yml'))}
    ]

    @instance(byApplication=name)
    def test_zabbix_agent_host_screen(self, instance):
        self.call_zabbix_agent_host_screen(instance)
