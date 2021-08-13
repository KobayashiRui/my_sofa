import pymesh


input_mesh = pymesh.load_mesh("./chamber_test1.stl")
tetgen = pymesh.tetgen()
tetgen.points = input_mesh.vertices # Input points.
tetgen.triangles = input_mesh.faces # Input triangles
tetgen.max_tet_volume = 0.01
tetgen.verbosity = 0
tetgen.run() # Execute tetgen
mesh = tetgen.mesh # Extract output tetrahedral mesh.