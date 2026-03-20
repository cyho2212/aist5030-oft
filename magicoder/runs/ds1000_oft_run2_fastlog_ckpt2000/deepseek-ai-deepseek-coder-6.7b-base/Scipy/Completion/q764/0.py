    tck = scipy.interpolate.bisplrep(s, t, z, s=0)
    return scipy.interpolate.bisplev(s, t, tck)
