# ROS Tools
# Author: Pranav Srinivas Kumar
# Date: 2015.02.20

import sys, os, inspect, collections
from collections import OrderedDict

# Find ANTLR4 python runtime
antlr4 = os.path.realpath(os.path.abspath
                          (os.path.join
                           (os.path.split
                            (inspect.getfile
                             (inspect.currentframe()
                          )
                         )[0], "Antlr4")
                       ))
if antlr4 not in sys.path:
    sys.path.insert(0, antlr4)
from antlr4 import *

# Find ROS Lexer, Parser and Visitor
ros_grammar = os.path.realpath(os.path.abspath
                               (os.path.join
                                (os.path.split
                                 (inspect.getfile
                                  (inspect.currentframe()
                               )
                              )[0], "grammar/01-Workspace/")
                            ))

if ros_grammar not in sys.path:
    sys.path.insert(0, ros_grammar)
from ROSLexer import ROSLexer
from ROSParser import ROSParser
from ROSListener import ROSListener
from ROSVisitor import ROSVisitor

# Find Hosts Lexer, Parser and Visitor
hosts_grammar = os.path.realpath(os.path.abspath
                               (os.path.join
                                (os.path.split
                                 (inspect.getfile
                                  (inspect.currentframe()
                               )
                              )[0], "grammar/02-Hosts/")
                            ))

if hosts_grammar not in sys.path:
    sys.path.insert(0, hosts_grammar)
from HostsLexer import HostsLexer
from HostsParser import HostsParser
from HostsListener import HostsListener

# Find Hosts Lexer, Parser and Visitor
deployment_grammar = os.path.realpath(os.path.abspath
                               (os.path.join
                                (os.path.split
                                 (inspect.getfile
                                  (inspect.currentframe()
                               )
                              )[0], "grammar/03-Deployment/")
                            ))

if deployment_grammar not in sys.path:
    sys.path.insert(0, deployment_grammar)
from DeploymentLexer import DeploymentLexer
from DeploymentParser import DeploymentParser
from DeploymentListener import DeploymentListener

from Cheetah.Template import Template

# Template Compile Step -- Compiling tmpl files in templates
# Generate template python files
generator_dir = os.path.dirname(os.path.realpath(__file__))
template_dir = os.path.join(generator_dir + "/templates")

# Recursively compile on template files in templates directory
os.system("/usr/local/bin/cheetah compile " + template_dir + "/*.tmpl > /dev/null 2>&1")
ros_templates = os.path.realpath(os.path.abspath
                                 (os.path.join
                                  (os.path.split
                                   (inspect.getfile
                                    (inspect.currentframe()
                                 )
                                )[0], "templates")
                              ))
if ros_templates not in sys.path:
    sys.path.insert(0, ros_templates)
from package_xml import *
from rapidxml_hpp import *
from rapidxml_utils_hpp import *
from xmlParser_hpp import *
from node_groups_xml import *
from base_component_hpp import *
from base_component_cpp import *
from msg import *
from srv import *
from component_hpp import *
from component_cpp import *
from Logger_cpp import *
from Logger_hpp import *
from nodeMain import *
from CMakeLists import *
from rml import *
from rhw import *
from rdp import *

# Find Drawable_Object
exeName = sys.argv[0]
dirName = os.path.abspath(exeName)
head,tail = os.path.split(dirName)
head,tail = os.path.split(head)
sys.path.append(head + '/editor_v2/')
from drawable import Drawable_Object

# ROS Workspace
class ROS_Workspace(Drawable_Object):
    # Initialize Workspace
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "workspace"
        self.properties["name"] = ""

# ROS Package
class ROS_Package(Drawable_Object):
    # Initialize Package
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "package"
        self.properties["name"] = ""
        self.properties["cmakelists_packages"] = ""
        self.properties["cmakelists_functions"] = ""
        self.properties["cmakelists_include_dirs"] = ""

# ROS Message
class ROS_Message(Drawable_Object):
    # Initialize Message
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "message"
        self.properties["name"] = ""
        # Fields e.g. [["int", "position"], ["float", "velocity", "334.5"]]
        self.properties["fields"] = []

# ROS Service
class ROS_Service(Drawable_Object):
    # Initialize Service
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "service"
        self.properties["name"] = ""
        self.properties["request"] = []
        self.properties["response"] = []

# ROS Component
class ROS_Component(Drawable_Object):
    # Initialize Component
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "component"
        self.properties["name"] = ""
        self.properties["type"] = "base"
        self.properties["init_business_logic"] = ""
        self.properties["user_includes"] = ""
        self.properties["user_globals"] = ""
        self.properties["hpp_globals"] = ""
        self.properties["user_private_variables"] = ""
        self.properties["destructor"] = ""

# ROS Timer
class ROS_Timer(Drawable_Object):
    # Initialize Timer
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "timer"
        self.properties["priority"] = "0"
        self.properties["deadline"] = "0.0"
        self.properties["deadline_unit"] = ""
        self.properties["name"] = ""
        self.properties["period"] = "0.0"
        self.properties["unit"] = ""
        self.properties["business_logic"] = ""

# ROS Client
class ROS_Client(Drawable_Object):
    # Initialize Client
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "client"
        self.properties["name"] = ""
        self.properties["service_text"] = ""
        self.properties["service_reference"] = None

# ROS Server
class ROS_Server(Drawable_Object):
    # Initialize Server
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "server"
        self.properties["name"] = ""
        self.properties["priority"] = "0"
        self.properties["deadline"] = "0.0"
        self.properties["deadline_unit"] = ""
        self.properties["service_text"] = ""
        self.properties["service_reference"] = None
        self.properties["business_logic"] = ""

# ROS Publisher
class ROS_Publisher(Drawable_Object):
    # Initialize Publisher
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "publisher"
        self.properties["message_text"] = ""
        self.properties["name"] = ""
        self.properties["message_reference"] = None

# ROS Subscriber
class ROS_Subscriber(Drawable_Object):
    # Initialize Subscriber
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "subscriber"
        self.properties["name"] = ""
        self.properties["priority"] = "0"
        self.properties["deadline"] = "0.0"
        self.properties["deadline_unit"] = ""
        self.properties["message_text"] = ""
        self.properties["message_reference"] = None
        self.properties["business_logic"] = ""

# ROS Component Instance
class ROS_Component_Instance(Drawable_Object):
    # Initialize Instance
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "component_instance"
        self.properties["name"] = ""
        self.properties["component_text"] = ""
        self.properties["component_reference"] = None

# ROS Node
class ROS_Node(Drawable_Object):
    # Initialize Node
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "node"
        self.properties["name"] = ""
        self.properties["cmakelists_add_cpp"] = ""
        self.properties["cmakelists_target_link_libs"] = ""

# ROS Host
class ROS_Host(Drawable_Object):
    # Initialize Host
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "host"
        self.properties["name"] = ""
        self.properties["ip_address"] = ""
        self.properties["architecture"] = ""

# Hardware Configuration - Group of ROS Hosts
class ROS_HW(Drawable_Object):
    # Initialize Hardware Configuration
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "hardware_configuration"
        self.properties["name"] = ""

# Deployment classes here
class ROS_Deployment(Drawable_Object):
    # Initialize Deployment
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "deployment"
        self.properties["name"] = ""
        self.properties["hardware_configuration_reference"] = None
        self.properties["xml_list"] = []
        self.groups = OrderedDict()

class ROS_Port_Instance(Drawable_Object):
    # Initialize the port 
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "port_instance"
        self.properties['name'] = ""
        self.properties['node_instance_reference'] = None
        self.properties['component_instance_reference'] = None
        self.properties["port_reference_string"] = ""
        self.properties['port_reference'] = None

class ROS_Group(Drawable_Object):
    # Initialize the group; children are port_instances
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "group"
        self.properties["name"] = ""

# Logger Object
# Values are set @ Deployment Time
# Values propagate to each Component
class ROS_Logger(Drawable_Object):
    # Initialize Logger 
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "logger"
        self.properties["name"] = "LOGGER"
        # Log levels of Logger
        self.properties["debug"] = "false"
        self.properties["info"] = "true"
        self.properties["warning"] = "false"
        self.properties["error"] = "true"
        self.properties["critical"] = "true"

