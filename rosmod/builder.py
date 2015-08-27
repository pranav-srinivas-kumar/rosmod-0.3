# ROSMOD Builder
# Author: Pranav Srinivas Kumar
# Date: 2015.07.23

import json, jsonpickle
import classes

with open('model.txt', 'r') as input_model:
    decoder_output = jsonpickle.decode(input_model.read())
    print "Done decoding"
#    print decoder_output.children._cardinality[str(type(Hardware()))]
    print type(decoder_output)
    print decoder_output

    # The following prints will point to the same object!
    # Service defined in a package
    print decoder_output.children._inner[0].children[0].children[1]
    # Client's service_reference 
    print decoder_output.children._inner[0].children[0].children[2].children[0]["service_reference"]
