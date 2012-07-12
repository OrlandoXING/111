from math import sqrt, pi, sin, cos, atan2, acos

def cartesian_2_sphericalPolar(positionVectorCartesian):
    '''Convert cartesian coordinates to radial-azimuthal-polar spherical coordinates, in radians. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent.'''
    #Extract the Cartesian vector comopnents.
    x = positionVectorCartesian[0]
    y = positionVectorCartesian[1]
    z = positionVectorCartesian[2]
    #Calculate the radius.
    radius = sqrt(x**2 + y**2 + z**2)
    #Calculate azimuthal (theta) and zenith (phi) angles
    theta = acos(z/radius)
    phi = atan2(y,x)
    return [radius, theta, phi]

def lonlatdeg_2_xyz(positionVector):
    '''Convert longitude-latitude-radial coordinates on the surface of the Earth (in degrees) to cartesian coordinates. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent.'''
    return X

def cartesian_2_lonlatradius(positionVectorCartesian):
    '''Convert cartesian coordinates on a sphere to longitude-latitude-radius, where lon & lat are in radians. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent.'''
    #Calculate azimuthal (phi), polar (theta) angles and distance from origin.
    [radius, theta, phi] = cartesian_2_sphericalPolar(positionVectorCartesian)
    #Claculate longitude and latitude
    lon = phi*180.0/pi
    lat = (pi/2 - theta)*180.0/pi
    
    positionVectorLonlat = [lon, lat, radius]
    return positionVectorLonlat
    

def transform_tensor_sphericalPolar_2_cartesian(positionVectorSpherical, tensor):
    '''Function changing the basis of a tensor from zonal-meridional-radial basis to a cartesian basis. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent. The input position vector must be given as [longitude, latitude, radius], all anlges specified in radians'''
    import scipy as sp
    from scipy import linalg
    #extract distance from origin, polar (theta) angles and azimuthal (phi) angles.
    [radius, theta, phi] = positionVectorSpherical
    #Evaluate components of rotation matrices.
    transformationMatrix =\
       sp.array([\
                 [sp.sin(theta)*sp.cos(phi),   sp.cos(theta)*sp.cos(phi),  -sp.sin(phi)],\
                 [sp.sin(theta)*sp.sin(phi),   sp.cos(theta)*sp.sin(phi),   sp.cos(phi)],\
                 [sp.cos(theta),              -sp.sin(theta),              0]])
    transposedTransformationMatrix = transformationMatrix.transpose()
    #Calculate the components of the tesnor in the reference system.
    transformed_Tensor = sp.dot(transformationMatrix, sp.array(tensor))
    transformed_Tensor = sp.dot(transformed_Tensor,transposedTransformationMatrix)
    return transformed_Tensor

def transform_tensor_cartesian_2_sphericalPolar(positionVectorCartesian, tensor):
    '''Function transforming the components of a tensor from a cartesian basis to a zonal-meridional-radial basis. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent.'''
    import scipy as sp
    from scipy import linalg
    #Calculate azimuthal (theta) and zenith (phi) angles and distance from origin
    [radius, theta, phi] = cartesian_2_sphericalPolar(positionVectorCartesian)
    #Evaluate components of rotation matrices.
    transformationMatrix =\
       sp.array([\
                 [sp.sin(theta)*sp.cos(phi),   sp.sin(theta)*sp.sin(phi),   sp.cos(theta)],\
                 [sp.cos(theta)*sp.cos(phi),   sp.cos(theta)*sp.sin(phi),   -sp.sin(theta)],\
                 [-sp.sin(phi),                sp.cos(phi),                 0]])
    transposedTransformationMatrix = transformationMatrix.transpose()
    #Calculate the components of the tesnor in the reference system.
    transformed_Tensor = sp.dot(transformationMatrix, sp.array(tensor))
    transformed_Tensor = sp.dot(transformed_Tensor,transposedTransformationMatrix)
    return transformed_Tensor

def transform_vector_sphericalPolar_2_cartesian(positionVectorSpherical, vector):
    '''Function transforming the components of a vector from a spherical-polar basis to a cartesian basis. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent. The input position vector must be given as [longitude, latitude, radius], all anlges specified in radians'''
    import scipy as sp
    #extract distance from origin, polar (theta) angles and azimuthal (phi) angles.
    [radius, theta, phi] = positionVectorSpherical
    #Evaluate components of rotation matrices.
    transformationMatrix =\
       sp.array([\
                 [sp.sin(theta)*sp.cos(phi),   sp.cos(theta)*sp.cos(phi),  -sp.sin(phi)],\
                 [sp.sin(theta)*sp.sin(phi),   sp.cos(theta)*sp.sin(phi),   sp.cos(phi)],\
                 [sp.cos(theta),              -sp.sin(theta),              0]])
    #Calculate the components of the tesnor in the reference system.
    transformed_Vector = sp.dot(transformationMatrix, sp.array(vector))
    return transformed_Vector