class ROS_Group_XML(Drawable_Object):
    # Initialize a Node_Instance.Component_Instance.xml file
    def __init__(self, node_instance, component_instance):
        Drawable_Object.__init__(self)
        self.kind = "group_xml"
        self.properties["name"] = node_instance.properties["name"] + "." + component_instance.properties["name"] + ".xml"
        self.properties["node_instance"] = node_instance
        self.properties["component_instance"] = component_instance
        self.properties["groups"] = []
        self.properties["logger"] = ROS_Logger()

# Host Instances in a Deployment
class ROS_Host_Instance(Drawable_Object):
    # Initialize Host Instance
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "host_instance"
        self.properties["name"] = ""
        # Reference to actual host object
        self.properties["host_reference"] = None
        # Username of host
        self.properties["username"] = ""
        # Path to ssh key to access host
        self.properties["sshkey"] = ""
        # Absolute path to some start up script
        self.properties["init"] = ""
        # Environment Variables per host instance
        # [[env_name1, env_value1], [env_name2, env_value2], ..]
        self.properties["env_variables"] = []
 
# Node Instances in Deployment per Host Instance
class ROS_Node_Instance(Drawable_Object):
    # Initialize ROS Node Instance
    def __init__(self):
        Drawable_Object.__init__(self)
        self.kind = "node_instance"
        # Alias name given to Node instance
        self.properties["name"] = ""
        # Reference to actual node object
        self.properties["node_reference_string"] = ""
        self.properties["node_reference"] = None
        self.properties["cmdline_arguments"] = "" 

# Ros Workspace Builder
# Builds a ROS Workspace Object from .rml file
class ROS_Workspace_Builder(ROSListener):
    def __init__(self, parent_project):
        self.workspace = ROS_Workspace()
        self.workspace.parent = parent_project
        self.parent = parent_project
        self.server = ROS_Server()
        self.subscriber = ROS_Subscriber()
        self.timer = ROS_Timer()

    # Create a new ROS Package object
    def enterRos_packages(self, ctx):
        self.package = ROS_Package()
        self.package.parent = self.workspace
        
    # On exit, add the new package to list of packages in workspace
    def exitRos_packages(self, ctx):
        self.workspace.add(self.package)

    # Save the package name
    def enterPackage_name(self, ctx):
        self.package.properties["name"] = ctx.getText()
        print "ROSTOOLS::Reading Package: " + ctx.getText()

    # Create a new ROS Message object
    def enterRos_msg(self, ctx):
        self.message = ROS_Message()
        self.message.parent = self.package

    # Save the message name
    def enterMsg_name(self, ctx):
        self.message.properties["name"] = ctx.getText()

    # Save the fields in the ROS msg
    def enterMsg_field(self,ctx):
        field_type = ""
        field_name = ""
        field_value = ""
        for child in ctx.getChildren():
            context = str(type(child))
            # Find the message field type
            if "Msg_field_typeContext" in context:
                field_type = child.getText()
            # Find the message field name
            if "Msg_field_nameContext" in context:
                field_name = child.getText()
            # Find the message field value
            if "Msg_field_valueContext" in context:
                field_value = child.getText().replace(";", "")
        if field_type != "":
            if field_name != "":
                if field_value != "":
                    self.message.properties["fields"].append([field_type, field_name, field_value])
                else:
                    self.message.properties["fields"].append([field_type, field_name])

    # On exit, append message to list of messages in package
    def exitRos_msg(self, ctx):
        self.package.add(self.message)

    # Create a new ROS Service object
    def enterRos_srv(self, ctx):
        self.service = ROS_Service()
        self.service.parent = self.package

    # Save the name of the ROS Service
    def enterSrv_name(self, ctx):
        self.service.properties["name"] = ctx.getText()

    # Save the request arguments of the service
    def enterReq_argument(self, ctx):
        field_type = ""
        field_name = ""
        field_value = ""
        for child in ctx.getChildren():
            context = str(type(child))
            # Find request field type
            if "Req_field_typeContext" in context:
                field_type = child.getText()
            # Find request field name
            if "Req_field_nameContext" in context:
                field_name = child.getText()
            # Find request field value
            if "Req_field_valueContext" in context:
                field_value = child.getText()
        if field_type != "":
            if field_name != "":
                if field_value != "":
                    self.service.properties["request"].append([field_type, field_name, field_value])
                else:
                    self.service.properties["request"].append([field_type, field_name])

    # Save the response arguments of the service
    def enterRes_argument(self, ctx):
        field_type = ""
        field_name = ""
        field_value = ""
        for child in ctx.getChildren():
            context = str(type(child))
            # Find request field type
            if "Res_field_typeContext" in context:
                field_type = child.getText()
            # Find request field name
            if "Res_field_nameContext" in context:
                field_name = child.getText()
            # Find request field value
            if "Res_field_valueContext" in context:
                field_value = child.getText()
        if field_type != "":
            if field_name != "":
                if field_value != "":
                    self.service.properties["response"].append([field_type, field_name, field_value])
                else:
                    self.service.properties["response"].append([field_type, field_name])

    # On exit, add the service to the list of services in the package
    def exitRos_srv(self, ctx):
        self.package.add(self.service)
        
    # Create a new component object
    def enterRos_component(self, ctx):
        self.component = ROS_Component()
        self.component.parent = self.package

    # Save the name of the component
    def enterComponent_name(self, ctx):
        self.component.properties["name"] = ctx.getText()

    # Save the type of the component
    def enterComp_type(self, ctx):
        self.component.properties["type"] = ctx.getText()

    # Save all provided and required services
    def enterRos_client_server(self, ctx):
        if "provides" in ctx.getText():
            for child in ctx.getChildren():
                context = str(type(child))
                if "Service_nameContext" in context:
                    self.server = ROS_Server()
                    if "/" not in child.getText():
                        service_name = child.getText()
                        self.server.properties["service_text"] = child.getText()
                        for service in self.package.children:
                            if service.properties["name"] == service_name:
                                self.server.properties["service_reference"] = service
                    else:
                        self.server.properties["service_text"] = child.getText()
                        service_name = child.getText().split('/')[-1]
                    # CHECK: If this service has been defined 
                    self.server.properties["name"] = service_name + "_server"
                    self.server.parent = self.component
                    if self.server.properties["service_reference"] == None:
                        self.parent.null_references.append(self.server)
        elif "requires" in ctx.getText():
            for child in ctx.getChildren():
                context = str(type(child))
                if "Service_nameContext" in context:
                    self.client = ROS_Client()
                    if "/" not in child.getText():
                        service_name = child.getText()
                        self.client.properties["service_text"] = child.getText()
                        for service in self.package.children:
                            if service.properties["name"] == service_name:
                                self.client.properties["service_reference"] = service
                    else:
                        self.client.properties["service_text"] = child.getText()
                        service_name = child.getText().split('/')[-1]
                    # CHECK: If this service has been defined 
                    self.client.properties["name"] = service_name + "_client"
                    self.client.parent = self.component
                    if self.client.properties["service_reference"] == None:
                        self.parent.null_references.append(self.client)
                    self.component.add(self.client)

    # Save server priority
    def enterServer_priority(self, ctx):
        self.server.properties["priority"] = ctx.getText()

    # Save server deadline
    def enterServer_deadline(self, ctx):
        self.server.properties["deadline"] = ctx.getText()
        
    # Save server deadline unit
    def enterServer_deadline_unit(self, ctx):
        self.server.properties["deadline_unit"] = ctx.getText()

    # Save server properties and add server to component
    def exitRos_client_server_properties(self, ctx):
        self.component.add(self.server)

    # Save all publishers and susbcribers
    def enterRos_pub_sub(self, ctx):
        if "publisher" in ctx.getText():
            self.publisher = ROS_Publisher()
            for child in ctx.getChildren():
                context = str(type(child))
                if "TopicContext" in context:
                    if "/" not in child.getText():
                        topic_name = child.getText()
                        self.publisher.properties["message_text"] = child.getText()
                        # CHECK: If this toic has been defined
                        for message in self.package.children:
                            if message.properties["name"] == topic_name:
                                self.publisher.properties["message_reference"] = message
                    else:
                        self.publisher.properties["message_text"] = child.getText()
                        topic_name = child.getText().split('/')[-1]
                if "PublisherContext" in context:
                    self.publisher.properties["name"] = child.getText()
            self.publisher.parent = self.component
            if self.publisher.properties["message_reference"] == None:
                self.parent.null_references.append(self.publisher)
            self.component.add(self.publisher)

        elif "subscriber" in ctx.getText():
            self.subscriber = ROS_Subscriber()
            for child in ctx.getChildren():
                context = str(type(child))
                if "TopicContext" in context:
                    if "/" not in child.getText():
                        topic_name = child.getText()
                        self.subscriber.properties["message_text"] = child.getText()          
                        for message in self.package.children:
                            if message.properties["name"] == topic_name:
                                self.subscriber.properties["message_reference"] = message   
                    else:
                        self.subscriber.properties["message_text"] = child.getText()
                        topic_name = child.getText().split('/')[-1]
                if "SubscriberContext" in context:
                    self.subscriber.properties["name"] = child.getText()
            self.subscriber.parent = self.component
            if self.subscriber.properties["message_reference"] == None:
                self.parent.null_references.append(self.subscriber)

    # Save subscriber priority
    def enterSubscriber_priority(self, ctx):
        self.subscriber.properties["priority"] = ctx.getText()

    # Save subscriber deadline
    def enterSubscriber_deadline(self, ctx):
        self.subscriber.properties["deadline"] = ctx.getText()
        
    # Save subscriber deadline unit
    def enterSubscriber_deadline_unit(self, ctx):
        self.subscriber.properties["deadline_unit"] = ctx.getText()

    # Save subscriber properties and add subscriber to component
    def exitRos_pub_sub_properties(self, ctx):
        self.component.add(self.subscriber)

    # Save all component timers
    def enterRos_timer(self, ctx):
        for child in ctx.getChildren():
            context = str(type(child))
            if "Timer_nameContext" in context:
                name = child.getText()
            elif "Timer_periodContext" in context:
                period = child.getText()
            elif "Period_unitContext" in context:
                period_unit = child.getText()
        self.timer = ROS_Timer()
        self.timer.properties["name"] = name
        self.timer.properties["period"] = period
        self.timer.properties["unit"] = period_unit
        self.timer.parent = self.component

    # Save timer priority
    def enterTimer_priority(self, ctx):
        self.timer.properties["priority"] = ctx.getText()

    # Save subscriber deadline
    def enterTimer_deadline(self, ctx):
        self.timer.properties["deadline"] = ctx.getText()
        
    # Save subscriber deadline unit
    def enterTimer_deadline_unit(self, ctx):
        self.timer.properties["deadline_unit"] = ctx.getText()

    # Save timer properties and add timer to component
    def exitRos_Timer_properties(self, ctx):
        self.component.add(self.timer)

    # On exit, add component to list of components in package
    def exitRos_component(self, ctx):
        self.package.children.append(self.component)

    # Create a new ROS node object
    def enterRos_node(self, ctx):
        self.node = ROS_Node()
        self.node.parent = self.package

    # Save ROS node name
    def enterNode_name(self, ctx):
        self.node.properties["name"] = ctx.getText()

    # Save the component instances in each node
    def enterComponent_instances(self, ctx):
        comp_type = ""
        instance = ""
        local_component = False
        self.component_instance = ROS_Component_Instance()
        for child in ctx.getChildren():
            context = str(type(child))
            if "Component_typeContext" in context:
                if "/" not in child.getText():
                    comp_type = child.getText()
                    self.component_instance.properties["component_text"] = child.getText()
                    local_component = True
                else:
                    self.component_instance.properties["component_text"] = child.getText()
                    comp_type = child.getText().split('/')[-1]
            elif "Component_instanceContext" in context:
                instance = child.getText()
        self.component_instance.properties["name"] = instance
        if local_component == True:
            for child in self.package.children:
                if child.properties["name"] == comp_type:
                    self.component_instance.properties["component_reference"] = child
        self.component_instance.parent = self.node
        if self.component_instance.properties["component_reference"] == None:
            self.parent.null_references.append(self.component_instance)
        self.node.add(self.component_instance)

    # On exit, add the node to the list of nodes in package
    def exitRos_node(self, ctx):
        self.package.children.append(self.node)

