"""Ubuntu 16 on a d430.

Instructions:
Swap 'er in, gitter done!"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab extensions library.
import geni.rspec.emulab as emulab

pc = portal.Context()

request = pc.makeRequestRSpec()

# Node imp
node_imp = request.RawPC('imp')
node_imp.hardware_type = 'd430'
node_imp.disk_image = \
    'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD'
# node_imp.Site('Site 1')

pc.printRequestRSpec(request)

## End of file.
