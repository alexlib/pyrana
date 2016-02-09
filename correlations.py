import numpy as np
import numpy.fft as fft
import scipy.ndimage as img
import matplotlib.pyplot as plt
import os
import pdb

class Correlation:
    def __init__(self, data = None):
        self.Data = data;

    def SwitchDomains(self, direction = 1):
        if direction > 0:
            self.Data = fft.fftshift(np.abs(np.real(fft.ifft2(self.Data))))
        if direction < 0:
            self.Data = fft.fft2(self.Data)
            
    # def Subpixel(self, method = 1):
        
        

class InterrogationRegion:
    def __init__(self, data = None):
        if data is not None:
            # The data array
            self.Data = data;

            # Region shape
            shape = data.shape;

            # The region dimensions
            self.Height = shape[0]
            self.Width  = shape[1]
        

class RegionList:
    def __init__(self, Regions = None):
        if Regions is not None:
            
            # Number of regions
            num_regions = len(Regions)
            
            # Define the region list
            region_list = [];
            
            # Populate the list
            for k in range(num_regions):
                region_list.append(InterrogationRegion(Regions[k]))
            
            # Append list    
            self.Regions = region_list
                
                
    def SpectralCrossCorrelation(self, cstep = 1):
        
        # Measure the length of the list
        num_regions = len(self.Regions)
        
        # Width and height
        height = self.Regions[0].Height;
        width  = self.Regions[0].Width;
        
        # Allocate the correlation
        spectral_corr = Correlation(np.zeros((height, width), dtype = "complex"))
        
        # Calculate the FT of the first region.
        # Do this outside the loop so that we
        # only have to perform one FFT per iteration.
        ft_01 = fft.fft2(self.Regions[0].Data)
        
        # Correlate all the regions
        for k in range(num_regions - 1):    
            ft_02 = fft.fft2(self.Regions[k].Data)
            
            # Conjugate multiply
            spectral_corr.Data += ft_01 * np.conj(ft_02);
            
            # Shift the second FT into
            # the position of the first FT.
            ft_01 = ft_02
            
        return spectral_corr
        
    def SCC(self):
        
        # pdb.set_trace()
        
        # Spectral cross correlation
        correlation = self.SpectralCrossCorrelation()
        
        # 
        correlation.SwitchDomains()
        
        # Switch to the spatial domain
        return(correlation);
        
        # IFFT
        
        
        
    
            




# class correlation:
#
#
















