# Copyright (C) 2012-2014 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import bitcoin.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.6.2-SNAPSHOT'

class MainParams(bitcoin.core.CoreMainParams):
    MESSAGE_START = b'\xaf\x45\x76\xee'
    DEFAULT_PORT = 10888
    RPC_PORT = 10889
    DNS_SEEDS = (('seed1.myriadcoin.org', 'seed2.myriadcoin.org'),
                 ('seed3.myriadcoin.org', 'seed4.myriadcoin.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':50,
                       'SCRIPT_ADDR':9,
                       'SECRET_KEY' :178}

class TestNetParams(bitcoin.core.CoreTestNetParams):
    MESSAGE_START = b'\x01\xf5\x55\xa4'
    DEFAULT_PORT = 20888
    RPC_PORT = 20889
    DNS_SEEDS = (('seed1.myriadcoin.org', 'seed2.myriadcoin.org'),
                 ('seed3.myriadcoin.org', 'seed4.myriadcoin.org'))
    BASE58_PREFIXES = {'PUBKEY_ADDR':88,
                       'SCRIPT_ADDR':188,
                       'SECRET_KEY' :239}

class RegTestParams(bitcoin.core.CoreRegTestParams):
    MESSAGE_START = b'\xfa\x0f\xa5\x5a'
    DEFAULT_PORT = 18444
    RPC_PORT = 18332
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':88,
                       'SCRIPT_ADDR':188,
                       'SECRET_KEY' :239}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
bitcoin.core.params correctly too.
"""
#params = bitcoin.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    bitcoin.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = bitcoin.core.coreparams = MainParams()
    elif name == 'testnet':
        params = bitcoin.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = bitcoin.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
