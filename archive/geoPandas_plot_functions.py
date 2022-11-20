import geopandas

def plot_US():
    states = geopandas.read_file('tl_2021_us_state/tl_2021_us_state.shp')
    states = states.to_crs("EPSG:4326")
    non_continental = ['HI','VI','MP','GU','AK','AS','PR']
    
    for n in non_continental:
        states = states[states.STUSPS != n]
        
    return states.boundary.plot(cmap = "Accent", figsize=(12, 12))

def plot_STATE(state):
    states = geopandas.read_file('tl_2021_us_state/tl_2021_us_state.shp')
    states = states.to_crs("EPSG:4326")
    non_continental = ['HI','VI','MP','GU','AK','AS','PR']
    
    for n in non_continental:
        states = states[states.STUSPS != n]
        
    return states[states['NAME'] == state].plot(figsize=(12, 12))

def plot_STATES(sts):
    states = geopandas.read_file('tl_2021_us_state/tl_2021_us_state.shp')
    states = states.to_crs("EPSG:4326")
    non_continental = ['HI','VI','MP','GU','AK','AS','PR']
    
    for n in non_continental:
        states = states[states.STUSPS != n]
        
    group = states[states['STUSPS'].isin(sts)]
        
    return group.plot(cmap='tab10', figsize=(14, 12))

#plot_US()
#plot_STATE('Texas')
# southeast = ['FL','GA','AL','SC','NC', 'TN', 'AR', 'LA', 'MS']
# plot_STATES(southeast)

#https://jcutrer.com/python/learn-geopandas-plotting-usmaps