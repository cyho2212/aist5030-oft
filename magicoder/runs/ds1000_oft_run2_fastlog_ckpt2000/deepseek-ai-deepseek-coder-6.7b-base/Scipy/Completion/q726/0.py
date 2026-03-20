data_rot = rotate(data_orig, angle)
xrot, yrot = np.round(np.dot(np.array([[np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle))], [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))]]), np.array([x0, y0]))).astype(int)
