#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Koha-Suomi Oy
#
# This file is part of Ansible-NetVisibility
#

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}


DOCUMENTATION = '''
---
module: netvisibility
author: "Olli-Antti Kivilahti (olli-antti.kivilahti@jns.fi)"
version_added: "2.4"
short_description: Identify how two devices should communicate
requirements: [ ]
description:
    - Detect network information needed for two different devices through various network layers
options:
    server_ips:
        required: true
        description:
            - IP-addresses of the server.
    client_ips:
        required: true
        description:
            - IP-addresses of the client.
    connection:
        required: true
        choices: [ public, intra, local, socket ]
        description:
            - The outermost network segment these two devices communicate through.
'''

EXAMPLES = '''
# Example netvisibility command from Ansible Playbooks
- netvisibility:
    name: somegroup
    state: present
'''

RETURN = '''
---
server:
  description: Server network information visible from the client
  type: complex
  returned: always
  contains:
    ip:
      sample: 10.110.249.32
    hostname:
      sample: piika.pohjoiskarjala.net
   address:
      description: hostname is not always available so this is the hostname or the ip
      sample: piika.pohjoiskarjala.net || 10.110.249.32
client:
  description: Client network information visible from the server
  type: complex
  returned: always
  contains:
    ip:
      sample: 10.110.249.30
    hostname:
      sample: renki.pohjoiskarjala.net
   address:
      description: hostname is not always available so this is the hostname or the ip
      sample: renki.pohjoiskarjala.net || 10.110.249.30
'''

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec = dict(
            server_ips   = dict(required=True),
            client_ips   = dict(required=True),
            connection   = dict(required=True, choices=['public', 'intra', 'local', 'socket']),
        ),
        supports_check_mode=True
    )

    if module.check_mode:
        # Check if any changes would be made but don't actually make those changes
        module.exit_json(changed=False)








if __name__ == '__main__':
    main()

