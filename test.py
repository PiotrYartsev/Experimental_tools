#find out when file was created
from rucio.client import Client
from rucio.common.exception import RucioException
from rucio.common.utils import generate_uuid

import sys
import os
import time
import sys

CLIENT = Client()

print(CLIENT.ping())

#print(CLIENT.get_metadata(scope="mc20", name="mc_v9-8GeV-1e-inclusive_1000_t1588350689.root"))
os.system("cd; cd rucio-client-venv/bin; source activate")
L=os.popen("rucio get-metadata mc20:mc_v9-8GeV-1e-inclusive_1000_t1588350689.root").read()

L2=L.split("\n")
L2=[s.strip('\n') for s in L2]
L3=[s.split(":") for s in L2]

print(L3)