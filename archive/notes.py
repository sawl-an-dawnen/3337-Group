#develope system for streaming spatial events
#can this be applied to different regions
#can we use varying types of data sizes (amounts)

#each file contains two months worth of data
#use sliding window to create input data

#hotspot definitions
#small hotspots based on d1 (user defined high density threshold)
#large regional hotspots based on d2 (medium threshhold d2 < d1)

#read data in

#define d1 and d2 based on magnitude and depth

#look at the location
#&
#compare datapoint density to d1 and d2
#if applicable add to map d1 or d2 map

#------------------------------------------------------------------------------

#11/17
#make arbitrary d1 and d2 thresholds 
#if mag x depth > d1
    #add to df1
#if mag x depth > d2 && mag x depth < d1
    #add to df2

#figure out how to animate the plots

#modify the plotting function to overlay map and demonstrate hotspots, instead of
#heatmap