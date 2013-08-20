#Mandelbrot Set Generator-----------------------------------------------------#
#August 20, 2013--------------------------------------------------------------#
#By Kyle Buchanan-------------------------------------------------------------#
#-----------------------------------------------------------------------------#


#Importing the needed libraries-----------------------------------------------#
import math
import pygame
import time
#-----------------------------------------------------------------------------#


#Setting some constants, should be pretty straightforward---------------------#
screensize = (600,600)
scale = 250
center = (-0.7,0)
iterations = 30
colour = (0.2,0.6,1) #Sort of a sky-blue-ish colour---------------------------#
#-----------------------------------------------------------------------------#


#Drawing the window-----------------------------------------------------------#
screen = pygame.display.set_mode(screensize)
#-----------------------------------------------------------------------------#


#This is just for readability-------------------------------------------------#
def pixel_change(position,colour):
	screen.set_at(position,colour)
#-----------------------------------------------------------------------------#


#Two simple 2-D vector math thingies------------------------------------------#	
def vector_square(i):
	return (i[0]*i[0]-i[1]*i[1],2*i[0]*i[1])
	
def vector_add(i,j):
	return (i[0]+j[0],i[1]+j[1])
#-----------------------------------------------------------------------------#

	
#Loops over the points corresponding to every pixel in the window-------------#
for y in range(screensize[1]):
	for x in range(screensize[0]):
	
		
		#This is just the initial position of the point, which gets added to--#
		#the function on every iteration--------------------------------------#
		constant = ((x-screensize[0]/2)/scale+center[0],(y-screensize[1]/2)/scale-center[1])
		#---------------------------------------------------------------------#
		
		
		#Resetting the position, new position, and pixel intensity to zero----#
		#'intensity' is basically a measure of how fast the iterated function-#
		#increases------------------------------------------------------------#
		pos_ = [0,0]
		pos_new = [0,0]
		intensity = 0
		#---------------------------------------------------------------------#
		
		
		#Now here's the loop that figured out whether the function is bounded-#
		#at a point, making it part of the Mandelbrot set.--------------------#
		for n in range(iterations):
		
		
			#If it gets above 10, it definitely ain't coming back, so might as#
			#well break the loop and use this to make the pretty colours.-----#
			if pos_[0]*pos_[0]+pos_[1]*pos_[1] > 10:
				intensity = 1000/n
				break
			#-----------------------------------------------------------------#
			
			#Squares the point and adds the initial point---------------------#
			pos_new = vector_add(vector_square(pos_),constant)
			#-----------------------------------------------------------------#
			
			
			#Sets the position equal to the new position----------------------#
			pos_[0] = pos_new[0]
			pos_[1] = pos_new[1]
			#-----------------------------------------------------------------#
			
			
		#Draw the pixel based on how quickly the function increases-----------#
		if intensity > 255:
			intensity = 255
		pixel_change((x,y),(colour[0]*intensity,colour[1]*intensity,colour[2]*intensity))
		#---------------------------------------------------------------------#
		
		
	#Redraw the screen--------------------------------------------------------#	
	pygame.display.flip()
	#-------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
	

#Wait 10 seconds--------------------------------------------------------------#
time.sleep(10)
#-----------------------------------------------------------------------------#