class ROS_Hardware_Builder(HostsListener):
    def __init__(self, parent_project):
        self.hardware_configuration = ROS_HW()
        self.hardware_configuration.parent = parent_project
        self.host = ROS_Host()

    # Create a new ROS Host
    def enterHost(self, ctx):
        self.host = ROS_Host()

    def enterHost_name(self, ctx):
        self.host.properties["name"] = ctx.getText()

    def enterIp_address_string(self, ctx):
        self.host.properties["ip_address"] = ctx.getText()

    def enterArchitecture_string(self, ctx):
        self.host.properties["architecture"] = ctx.getText()

    # Add the created host to hardware configuration children
    def exitHost(self, ctx):
        self.hardware_configuration.add(self.host)  

class ROS_Deployment_Builder(DeploymentListener):
    def __init__(self, workspace_object, hardware_configurations_object, deployment_name, parent_project):
        self.deployment = ROS_Deployment()
        self.deployment.parent = parent_project
        self.deployment.properties["name"] = deployment_name
        self.workspace = workspace_object
        self.all_hw_configs = hardware_configurations_object
        self.host_instance = None
        self.node_instance = None
        self.port_instance = None
        self.group = None

    # Group Definitions
    def enterGroup(self, ctx):
        self.group = ROS_Group()

    def enterGroup_id(self, ctx):
        self.group.properties['name'] = ctx.getText()

    def enterPort(self,ctx):
        found = False
        self.port_instance = ROS_Port_Instance()
        self.port_instance.properties['name'] = ctx.getText()

        self.node_instance.properties["port_reference_string"] = ctx.getText()
        nodeInst = ctx.getText().split("/")[0]
        compInst = ctx.getText().split("/")[1]
        portInst = ctx.getText().split("/")[2]
        found_comp = False
        found_port = False
        nodeRef = None
        for ni in self.deployment.getChildrenByKind("node_instance"):
            if ni.properties['name'] == nodeInst:
                nodeRef = ni.properties['node_reference']
                self.port_instance.properties['node_instance_reference'] = ni
                break
        if nodeRef != None:
            compRef = None
            for ci in nodeRef.children:
                if ci.properties['name'] == compInst:
                    compRef = ci.properties['component_reference']
                    self.port_instance.properties['component_instance_reference'] = ci
                    break
            if compRef != None:
                portRef = None
                for p in compRef.children:
                    if p.properties['name'] == portInst:
                        portRef = p
                        break
                if portRef != None:
                    self.port_instance.properties['port_reference'] = portRef
                    self.port_instance.properties['name'] = portRef.properties['name']
                    return
                else:
                    print "ROSTOOLS::ERROR::Invalid Group Port Name {}".format(portInst)
            else:
                print "ROSTOOLS::ERROR::Invalid Group Component Instance Name {}".format(compInst)
        else:
            print "ROSTOOLS::ERROR::Invalid Group Node Instance Name {}".format(nodeInst)
        self.port_instance = None

    def exitPort(self, ctx):
        if self.port_instance != None:
            self.group.add(self.port_instance)
        else:
            print "ROSTOOLS::ERROR::Invalid Port Instance used in Deployment"

    def exitGroup(self, ctx):
        if self.group != None:
            self.deployment.groups[self.group.properties['name']] = self.group
            self.deployment.add(self.group)
        else:
            print "ROSTOOLS::ERROR::Invalid Group in Deployment"

    # Using hardware configuration
    def enterHardware(self, ctx):
        found = False
        for config in self.all_hw_configs:
            if config.properties["name"] == ctx.getText():
                print "ROSTOOLS::Using Hardware Configuration:", ctx.getText()
                self.deployment.properties["hardware_configuration_reference"] = config
                found = True
                break
        if found == False:
            print "ROSTOOLS::ERROR::Invalid Hardware Configuration used in Deployment"

    # Create a new host instance
    def enterNode_host_mapping(self, ctx):
        self.host_instance = ROS_Host_Instance()

    # Add host instance to self.deployment.children
    def exitNode_host_mapping(self, ctx):
        if self.host_instance != None:
            self.deployment.add(self.host_instance)
        else:
            print "ROSTOOLS::ERROR::Invalid Host Instance in Deployment"
    
    # Find host object ref from host name
    def enterHostname(self, ctx):
        self.host_instance.properties["name"] = ctx.getText()
        if self.deployment.properties["hardware_configuration_reference"] != None:
            for hardware in self.deployment.properties["hardware_configuration_reference"].children:
                if hardware.properties["name"] == ctx.getText():
                    self.host_instance.properties["host_reference"] = hardware
                    break
        else:
            print "ROSTOOLS::ERROR::Hardware Configuration Reference is set to None"

    # Username to login to host
    def enterUsername_string(self, ctx):
        self.host_instance.properties["username"] = ctx.getText()

    # SSH Key to login to host
    def enterSshkey_path(self, ctx):
        self.host_instance.properties["sshkey"] = ctx.getText()

    # Init script to run on host
    def enterInit_path(self, ctx):
        self.host_instance.properties["init"] = ctx.getText()

    # Environment variables to set on host
    def enterEnv_variables(self, ctx):
        env_name = ""
        env_value = ""
        for child in ctx.getChildren():
            context = str(type(child))
            if "Env_nameContext" in context:
                env_name = child.getText()
            elif "Env_valueContext" in context:
                env_value = child.getText()
        if env_name != "" and env_value != "":
            self.host_instance.properties["env_variables"].append([env_name, env_value])
        else:
            print "ROSTOOLS::ERROR::Invalid Environment Variable!"

    def enterNodes(self, ctx):
        self.node_instance = ROS_Node_Instance()

    def exitNodes(self, ctx):
        if self.node_instance != None:
            self.host_instance.add(self.node_instance)
        else:
            print "ROSTOOLS::ERROR::Invalid Node Instance used in Deployment"

    def enterNode_alias(self, ctx):
        self.node_instance.properties["name"] = ctx.getText()
        self.node_alias = ctx.getText()

    def enterNode(self, ctx):
        self.node_instance.properties["node_reference_string"] = ctx.getText()
        package = ctx.getText().split("/")[0]
        node = ctx.getText().split("/")[1]
        found_package = False
        found_node = False

        # For all packages in workspace
        for child in self.workspace.children:
            # Find the referenced package
            if child.properties["name"] == package:
                found_package = True
                # For all nodes in package
                for node_ref in child.getChildrenByKind("node"):
                    # Find the referenced node
                    if node_ref.properties["name"] == node:
                        self.node_instance.properties["node_reference"] = node_ref
                        found_node = True
                        break

        if found_package != True or found_node != True:
            print "ROSTOOLS::ERROR::Invalid Package or Node Name"

    def enterArguments(self, ctx):
        self.node_instance.properties["cmdline_arguments"] = ctx.getText()

