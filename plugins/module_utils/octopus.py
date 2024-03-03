def octopus_auth_argument_spec():
    return dict(
        api_token=dict(
            type="str",
            required=True,
            no_log=True,
        ),
    )