def transform_vector_cartesian_2_sphericalPolar(positionVectorCartesian, vector):
    '''Function transforming the components of a vector from a cartesian basis to a spherical-polar basis. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent.'''
    import scipy as sp
    #Calculate distance from origin, polar (theta) angles and azimuthal (phi) angles.
    [radius, theta, phi] = cartesian_2_sphericalPolar(positionVectorCartesian)
    #Evaluate components of rotation matrices.
    transformationMatrix =\
       sp.array([\
                 [sp.sin(theta)*sp.cos(phi),   sp.cos(theta)*sp.cos(phi),  -sp.sin(phi)],\
                 [sp.sin(theta)*sp.sin(phi),   sp.cos(theta)*sp.sin(phi),   sp.cos(phi)],\
                 [sp.cos(theta),              -sp.sin(theta),              0]])
    #Calculate the components of the tesnor in the reference system.
    transformed_Vector = sp.dot(transformationMatrix, sp.array(vector))
    return transformed_Vector

def transform_vector_cartesian_2_lon_lat_rad(positionVectorCartesian, vector):
    '''Function transforming the components of a vector from a cartesian basis to a zonal-meridional-radial basis. The origin of the Cartesian frame of reference is located at the centre of the sphere, the positive half of x-axis goes through 0 deg E, 0 deg N, the positive half of y-axis goes through 90 deg E, 0 deg N and the positive half of the z axis goes through the North Pole equivalent.'''
    #Calculate spherical-polar components of the vector.
    [radial, azimuthal, polar] = transform_vector_cartesian_2_sphericalPolar(positionVectorCartesian, vector)
    #Calculate zonal, meridional and radial components of the vector.
    transformed_Vector[0] = polar
    transformed_Vector[1] = -azimuthal
    transformed_Vector[2] = radial
    return transformed_Vector

def transform_vector_sphericalPolar_2_lon_lat_rad(vector):
    '''Function transforming the components of a vector from a spherical-polar basis to a zonal-meridional-radial basis.'''
    import scipy as sp
    #The requested transformation is just a reflection followed by a change in the order
    # of the components in order to get a right-handed system.
    transformationMatrix = sp.array([[ 0.0, 0.0, 1.0 ],\
                                     [ 0.0,-1.0, 0.0 ],\
                                     [ 1.0, 0.0, 0.0 ]])
    transformed_Vector = sp.dot(transformationMatrix, sp.array(vector))
    return transformed_Vector

def transform_vector_lon_lat_rad_2_sphericalPolar(vector):
    '''Function transforming the components of a vector from a zonal-meridional-radial basis to a spherical-polar basis.'''
    import scipy as sp
    #The requested transformation is just a reflection followed by a change in the order
    # of the components in order to get a right-handed system.
    transformationMatrix = sp.array([[ 0.0, 0.0, 1.0 ],\
                                     [ 0.0,-1.0, 0.0 ],\
                                     [ 1.0, 0.0, 0.0 ]])
    transformed_Vector = sp.dot(transformationMatrix, sp.array(vector))
    return transformed_Vector

def transform_tensor_sphericalPolar_2_lon_lat_rad(tensor):
    '''Function transforming the components of a tensor from a spherical-polar basis to a zonal-meridional-radial basis.'''
    import scipy as sp
    #The requested transformation is just a reflection followed by a change in the order
    # of the components in order to get a right-handed system.
    transformationMatrix = sp.array([[ 0.0, 0.0, 1.0 ],\
                                     [ 0.0,-1.0, 0.0 ],\
                                     [ 1.0, 0.0, 0.0 ]])
    transformed_Tensor = sp.dot(sp.dot(transformationMatrix, sp.array(tensor)), transformationMatrix)
    return transformed_Tensor

def transform_tensor_lon_lat_rad_2_sphericalPolar(tensor):
    '''Function transforming the components of a tensor from a zonal-meridional-radial basis to a spherical-polar basis.'''
    import scipy as sp
    #The requested transformation is just a reflection followed by a change in the order
    # of the components in order to get a right-handed system.
    transformationMatrix = sp.array([[ 0.0, 0.0, 1.0 ],\
                                     [ 0.0,-1.0, 0.0 ],\
                                     [ 1.0, 0.0, 0.0 ]])
    transformed_Tensor = sp.dot(sp.dot(transformationMatrix, sp.array(tensor)), transformationMatrix)
    return transformed_Tensor
