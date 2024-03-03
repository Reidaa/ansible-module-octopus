from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import fetch_url
from ansible_collections.community.general.plugins.module_utils.octopus import (
    OctopusAnsible,
    octopus_auth_argument_spec,
)

# state: absent, create, present

"""
#
- name: blablabla
  reidas.octopus.environment:
    state: present
    Name:
    Slug:
    SpaceId:
    Description:

"""


def main():
    module_args: dict = octopus_auth_argument_spec()
    environment_args = dict(
        ### Body Param
        AllowDynamicInfrastructure=dict(type="bool", required=True),
        Description=dict(type="str", required=True),
        Name=dict(type="str", required=True),
        Slug=dict(type="str", required=True),
        SpaceId=dict(type="str", required=True),
        UseGuidedFailure=dict(type="bool", required=True),
        # Todo: ExtensionSettings
        ### Module Param
        operation=dict(
            type="str",
            choices=["create", "update", "read", "delete"],
            required=True,
        ),
        id=dict(type="str"),
        name=dict(type="str"),
    )

    module_args.update(environment_args)

    module = AnsibleModule(
        argument_spec=module_args,
        required_if=[
            ("operation", "create", []),
            ("operation", "update", ["id"]),
            ("operation", "read", []),
            ("operation", "delete", ["id"]),
        ],
        mutually_exclusive=[
            ["id", "name"],
        ],
    )