# OrderedSet recipe - because python set doesn't preserve order
class OrderedSet(collections.MutableSet):

    def __init__(self, iterable=None):
        self.end = end = [] 
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            curr = end[1]
            curr[2] = end[1] = self.map[key] = [key, curr, end]

    def discard(self, key):
        if key in self.map:        
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        curr = end[2]
        while curr is not end:
            yield curr[0]
            curr = curr[2]

    def __reversed__(self):
        end = self.end
        curr = end[1]
        while curr is not end:
            yield curr[0]
            curr = curr[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)

class Workspace_Generator:
    # Main Generate function
    def generate(self, workspace, path, deployments, xml_path):
        print "ROSTOOLS::Generating ROS Workspace..."
        # Make the workspace directory
        self.workspace_dir = os.path.join(path, workspace.properties["name"])
        print "ROSTOOLS::Workspace Path:", self.workspace_dir
        if not os.path.exists(self.workspace_dir):
            os.makedirs(self.workspace_dir)

        # Generate the .catkin_ws file
        catkin_ws = "# This file currently only serves to mark the location of a catkin workspace for tool integration "
        filename = ".catkin_workspace"
        with open(os.path.join(self.workspace_dir, filename), 'w') as temp_file:
            temp_file.write(catkin_ws)
            temp_file.close()  

        # Make the src directory
        self.src_path = self.workspace_dir + "/src"
        if not os.path.exists(self.src_path):
            os.makedirs(self.src_path)     

        # For each package in the ros model
        for package in workspace.children:
            # Create the package directory
            self.package_path = os.path.join(self.src_path, package.properties["name"])
            print "ROSTOOLS::" + package.properties["name"] + " Path: " + self.package_path
            if not os.path.exists(self.package_path):
                os.makedirs(self.package_path)

            # Create the include directory
            self.include = self.package_path + "/include"
            if not os.path.exists(self.include):
                os.makedirs(self.include)
                
            # Create the src directory
            self.src = self.package_path + "/src"
            if not os.path.exists(self.src):
                os.makedirs(self.src)

            messages = []
            services = []
            components = []
            nodes = []
            for child in package.children:
                if child.kind == "message":
                    messages.append(child)
                elif child.kind == "service":
                    services.append(child)
                elif child.kind == "component":
                    components.append(child)
                elif child.kind == "node":
                    nodes.append(child)

            if (len(messages) > 0):
                self.msg = self.package_path + "/msg"
                if not os.path.exists(self.msg):
                    os.makedirs(self.msg)

            # Create the srv directory if there are services
            if (len(services) > 0):
                self.srv = self.package_path + "/srv"
                if not os.path.exists(self.srv):
                    os.makedirs(self.srv)

            # Create package.xml
            package_xml_namespace = {'package_name': package.properties["name"]}
            t = package_xml(searchList=[package_xml_namespace])
            self.package_xml = str(t)
            with open(os.path.join(self.package_path, "package.xml"), 'w') as temp_file:
                temp_file.write(self.package_xml)


            # Create rapidxml.hpp, rapidxml_utils.hpp, and xmlParser.hpp
            self.cpp = self.src + "/" + package.properties["name"]
            self.hpp = self.include + "/" + package.properties["name"]

            if not os.path.exists(self.hpp):
                os.makedirs(self.hpp)
            xml_namespace = {'hash_include': "#include", 
                                      'package_name': package.properties["name"]}
            # MAIN RAPIDXML FILE
            t = rapidxml_hpp(searchList=[xml_namespace])
            self.rapidxml_hpp = str(t)
            with open(os.path.join(self.hpp, "rapidxml.hpp"), 'w') as temp_file:
                temp_file.write(self.rapidxml_hpp)
            # UTILS FILE
            t = rapidxml_utils_hpp(searchList=[xml_namespace])
            self.rapidxml_utils_hpp = str(t)
            with open(os.path.join(self.hpp, "rapidxml_utils.hpp"), 'w') as temp_file:
                temp_file.write(self.rapidxml_utils_hpp)
            # XML PARSER FILE
            t = xmlParser_hpp(searchList=[xml_namespace])
            self.xmlParser_hpp = str(t)
            with open(os.path.join(self.hpp, "xmlParser.hpp"), 'w') as temp_file:
                temp_file.write(self.xmlParser_hpp)

            # Create Component.cpp and Component.hpp
            self.cpp = self.src + "/" + package.properties["name"]
            self.hpp = self.include + "/" + package.properties["name"]

            if not os.path.exists(self.cpp):
                os.makedirs(self.cpp)
            base_cpp_namespace = {'hash_include': "#include", 
                                      'package_name': package.properties["name"]}
            # Populate Base Component cpp template
            t = base_component_cpp(searchList=[base_cpp_namespace])
            self.base_cpp = str(t)
            # Write Component.cpp
            with open(os.path.join(self.cpp, "Component.cpp"), 'w') as temp_file:
                temp_file.write(self.base_cpp)

            if not os.path.exists(self.hpp):
                os.makedirs(self.hpp)
            base_hpp_namespace = {'hash_include': "#include", 
                                      'package_name': package.properties["name"]}
            # Populate Base Component hpp template
            t = base_component_hpp(searchList=[base_hpp_namespace])
            self.base_hpp = str(t)
            # Write Component.hpp
            with open(os.path.join(self.hpp, "Component.hpp"), 'w') as temp_file:
                temp_file.write(self.base_hpp)

            # Populate Logger cpp template
            t = Logger_cpp(searchList=[base_cpp_namespace])
            self.logger_cpp = str(t)
            # Write Logger.cpp
            with open(os.path.join(self.cpp, "Logger.cpp"), 'w') as temp_file:
                temp_file.write(self.logger_cpp)

            # Populate Logger hpp template
            t = Logger_hpp(searchList=[base_hpp_namespace])
            self.logger_hpp = str(t)
            # Write Logger.hpp
            with open(os.path.join(self.hpp, "Logger.hpp"), 'w') as temp_file:
                temp_file.write(self.logger_hpp)

            # Create all package messages in msg folder
            for message in messages:
                msg_namespace = {'fields': message.properties["fields"]}
                msg_filename = message.properties["name"] + ".msg"
                t = msg(searchList=[msg_namespace])
                self.msg_fields = str(t)
                # Write msg file
                with open(os.path.join(self.msg, msg_filename), 'w') as temp_file:
                    temp_file.write(self.msg_fields)

            # Create all package services in srv folder
            for service in services:
                srv_filename = service.properties["name"] + ".srv"
                srv_namespace = {'request_fields': service.properties["request"], 
                                 'response_fields': service.properties["response"]}
                t = srv(searchList=[srv_namespace])
                self.srv_fields = str(t)
                # Write the srv file
                with open(os.path.join(self.srv, srv_filename), 'w') as temp_file:
                    temp_file.write(self.srv_fields)

            cmakelists_services = services

            # Create a .hpp and .cpp per component definition in package
            for component in components:
                component_name  = component.properties["name"]
                define_guard = component_name.upper()

                # Categorize children of component
                publishers = []
                subscribers = []
                clients = []
                servers = []
                timers = []
                provided_services = []
                required_services = []
                for child in component.children:
                    if child.kind == "publisher":
                        publishers.append(child)
                    elif child.kind == "subscriber":
                        subscribers.append(child)
                    elif child.kind == "client":
                        clients.append(child)
                        required_service = [child.properties["service_reference"].parent.properties["name"], child.properties["service_reference"].properties["name"]]
                        if required_service not in required_services:
                            required_services.append(required_service)
                    elif child.kind == "server":
                        servers.append(child)
                        provided_service = child.properties["service_reference"].properties["name"]
                        if provided_service not in provided_services:
                            provided_services.append(provided_service)
                    elif child.kind == "timer":
                        timers.append(child)

                topics = []
                for publisher in publishers:
                    topics.append([publisher.properties["message_reference"].parent.properties["name"], 
                                   publisher.properties["message_reference"].properties["name"]])
                for subscriber in subscribers:
                    topics.append([subscriber.properties["message_reference"].parent.properties["name"], 
                                   subscriber.properties["message_reference"].properties["name"]])
                # topics = OrderedSet(topics)
                services = []
                for client in clients:
                    services.append([client.properties["service_reference"].parent.properties["name"],
                                     client.properties["service_reference"].properties["name"]])
                for server in servers:
                    services.append([server.properties["service_reference"].parent.properties["name"],
                                    server.properties["service_reference"].properties["name"]])
                # services = OrderedSet(services)
                hash_include = "#include"
                component_namespace = {'define_guard': define_guard, 
                                       'hash_include': hash_include, 
                                       'package_name': package.properties["name"], 
                                       'topics': topics, 
                                       'services': services, 
                                       'component_name': component.properties["name"],
                                       'init_business_logic': component.properties["init_business_logic"],
                                       'user_includes': component.properties["user_includes"],
                                       'user_globals': component.properties["user_globals"],
                                       'hpp_globals': component.properties["hpp_globals"],
                                       'user_private_variables': component.properties["user_private_variables"],
                                       'destructor': component.properties["destructor"],
                                       'publishers': publishers, 
                                       'subscribers': subscribers, 
                                       'clients': clients,
                                       'servers': servers,
                                       'provided_services': provided_services, 
                                       'required_services': required_services, 
                                       'timers': timers}
                t = component_hpp(searchList=[component_namespace])
                self.component_hpp_str = str(t)
                # Write the component hpp file
                hpp_filename = component_name + ".hpp"

                with open(os.path.join(self.hpp, hpp_filename), 'w') as temp_file_h:
                    temp_file_h.write(self.component_hpp_str)

                # GENERATING CPP FILES

                t = component_cpp(searchList=[component_namespace])
                self.component_cpp_str = str(t)
                # Write the component cpp file
                cpp_filename = component_name + ".cpp"

                with open(os.path.join(self.cpp, cpp_filename), 'w') as temp_file:
                    temp_file.write(self.component_cpp_str)

            for node in nodes:
                node_name = node.properties["name"]
                hash_include = "#include"
                node_namespace = {'hash_include': hash_include, 
                                  'package_name': package.properties["name"],
                                  'node_name': node_name, 
                                  'component_instances': node.children}
                t = nodeMain(searchList=[node_namespace])
                self.nodeMain_str = str(t)
                # Write node main.cpp file
                node_filename = node_name + "_main.cpp"

                with open(os.path.join(self.cpp, node_filename), 'w') as temp_file_nm:
                    temp_file_nm.write(self.nodeMain_str)

            cmake_lists_namespace = {'package_name': package.properties["name"],
                                     'packages': package.properties["cmakelists_packages"],
                                     'functions': package.properties["cmakelists_functions"],
                                     'include_dirs': package.properties["cmakelists_include_dirs"],
                                     'messages': messages, 
                                     'services': cmakelists_services, 
                                     'catkin_INCLUDE_DIRS': "${catkin_INCLUDE_DIRS}",
                                     'PROJECT_NAME': "${PROJECT_NAME}",
                                     'catkin_LIBRARIES': '${catkin_LIBRARIES}',
                                     'CATKIN_PACKAGE_BIN_DESTINATION':
                                           "${CATKIN_PACKAGE_BIN_DESTINATION}",
                                     'CATKIN_PACKAGE_LIB_DESTINATION': 
                                           "${CATKIN_PACKAGE_LIB_DESTINATION}",
                                     'CATKIN_PACKAGE_INCLUDE_DESTINATION':
                                           "${CATKIN_PACKAGE_INCLUDE_DESTINATION}",
                                     'CATKIN_PACKAGE_SHARE_DESTINATION':
                                           "${CATKIN_PACKAGE_SHARE_DESTINATION}",
                                     'CMAKE_CXX_COMPILER': "${CMAKE_CXX_COMPILER}",
                                     'nodes': nodes}
            t = CMakeLists(searchList=[cmake_lists_namespace])
            self.cmake_lists = str(t)
            # Write CMakeLists file
            with open(os.path.join(self.package_path, "CMakeLists.txt"), 'w') as temp_file:
                temp_file.write(self.cmake_lists)

        for deployment in deployments:
            create_folder = False
            groups = []
            xml_list = []
            for child in deployment.children:
                if child.kind == "group":
                    create_folder = True
                    groups.append(child)
            if create_folder == True:
                xml_folder_home = os.path.join(xml_path, deployment.properties["name"])
                if not os.path.exists(xml_folder_home):
                    os.makedirs(xml_folder_home)
                
                # For every group in deployment
                for group in groups:
                    # For every port in the group
                    for port in group.children:
                        # Create a new xml file if needed by obtaining the node_instance 
                        # & component_instance of port
                        node_instance_name = port.properties["node_instance_reference"].properties["name"]
                        comp_instance_name = port.properties["component_instance_reference"].properties["name"]
                        new_xml = ROS_Group_XML(port.properties["node_instance_reference"], 
                                                port.properties["component_instance_reference"])
                        new_xml.properties["node_instance"] = port.properties["node_instance_reference"]
                        new_xml.properties["component_instance"] = port.properties["component_instance_reference"]

                        # Add new xml to list if not already in list
                        if new_xml not in xml_list:
                            xml_list.append(new_xml)
                        
                        # Add the group to xml.groups
                        for xml in xml_list:
                            if xml.properties["name"] == new_xml.properties["name"]:
                                xml_group = ROS_Group()
                                xml_group.properties["name"] = group.properties["name"]
                                for grp_port in group.children:
                                    if grp_port.properties["node_instance_reference"].properties["name"] == xml.properties["node_instance"].properties["name"]:
                                        if grp_port.properties["component_instance_reference"].properties["name"] == xml.properties["component_instance"].properties["name"]:
                                            xml_group.children.append(grp_port)
                                xml.properties["groups"].append(xml_group)
                               

                    deployment.properties["xml_list"] = xml_list
                    for xml in xml_list:
                        xml_namespace = {'xml': xml}
                        t = node_groups_xml(searchList=[xml_namespace])
                        xml_str = str(t)
                        # Write CMakeLists file
                        with open(os.path.join(xml_folder_home, 
                                               xml.properties["name"]), 'w') as temp_file:
                            temp_file.write(xml_str)
        return self.workspace_dir
                
