# PACE   

Requires Python3.7 and Pygame     

opto2560.py:
  -scaled to support ultra-wide display
  -no longer updating opto.py
  -changes made from opto.py to ensure correctness

opto.py:    
  -goal to simulate optokinetic tape movement   
  -keep track of location of red segments that enter green highlighted area  
  -write these segments' x,y location to file along with time   
  -keep track of mouse cursor x,y  
  -write mouse cursor x,y to file along with time   
  -use tobii camera to control mouse cursor via eye location   
  -analyze data   

  TODO/DONE   
  *animation of ribbon - done   
  *tracking position of red rectangles in focus zone - DONE   
  *recording cursor location - DONE   
  *recording time of each update - DONE   
  *writing block location and time to file - DONE  
  *writing mouse location and time to file - DONE  
  *adapt code for project hardware specs - DONE
  *make rand test multithreaded
  *implement further visual tests    
