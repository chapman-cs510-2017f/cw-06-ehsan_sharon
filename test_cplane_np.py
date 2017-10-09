#!/usr/bin/env python3
from cplane_np import ArrayComplexPlane, np, pd

#test __init__ & __creategrid__
def test_creategrid():
    
    retlcp = ArrayComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-1+-1*1j), (0+-1*1j), (1+-1*1j)],
        [(-1+0*1j), (0+0*1j), (1+0*1j)],
        [(-1+1*1j), (0+1*1j), (1+1*1j)]
    ]
    testplane = pd.DataFrame(testplane)
    #print(retlcp.plane)
    #print(testplane)
    assert testplane.equals(retlcp.plane)
    print("test_creategrid pass")
    
test_creategrid()

#test refresh
def test_refresh():
    retlcp = ArrayComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-1+-1*1j), (0+-1*1j), (1+-1*1j)],
        [(-1+0*1j), (0+0*1j), (1+0*1j)],
        [(-1+1*1j), (0+1*1j), (1+1*1j)]
    ]
    testplane = pd.DataFrame(testplane)
    
    def f():
        pass
    retlcp.fs = [f]
    retlcp.refresh()
    assert testplane.equals(retlcp.plane) and retlcp.fs == []
    print("test_refresh pass")
    
test_refresh()

#test apply
def test_apply():
    retlcp = ArrayComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-2+-2*1j), (0+-2*1j), (2+-2*1j)],
        [(-2+0*1j), (0+0*1j), (2+0*1j)],
        [(-2+2*1j), (0+2*1j), (2+2*1j)]
    ]
    testplane = pd.DataFrame(testplane)
    
    def f(p):
        return p*2
    
    retlcp.apply(f)
    assert testplane.equals(retlcp.plane)
    print("test_apply pass")
    
test_apply()

#test zoom
def test_zoom():
    
    retlcp = ArrayComplexPlane(-1,1,3,-1,1,3) #return lcp
    testplane = [
        [(-2+-2*1j), (0+-2*1j), (2+-2*1j)],
        [(-2+0*1j), (0+0*1j), (2+0*1j)],
        [(-2+2*1j), (0+2*1j), (2+2*1j)]
    ]
    testplane = pd.DataFrame(testplane)
    
    retlcp.zoom(-2,2,3,-2,2,3)
   
    assert testplane.equals(retlcp.plane)
    print("test_zoom pass")
test_zoom()