class Workspace_Loader:
    # Load the business logic of component operations
    def load(self, workspace, path):
        
        print "ROSTOOLS::Checking for existing workspace in path:", path
        self.workspace_dir = path + "/" + workspace.properties["name"]

        if os.path.exists(self.workspace_dir):
            self.src_path = self.workspace_dir + "/src"

            for package in workspace.children:
                self.package_path = self.src_path + "/" + package.properties["name"]

                if(os.path.isfile(os.path.join(self.package_path, "CMakeLists.txt")) == True):
                    with open(os.path.join(self.package_path, "CMakeLists.txt"), 'r') as cmakelists:
                        
                        # CHECK CMAKELISTS FILE
                        package_marker = False
                        package_text = ""
                        for num, line in enumerate(cmakelists, 1):
                            if package_marker == True and "## End Package Marker" not in line:
                                package_text += line
                            if package_marker == False and "## Start Package Marker" in line:
                                package_marker = True
                            if package_marker == True and "## End Package Marker" in line:
                                package_marker = False
                        package.properties["cmakelists_packages"] = package_text   

                    with open(os.path.join(self.package_path, "CMakeLists.txt"), 'r') as cmakelists:
                        
                        # CHECK CMAKELISTS FILE
                        functions_marker = False
                        functions_text = ""
                        for num, line in enumerate(cmakelists, 1):
                            if functions_marker == True and "## End Global Marker" not in line:
                                functions_text += line
                            if functions_marker == False and "## Start Global Marker" in line:
                                functions_marker = True
                            if functions_marker == True and "## End Global Marker" in line:
                                functions_marker = False
                        package.properties["cmakelists_functions"] = functions_text  

                    with open(os.path.join(self.package_path, "CMakeLists.txt"), 'r') as cmakelists:
                        
                        # CHECK CMAKELISTS FILE
                        include_marker = False
                        include_text = ""
                        for num, line in enumerate(cmakelists, 1):
                            if include_marker == True and "## End Include Directories Marker" not in line:
                                include_text += line
                            if include_marker == False and "## Start Include Directories Marker" in line:
                                include_marker = True
                            if include_marker == True and "## End Include Directories Marker" in line:
                                include_marker = False
                        package.properties["cmakelists_include_dirs"] = include_text   

                if(os.path.isfile(os.path.join(self.package_path, "CMakeLists.txt")) == True):

                    nodes = []
                    for child in package.children:
                        if child.kind == "node":
                            nodes.append(child)
                    for node in nodes:

                        with open(os.path.join(self.package_path, "CMakeLists.txt"), 'r') as cmakelists:
                            # CHECK CMAKELISTS FILE
                            cpp_marker = False
                            cpp_text = ""
                            start_marker = "## Start " + node.properties["name"] + " CPP Marker"
                            end_marker = "## End " + node.properties["name"] + " CPP Marker"
                            for num, line in enumerate(cmakelists, 1):
                                if cpp_marker == True and end_marker not in line:
                                    cpp_text += line
                                if cpp_marker == False and start_marker in line:
                                    cpp_marker = True
                                if cpp_marker == True and end_marker in line:
                                    cpp_marker = False
                            node.properties["cmakelists_add_cpp"] = cpp_text  

                        with open(os.path.join(self.package_path, "CMakeLists.txt"), 'r') as cmakelists:
                            # CHECK CMAKELISTS FILE
                            tll_marker = False
                            tll_text = ""
                            start_marker = "## Start " + node.properties["name"] + " Target Link Libraries Marker"
                            end_marker = "## End " + node.properties["name"] + " Target Link Libraries Marker"
                            for num, line in enumerate(cmakelists, 1):
                                if tll_marker == True and end_marker not in line:
                                    tll_text += line
                                if tll_marker == False and start_marker in line:
                                    tll_marker = True
                                if tll_marker == True and end_marker in line:
                                    tll_marker = False
                            node.properties["cmakelists_target_link_libs"] = tll_text                     

                if os.path.exists(self.package_path):
                    print "ROSTOOLS::Preserving code for Package: ", self.package_path

                    self.include = self.package_path + "/include"
                    self.src = self.package_path + "/src"
                    self.cpp = self.src + "/" + package.properties["name"]
                    self.hpp = self.include + "/" + package.properties["name"]

                    components = []
                    for child in package.children:
                        if child.kind == "component":
                            components.append(child)

                    for component in components:

                        # FIND ALL COMPONENT HPP FILES
                        if(os.path.isfile(os.path.join(self.hpp, component.properties["name"] + ".hpp")) == True):

                            with open(os.path.join(self.hpp, component.properties["name"] + ".hpp"), 'r') as hpp_file:
                                # CHECK USER INCLUDES
                                incl_marker = False
                                incl_text = ""
                                for num, line in enumerate(hpp_file, 1):
                                    if incl_marker == True and "//# End User Includes Marker" not in line:
                                        incl_text += line
                                    if incl_marker == False and "//# Start User Includes Marker" in line:
                                        incl_marker = True
                                    if incl_marker == True and "//# End User Includes Marker" in line:
                                        incl_marker = False
                                component.properties["user_includes"] = incl_text

                            with open(os.path.join(self.hpp, component.properties["name"] + ".hpp"), 'r') as hpp_file:
                                # CHECK USER GLOBALS IN HPP
                                hpp_globals_marker = False
                                hpp_globals_text = ""
                                for num, line in enumerate(hpp_file, 1):
                                    if hpp_globals_marker == True and "//# End User Globals Marker" not in line:
                                        hpp_globals_text += line
                                    if hpp_globals_marker == False and "//# Start User Globals Marker" in line:
                                        hpp_globals_marker = True
                                    if hpp_globals_marker == True and "//# End User Globals Marker" in line:
                                        hpp_globals_marker = False
                                component.properties["hpp_globals"] = hpp_globals_text

                            with open(os.path.join(self.hpp, component.properties["name"] + ".hpp"), 'r') as hpp_file:
                                # CHECK USER Private Variables
                                pv_marker = False
                                pv_text = ""
                                for num, line in enumerate(hpp_file, 1):
                                    if pv_marker == True and "//# End User Private Variables Marker" not in line:
                                        pv_text += line
                                    if pv_marker == False and "//# Start User Private Variables Marker" in line:
                                        pv_marker = True
                                    if pv_marker == True and "//# End User Private Variables Marker" in line:
                                        pv_marker = False
                                component.properties["user_private_variables"] = pv_text
                                                    
                        # FIND ALL COMPONENT CPP FILES
                        if(os.path.isfile(os.path.join(self.cpp, component.properties["name"] + ".cpp")) == True):

                            with open(os.path.join(self.cpp, component.properties["name"] + ".cpp"), 'r') as cpp_file:
                                # CHECK USER GLOBALS
                                globals_marker = False
                                globals_text = ""
                                for num, line in enumerate(cpp_file, 1):
                                    if globals_marker == True and "//# End User Globals Marker" not in line:
                                        globals_text += line
                                    if globals_marker == False and "//# Start User Globals Marker" in line:
                                        globals_marker = True
                                    if globals_marker == True and "//# End User Globals Marker" in line:
                                        globals_marker = False
                                component.properties["user_globals"] = globals_text
                            
                            # OPEN THE CPP FILE
                            with open(os.path.join(self.cpp, component.properties["name"] + ".cpp"), 'r') as cpp_file:
                                # CHECK INIT BUSINESS LOGIC
                                init_marker = False
                                init_text = ""
                                for num, line in enumerate(cpp_file, 1):
                                    if init_marker == True and "//# End Init" not in line:
                                        init_text += line
                                    if init_marker == False and "//# Start Init Marker" in line:
                                        init_marker = True
                                    if init_marker == True and "//# End Init Marker" in line:
                                        init_marker = False
                                component.properties["init_business_logic"] = init_text

                            # OPEN THE CPP FILE
                            with open(os.path.join(self.cpp, component.properties["name"] + ".cpp"), 'r') as cpp_file:
                                # CHECK INIT BUSINESS LOGIC
                                destructor_marker = False
                                destructor_text = ""
                                for num, line in enumerate(cpp_file, 1):
                                    if destructor_marker == True and "//# End Destructor" not in line:
                                        destructor_text += line
                                    if destructor_marker == False and "//# Start Destructor Marker" in line:
                                        destructor_marker = True
                                    if destructor_marker == True and "//# End Destructor Marker" in line:
                                        destructor_marker = False
                                component.properties["destructor"] = destructor_text

                            subscribers = []
                            timers = []
                            servers = []
                            for child in component.children:
                                if child.kind == "subscriber":
                                    subscribers.append(child)
                                elif child.kind == "timer":
                                    timers.append(child)
                                elif child.kind == "server":
                                    servers.append(child)
                                
                            # CHECK SUBSCRIBER BUSINESS LOGIC
                            for sub in subscribers:

                                # OPEN THE CPP FILE
                                with open(os.path.join(self.cpp, component.properties["name"] + ".cpp"), 'r') as cpp_file:
                                    
                                    sub_marker = False
                                    sub_text = ""
                                    callback_name = sub.properties["name"] + "_OnOneData"
                                    start_callback = "//# Start " + callback_name
                                    end_callback = "//# End " + callback_name
                                    for num, line in enumerate(cpp_file, 1):
                                        if sub_marker == True and end_callback not in line:
                                            sub_text += line
                                        if sub_marker == False and start_callback in line:
                                            sub_marker = True
                                        if sub_marker == True and end_callback in line:
                                            sub_marker = False
                                    sub.properties["business_logic"] = sub_text
                                    
                            # CHECK TIMER BUSINESS LOGIC
                            for timer in timers:

                                # OPEN THE CPP FILE
                                with open(os.path.join(self.cpp, component.properties["name"] + ".cpp"), 'r') as cpp_file:
                                    
                                    timer_marker = False
                                    timer_text = ""
                                    callback_name = timer.properties["name"] + "Callback"
                                    start_callback = "//# Start " + callback_name
                                    end_callback = "//# End " + callback_name
                                    for num, line in enumerate(cpp_file, 1):
                                        if timer_marker == True and end_callback not in line:
                                            timer_text += line
                                        if timer_marker == False and start_callback in line:
                                            timer_marker = True
                                        if timer_marker == True and end_callback in line:
                                            timer_marker = False
                                    timer.properties["business_logic"] = timer_text
                                    
                            # CHECK SERVICE BUSINESS LOGIC
                            for server in servers:

                                # OPEN THE CPP FILE
                                with open(os.path.join(self.cpp, component.properties["name"] + ".cpp"), 'r') as cpp_file:
                                    
                                    service_marker = False
                                    service_text = ""
                                    callback_name = server.properties["service_reference"].properties["name"] + "Callback"
                                    start_callback = "//# Start " + callback_name
                                    end_callback = "//# End " + callback_name
                                    for num, line in enumerate(cpp_file, 1):
                                        if service_marker == True and end_callback not in line:
                                            service_text += line
                                        if service_marker == False and start_callback in line:
                                            service_marker = True
                                        if service_marker == True and end_callback in line:
                                            service_marker = False
                                    server.properties["business_logic"] = service_text

