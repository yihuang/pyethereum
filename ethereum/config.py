import utils
from ethereum.db import BaseDB
import time
from utils import address, int256, trie_root, hash32, to_string, \
    sha3, zpad, normalize_address, int_to_addr, big_endian_to_int, \
    int_to_big_endian

# List of system addresses and global parameters
SYS = int_to_addr(10)
STATEROOTS = int_to_addr(20)
BLKNUMBER = int_to_addr(30)
ETHER = int_to_addr(50)
CASPER = int_to_addr(60)
ECRECOVERACCT = int_to_addr(70)
PROPOSER = int_to_addr(80)
RNGSEEDS = int_to_addr(90)
BLOCKHASHES = int_to_addr(100)
GENESIS_TIME = int_to_addr(110)
LOG = int_to_addr(120)
BET_INCENTIVIZER = int_to_addr(150)
EXECUTION_STATE = int_to_addr(160)
TX_ENTRY_POINT = int_to_addr(2**160 - 1)
TXGAS = 1
TXINDEX = 2
GAS_REMAINING = 3
BLOOM = 2**32
GASLIMIT = 4712388 # Pau million
NULL_SENDER = int_to_addr(0)
BLKTIME = 3.5
# Note that this parameter must be set in the Casper contract as well
ENTER_EXIT_DELAY = 110
# Note that this parameter must be set in the Casper contract as well
VALIDATOR_ROUNDS = 5
# Number of shards
MAXSHARDS = 65536
SHARD_BYTES = len(int_to_big_endian(MAXSHARDS - 1))
ADDR_BYTES = 20 + SHARD_BYTES
ADDR_BASE_BYTES = 20
UNHASH_MAGIC_BYTES = 'unhash:'
