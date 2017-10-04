
import abscplane
import numpy as np

class ListComplexPlane(abscplane.AbsComplexPlane):
    
        def __init__(self,xmin,xmax,xlen,ymin,ymax,ylen):
        self.xmin  = float(xmin)
        self.xmax  = float(xmax)
        self.xlen  = int(xlen)
        self.ymin  = float(ymin)
        self.ymax  = float(ymax)
        self.ylen  = int(ylen)
        # The implementation type of plane is up to the user
        self.plane = self.__creategrid__()
        # fs should be a list of functions, initialized to be empty
        self.fs    = []
        
   
    def __creategrid__(self):
        
        x = np.linspace(self.xmin,self.xmax,self.xlen)
        y = np.linspace(self.ymin,self.ymax,self.ylen)
        
        x,y = np.meshgrid(x,y)
        return pd.DataFrame(x+1j*y)
        
    #[[(self.xmin + i*dx)+(self.ymin + j*dy)*1j for i in range(self.xlen)] for j in range(self.ylen)]
        #list comprehension to compress for loop that is creating a new list of values
        
    def refresh(self):
        self.fs = []
        self.plane = self.__creategrid__()
        
        
    
    '''The method self.apply(self,f) should take a function f that transforms 
    a complex number into another complex number and map that function 
    over the complex plane to produce the grid of numbers f(x + y*1j),
    adding the function f to the list self.fs in the process. If the
    method apply is called multiple times with different functions, then
    self.fs should record the ordered sequence of functions, and self.plane
    should contain the final output after applying the entire sequence
    of functions.'''
    def apply(self, f):

        self.plane = self.plane.applymap(f)
        
        self.fs = self.fs.append(f)
    
    def zoom(self,xmin,xmax,xlen,ymin,ymax,ylen):
        """Reset self.xmin, self.xmax, and self.xlen.
        Also reset self.ymin, self.ymax, and self.ylen.
        Regenerate the plane with the new range of the x- and y-axes,
        then apply all transformations in fs in the correct order to
        the new points so that the resulting value of self.plane is the
        final output of the sequence of transformations collected in
        the list self.fs.
        """
        self.xmin  = float(xmin)
        self.xmax  = float(xmax)
        self.xlen  = int(xlen)
        self.ymin  = float(ymin)
        self.ymax  = float(ymax)
        self.ylen  = int(ylen)
        self.plane = self.__creategrid__()
        
        fs=self.fs
        self.fs= []
        
        for f in fs:
            self.apply(f)

#lcp = ListComplexPlane(-10,10,20,-10,10,20)
#for y in lcp.plane:
    #for x in y:
        #print(x)