# ROS Project class
class ROS_Project(Drawable_Object):
    # Initialize ROS Project
    def __init__(self, **kwargs):
        Drawable_Object.__init__(self)
        # Name of the ROS Project
        self.project_name = kwargs.pop("name", "")
        # Path to ROS Project
        self.project_path = kwargs.pop("path", "")
        # Ros Workspace
        self.workspace = ROS_Workspace()
        # Workspace Path
        self.workspace_path = os.path.join(self.project_path, "01-Software-Configuration")
        self.workspace_dir = ""
        # Hardware Configurations Path
        self.hardware_configurations_path = os.path.join(self.project_path, "02-Hardware-Configuration")
        # Hardware Configurations - List of all rhw objects in Project
        self.hardware_configurations = []
        # Deployment
        self.deployments = []
        # Deployment Path
        self.deployment_path = os.path.join(self.project_path, "03-Deployment")

        # ROS Workspace Builder
        self.builder = ROS_Workspace_Builder(self)
        # Hardware Configuations Builder
        self.hardware = ROS_Hardware_Builder(self)
        # Deployment Builder
        self.deployment_builder = None

        # Global list of null references
        self.null_references = []
        self.checked_references = False

    # Create a new ROSMOD Project
    def new(self, project_name = "", project_path = ""):
        print "ROSTOOLS::Creating project " + project_name + " at " + project_path
        if project_name != "":
            self.project_name = project_name
        else:
            print "ROSTOOLS::ERROR::Invalid Project Name"
        if project_path != "":
            self.project_path = project_path
        else:
            print "ROSTOOLS::ERROR::Invalid Project Path"
        self.project_path = os.path.join(self.project_path, self.project_name)
        if not os.path.exists(self.project_path):
            os.makedirs(self.project_path)
        project = project_name + ".rosmod"
        with open(os.path.join(self.project_path, project), 'w') as temp_file:
            temp_file.write("This is a ROSMOD Project")
            temp_file.close() 
        self.workspace_path = os.path.join(self.project_path, "01-Software-Configuration")
        self.hardware_configurations_path = os.path.join(self.project_path, "02-Hardware-Configuration")
        self.deployment_path = os.path.join(self.project_path, "03-Deployment")
        if not os.path.exists(os.path.join(self.project_path, "01-Software-Configuration")):
            os.makedirs(self.workspace_path)
        if not os.path.exists(os.path.join(self.project_path, "02-Hardware-Configuration")):
            os.makedirs(self.hardware_configurations_path)
        if not os.path.exists(os.path.join(self.project_path, "03-Deployment")):
            os.makedirs(self.deployment_path)        

    # Open an existing ROSMOD Project
    def open(self, project_path):
        valid_project = False
        project_directories = []
        for prj_file in os.listdir(project_path):
            if prj_file.endswith(".rosmod"):
                print "ROSTOOLS::Opening ROSMOD Project:", project_path
                valid_project = True

        if valid_project == True:
            print "ROSTOOLS::Project Name:", os.path.basename(project_path)
            print "ROSTOOLS::Project Path:", project_path
            sub_directories = [x[0] for x in os.walk(project_path)]
            for sd in reversed(sub_directories):
                project_directories.append(sd)
            del project_directories[-1]
            
            # Find subdirectories
            sd_count = 0
            for pd in project_directories:
                if "01-Software-Configuration" in pd:
                    sd_count += 1
                elif "02-Hardware-Configuration" in pd:
                    sd_count += 1
                elif "03-Deployment" in pd:
                    sd_count += 1

            # If all is well, reinitialize the project with the right name & path
            if sd_count >= 3:
                self.__init__(name=os.path.basename(project_path), path=project_path)
                self.parse_models()
            else:
                print "ROSTOOLS::ERROR::Invalid Project!"

    # Parse .rml software configurations model
    def parse_rml(self, filename):
        print "ROSTOOLS::Parsing File:", filename
        # Read the input model
        model = FileStream(filename)
        # Instantiate the ROSLexer
        lexer = ROSLexer(model)
        # Generate Tokens
        stream = CommonTokenStream(lexer)
        # Instantiate the ROSParser
        parser = ROSParser(stream)
        # Parse from starting point of grammar
        tree = parser.start()
        # Instantiate a Parse Tree Walker
        walker = ParseTreeWalker()

        self.builder.workspace.properties["name"] = os.path.basename(filename.split(".")[0])
        print "ROSTOOLS::Reading ROS Workspace:", self.builder.workspace.properties["name"]

        # Walk the parse tree
        walker.walk(self.builder, tree)

        self.workspace =  self.builder.workspace
        return self.workspace

    # Parse .rhw hardware configurations model
    def parse_rhw(self, filename):
        print "ROSTOOLS::Parsing File:", filename
        # Read the hardware configurations model
        model = FileStream(filename)
        # Instantiate the HostsLexer
        lexer = HostsLexer(model)
        # Generate Tokens
        stream = CommonTokenStream(lexer)
        # Instantiate the HostsParser
        parser = HostsParser(stream)
        # Parse from starting point of grammar
        tree = parser.start()
        # Instantiate a Parse Tree Walker
        walker = ParseTreeWalker()

        # Walk the parse tree
        walker.walk(self.hardware, tree)

        self.hardware.hardware_configuration.properties["name"] = os.path.basename(filename.split(".")[0])
        print "ROSTOOLS::Reading Hardware Configuration:", self.hardware.hardware_configuration.properties["name"]
        self.hardware_configurations.append(self.hardware.hardware_configuration)
        self.hardware = ROS_Hardware_Builder(self)

    # Parse .rdp software deployment model
    def parse_rdp(self, filename):
        print "ROSTOOLS::Parsing File:", filename
        # Read the hardware configurations model
        model = FileStream(filename)
        # Instantiate the DeploymentLexer
        lexer = DeploymentLexer(model)
        # Generate Tokens
        stream = CommonTokenStream(lexer)
        # Instantiate the DeploymentParser
        parser = DeploymentParser(stream)
        # Parse from starting point of grammar
        tree = parser.start()
        # Instantiate a Parse Tree Walker
        walker = ParseTreeWalker()    

        # Create a deployment builder using the 
        # update workspace & hardware configurations objects
        deployment_name = os.path.basename(filename.split(".")[0])
        self.deployment_builder = ROS_Deployment_Builder(self.workspace, self.hardware_configurations, deployment_name, self)

        # Walk the parse tree
        walker.walk(self.deployment_builder, tree)

        self.deployments.append(self.deployment_builder.deployment)
        return self.deployments

    # Parse all model files in all aspects of Project
    def parse_models(self):
        count = 0
        for rml in os.listdir(self.workspace_path):
            if rml.endswith(".rml"):
                rml_file = os.path.join(self.workspace_path, rml)
                count += 1
                
        if count == 0:
            print "ROSTOOLS::No ROSMOD (.rml) file found in", self.workspace_path
        elif count > 1:
            print "ROSTOOLS::ERROR::There can only be one .rml file in 01-ROS-Workspace!"
        else:
            self.workspace = self.parse_rml(rml_file)
        count = 0

        for rhw in os.listdir(self.hardware_configurations_path):
            if rhw.endswith(".rhw"):
                rhw_file = os.path.join(self.hardware_configurations_path, rhw)
                self.parse_rhw(rhw_file)
                count += 1

        if count == 0:
            print "ROSTOOLS::No ROS Hardware Configurations (.rhw) files found in", self.hardware_configurations_path

        count = 0

        for rdp in os.listdir(self.deployment_path):
            if rdp.endswith(".rdp"):
                rdp_file = os.path.join(self.deployment_path, rdp)
                self.parse_rdp(rdp_file)
                count += 1
                
        if count == 0:
            print "ROSTOOLS::No ROS Deployment (.rdp) files found in", self.deployment_path

        self.resolve_references()

    # Resolving Null references in all workspace packages
    def resolve_references(self):
        print "ROSTOOLS::Checking for unresolved references..."
        object_kind = ""
        remove_list = []
        for obj in self.null_references:
            if "publisher" in obj.kind or "subscriber" in obj.kind:
                package = obj.properties["message_text"].split('/')[0]
                reference = obj.properties["message_text"].split('/')[-1]
                # First, find the package
                for child in self.workspace.children:
                    if child.properties["name"] == package:
                        # Get all its messages
                        for msg in child.getChildrenByKind("message"):
                            if msg.properties["name"] == reference:
                                obj.properties["message_reference"] = msg
                                remove_list.append(obj)
            if "client" in obj.kind or "server" in obj.kind:
                package = obj.properties["service_text"].split('/')[0]
                reference = obj.properties["service_text"].split('/')[-1]
                # First, find the package
                for child in self.workspace.children:
                    if child.properties["name"] == package:
                        # Get all its services
                        for srv in child.getChildrenByKind("service"):
                            if srv.properties["name"] == reference:
                                obj.properties["service_reference"] = srv
                                remove_list.append(obj)
            if "component_instance" in obj.kind:
                package = obj.properties["component_text"].split('/')[0]
                reference = obj.properties["component_text"].split('/')[-1]
                # First, find the package
                for child in self.workspace.children:
                    if child.properties["name"] == package:
                        # Get all components
                        for comp in child.getChildrenByKind("component"):
                            if comp.properties["name"] == reference:
                                obj.properties["component_reference"] = comp
                                remove_list.append(obj)

        # Removed not-null references from list
        for obj in remove_list:
            self.null_references.remove(obj)
        # Check for remaining null references
        if len(self.null_references) > 0 and self.checked_references == False:
            print self.null_references
            print "ROSTOOLS::ERROR::Unable to resolve all null references"
            for obj in self.null_references:
                if obj.kind == "publisher" or obj.kind == "subscriber":
                    print "ROSTOOLS::ERROR::Invalid Reference " + obj.properties["message_text"] + " used when defining " +  obj.kind + " " + obj.properties["name"]
                if obj.kind == "client" or obj.kind == "server":
                    print "ROSTOOLS::ERROR::Invalid Reference " + obj.properties["service_text"] + " used when defining " +  obj.kind + " " + obj.properties["name"]
                if obj.kind == "component_instance":
                    print "ROSTOOLS::ERROR::Invalid Reference " + obj.properties["component_text"] + " used when defining " +  obj.kind + " " + obj.properties["name"]
        self.checked_references = True

    # Check workspace directory for existing code that may
    # require preservation
    def check_workspace(self):
        # Instantiate a Loader Object
        business_logic = Workspace_Loader()
        # Use load to load existing business logic
        business_logic.load(self.workspace, self.workspace_path)
    
    # Generate the ROS workspace corresponding to the input model
    def generate_workspace(self):
        # Check for an existing workspace in workspace_path
        self.check_workspace()
        # Instantiate a Generator Object
        workspace = Workspace_Generator()
        # Use listener_object to generate ROS workspace
        self.workspace_dir = workspace.generate(self.workspace, self.workspace_path, self.deployments, self.deployment_path)

    # Generate a ROS model from a workspace object
    # Used to save an edited model
    def save_rml(self, path=""):
        if path == "":
            path = self.workspace_path
        rml_namespace = {'workspace': self.workspace}
        t = rml(searchList=[rml_namespace])
        self.rml = str(t)
        with open(os.path.join(path, self.workspace.properties["name"] + ".rml"), 'w') as temp_file:
            temp_file.write(self.rml)
        print "ROSTOOLS::Saving " + self.workspace.properties["name"] + ".rml " + "at " + path

    # Generate a ROS Hardware Configurations model (.rhw file) from a ROS_HW Object
    def save_rhw(self, path=""):
        if path == "":
            path = self.hardware_configurations_path
        for hw in self.hardware_configurations:
            rhw_namespace = {'hardware' : hw}
            t = rhw(searchList=[rhw_namespace])
            self.rhw = str(t)
            with open(os.path.join(path, hw.properties["name"] + ".rhw"), 'w') as temp_file:
                temp_file.write(self.rhw)
                temp_file.close()
            print "ROSTOOLS::Saving " + hw.properties["name"] + ".rhw " + "at " + path

    # Generate a ROS Deployment model (.rdp file) from a ROS_Deployment Object
    def save_rdp(self, path=""):
        if path == "":
            path = self.deployment_path
        for dp in self.deployments:
            rdp_namespace = {'deployment' : dp}
            t = rdp(searchList=[rdp_namespace])
            self.rdp = str(t)
            with open(os.path.join(path, dp.properties["name"] + ".rdp"), 'w') as temp_file:
                temp_file.write(self.rdp)
                temp_file.close()
            print "ROSTOOLS::Saving " + dp.properties["name"] + ".rdp " + "at " + path   

    # Save the entire project
    def save(self, project_name = "", project_path = ""):
        if project_path == "":
            project_path = self.project_path
        else:
            self.new(project_name, project_path)

        # Save the ROS Workpace Model
        self.save_rml()
        # Save the ROS Hardware Configurations Model
        self.save_rhw()
        # Save the ROS Deployment Model
        self.save_rdp()

if __name__ == "__main__":

    # Testing ROS Tools Features
    My_Project = ROS_Project()
    My_Project.open("/home/pranav/Repositories/rosmod/code/rosmod_v2/ros_tools/sample")
    My_Project.generate_workspace()
    My_Project.save()
       
