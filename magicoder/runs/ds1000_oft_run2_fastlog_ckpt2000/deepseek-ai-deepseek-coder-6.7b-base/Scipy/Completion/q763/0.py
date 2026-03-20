interp = scipy.interpolate.interp2d(s, t, z, kind='cubic')
result = interp(s, t)
