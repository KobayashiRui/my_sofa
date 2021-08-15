import Sofa.Core

def createScene(rootNode):
        rootNode.createObject('RequiredPlugin', pluginName='CGALPlugin')
        node = rootNode.createChild('node')
        node.createObject('Mesh',name='mesh',filename='./chamber_test1.stl')
        node.createObject('MeshGenerationFromPolyhedron',inputPoints='@mesh.position', 
                            inputTriangles='@mesh.triangles', drawTetras='1')
        node.createObject('Mesh', position='@gen.outputPoints', tetrahedra='@gen.outputTetras')
        node.createObject('VTKExporter', filename='chamber_test1', edges='0', tetras='1', exportAtBegin='1')