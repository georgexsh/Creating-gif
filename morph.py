#Siddharth Vadgama
#UTA ID-1001397508
import numpy as np
import matplotlib.pyplot as plt

def intermediate(firstImage, lastImage, N, display) :
    """
        if display is True
            display the images
        otherwise
            save as a file with the names mid01.jpg, mid02.jpg, ...
    """
    
    img1=plt.imread(firstImage)
    img2=plt.imread(lastImage)
    delt=(img2.astype(np.float)-img1.astype(np.float))/N
    for j in range(1,N):
        
        temp=img1.astype(float)+(j*delt.astype(float))
        
        #print(temp)
        temp=temp.astype(np.uint8)
        
        if display:
            plt.figure(j)      
            plt.imshow(temp)
            plt.show()    
        else:            
            plt.imsave(f'mid{j:02d}.jpg',temp)
    


###############  main  ###############
if __name__ == "__main__" :
    name1 = "darinYoung.jpg"  # first image
    name2 = "darinOld.jpg"    #  last image
    
    N = 10    # should produce N-1 intermediate images
    
    display = True   # True means display intermediate images
                     # False means save intermediate images
    intermediate(name1, name2, N, display)
