import sys
import os

sys.path.append("/Applications/runSofa.app/Contents/MacOS/plugins/SofaPython3/lib/python3/site-packages")

import Sofa
import SofaRuntime


def main():
	# Make sure to load all SOFA libraries
	#SofaRuntime.importPlugin("SofaBaseMechanics")
    SofaRuntime.importPlugin("SofaOpenglVisual")

	# Call the above function to create the scene graph
    root = Sofa.Core.Node("root")
    createScene(root)

    # Once defined, initialization of the scene graph
    Sofa.Simulation.init(root)

    # Run the simulation for 10 steps
    for iteration in range(10):
    	print(f'Iteration #{iteration}')
    	Sofa.Simulation.animate(root, root.dt.value)

    print("Simulation made 10 time steps. Done")


# Function called when the scene graph is being created
def createScene(root):

    root.addObject("OglGrid", nbSubdiv=10, size=1000)
    confignode = root.addChild("Config")
    confignode.addObject('RequiredPlugin', name="SofaPython3", printLog=False)
    confignode.addObject('OglSceneFrame', style="Arrows", alignment="TopRight")
    
    return root


# Function used only if this script is called from a python environment
if __name__ == '__main__':
    main()