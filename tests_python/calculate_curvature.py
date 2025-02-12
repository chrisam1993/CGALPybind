import CGALMethods as CM

if __name__ == "__main__":
    surface_mesh = CM.SurfaceMesh("resources/WALL_400.vtk", scale=1000)
    print("Surface mesh prior curvature calculation", surface_mesh)
    surface_mesh.calculate_curvature(4, 4, 300, True)
    surface_mesh.write_vtk("resources/WALL_400_python_write.vtk")
    print("Surface mesh after curvature calculation", surface_mesh)