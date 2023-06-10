"""
Implement rye_discovery config for tox.ini
and set VIRTUALENV_DISCOVERY as required.

This file is ready to become a tox plugin.
"""

import logging

from tox.plugin import impl
from tox.session.state import State
from tox.config.sets import ConfigSet, EnvConfigSet


_RYE_DISCOVERY_CONF = 'rye_discovery'


@impl
def tox_add_core_config(core_conf: ConfigSet, state: State):
    "tox section config for rye_discovery"
    core_conf.add_config(
        _RYE_DISCOVERY_CONF,
        of_type=bool,
        default=False,
        desc="If True, enable rye virtualenv discovery",
    )


@impl
def tox_add_env_config(env_conf: EnvConfigSet, state: State):
    "testenv section config for rye_discovery"
    # per-env default is tox setting
    env_conf.add_config(
        _RYE_DISCOVERY_CONF,
        of_type=bool,
        default=state.conf.core[_RYE_DISCOVERY_CONF],
        desc="If True, enable rye virtualenv discovery",
    )

    if env_conf[_RYE_DISCOVERY_CONF]:
        logging.getLogger(__name__).info("Using virtualenv discovery = rye")
        env_conf["set_env"].update({"VIRTUALENV_DISCOVERY": "rye"})
