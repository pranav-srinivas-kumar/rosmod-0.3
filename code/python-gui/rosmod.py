#!/usr/bin/python
'''
This Program is designed to be the user interface
for the ROSMOD modeling language.  It has the ability
to create, load, display, edit, and export ROSMOD models.

Additionally, it supports the interaction with analysis
tools through the use of toolbar buttons and subprocesses.
'''

from Tkinter import *
import tkFileDialog
import tkMessageBox

from collections import OrderedDict

from rosmod_tools import *
from rosmod_editor import *
from rosmod_classes import *

import sys

sys.path.append('../ros_generator/python/')

import rosgen as rg

class App:

    def __init__(self, master):

        '''
        -----------------------------------------------------
        -----------------------------------------------------
        THIS CODE IS FOR DEBUGGING ONLY
        -----------------------------------------------------
        -----------------------------------------------------
        '''

        serv1 = Service("basicService1",
                        """string hello
---
string retval"""
        )
        serv2 = Service("basicService2")
        msg1 = Message("basicMessage1")
        msg2 = Message("basicMessage2")
        msg3 = Message("basicMessage3")
        c1 = Component("Comp0Def")
        c1.addPub("pub0",msg1)
        c1.addPub("pub1",msg2)
        c1.addTimer("Timer0",Timer('TimerDef',1.0,False))
        c1.addSub("sub0",msg1)
        c1.addClient("client",serv1)
        c1.addServer("server",serv1)
        node1 = Node("sat0")
        node1.addComponent("Comp0",c1)
        node1.addComponent("Comp1",c1)
        node2 = Node("sat1")
        node2.addComponent("OtherComp",c1)
        package1 = Package()
        package1.addNode(node1.name,node1)
        self.Model = Model()
        self.Model.addPackage("mainPackage",package1)
        self.Model.addMessage(msg1)
        self.Model.addMessage(msg2)
        self.Model.addMessage(msg3)
        self.Model.addService(serv1)
        self.Model.addService(serv2)
        self.Model.components[c1.name] = c1
        self.Model.nodes[node1.name] = node1
        self.Model.nodes[node2.name] = node2
        '''
        -----------------------------------------------------
        -----------------------------------------------------
        END DEBUGGING CODE
        -----------------------------------------------------
        -----------------------------------------------------
        '''        

        self.master = master

        self.fileFormats = [
            ('ROSMOD Model','*.rosml')
        ]

        ''' Set up the program's menu '''
        menuDictDict = OrderedDict()
        fileDict = OrderedDict()
        fileDict['New Model']=self.menubar_New_Callback
        fileDict['Open Model']=self.menubar_Open_Callback
        fileDict['Save Model']=self.menubar_Save_Callback
        fileDict['Quit']=self.menubar_Quit_Callback
        optionsDict = OrderedDict()
        helpDict = OrderedDict()
        helpDict['Version']=self.menubar_Version_Callback
        helpDict['Author']=self.menubar_Author_Callback
        helpDict['Email']=self.menubar_Email_Callback

        menuDictDict['File'] = fileDict
        menuDictDict['Options'] = optionsDict
        menuDictDict['Help'] = helpDict

        self.menubar = MenuBar(self.master,menuDictDict)


        ''' Set up the toolbar '''
        toolbarMap = OrderedDict()
        toolbarMap['interpret'] = self.toolbar_Interpret_Callback
        toolbarMap['Network QoS'] = self.toolbar_NetworkAnalysis_Callback
        toolbarMap['BL Timing'] = self.toolbar_TimingAnalysis_Callback
        self.toolbar = ToolBar(self.master,toolbarMap)

        ''' Set up the Status Bar for messages '''
        self.statusBar = StatusBar(self.master)
        self.statusBar.pack(side=BOTTOM, fill=X)

        ''' Set up the Editor ''' 
        self.editorHeight = 800
        self.editorWidth = 800
        self.objectWidth = 100

        objectDict = OrderedDict()
        objectDict['service'] = ["green",("object","service")]
        objectDict['message'] = ["blue",("object","message")]
        objectDict['timer'] = ["gray",("object","timer")]
        objectDict['component'] = ["red",("object","component")]
        objectDict['node'] = ["cyan",("object","node")]

        self.editor = Editor(
            master = self.master,
            height = self.editorHeight,
            width = self.editorWidth,
            splitWidth = self.objectWidth,
            maxWidth = self.editorHeight * 2,
            maxHeight = self.editorHeight * 2,
            editorDict = objectDict,
            model = self.Model
        )

        self.master.protocol("WM_DELETE_WINDOW", self.close_Callback)

    '''
    -------------
    Exit Handler:
    -------------
    '''
    def close_Callback(self):
        if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
            self.master.quit()

    '''
    ------------------------
    Menu Callback Functions:
    ------------------------
    '''
    def menubar_Open_Callback(self):
        file = tkFileDialog.askopenfile(
            parent=self.master,
            mode='rb',
            filetypes=self.fileFormats,
            title="Select Model"
        )
        if file != None:
            self.fileName = file.name
            self.statusBar.set("Opened {0}".format(self.fileName))
            file.close()
            #implement the open functionality here to load the model in
            #self.Model = Model()
            #self.editor.modelViewer.canvas.delete(ALL)
            #self.editor.modelViewer.drawModel()        

    def menubar_New_Callback(self):
        self.statusBar.set("Creating new model.")
        self.Model = Model()
        self.editor.modelViewer.canvas.delete(ALL)
        self.editor.modelViewer.drawModel()

    def menubar_Save_Callback(self):
        fileName = tkFileDialog.asksaveasfilename(
            parent=self.master,
            filetypes=self.fileFormats,
            title="Save the model as..."
        )
        if len(fileName) > 0:
            self.statusBar.set("Saving model as {0}".format(fileName))
        #implement the save functionality here to write self.Model out

    def menubar_Version_Callback(self):
        self.statusBar.set("ROSMOD GUI Version 0.0.1")

    def menubar_Author_Callback(self):
        self.statusBar.set("William Emfinger; Pranav Srinivas Kumar")

    def menubar_Email_Callback(self):
        self.statusBar.set("emfinger@isis.vanderbilt.edu; pkumar@isis.vanderbilt.edu")

    def menubar_Quit_Callback(self):
        self.close_Callback()

    '''
    ---------------------------
    Toolbar Callback Functions:
    ---------------------------
    '''
    def toolbar_Interpret_Callback(self):
        self.statusBar.set("Generating ROS package files!")
        rg.main(["hello",self.fileName])
        #os.system("python ../ros_generator/python/rosgen.py {0}".format(self.fileName))
        
    def toolbar_NetworkAnalysis_Callback(self):
        self.statusBar.set("Analyzing the network characteristics!")

    def toolbar_TimingAnalysis_Callback(self):
        self.statusBar.set("Analyzing the business logic timing characteristics!")

if __name__ == "__main__":

    root = Tk()

    app = App(root)

    root.mainloop()
