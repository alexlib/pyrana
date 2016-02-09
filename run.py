from correlations import *
from mpl_toolkits.mplot3d import Axes3D
import pdb

image_dir = "/Users/matthewgiarra/Desktop/images/raw"

# 
file_names = os.listdir(image_dir)

# Get image names
for name in file_names:
    if ".tif" in name:
        

# Image names
img_01_name = "image_01_000001.tif"
img_02_name = "image_02_000001.tif"

img_01_path = os.path.join(image_dir, img_01_name)
img_02_path = os.path.join(image_dir, img_02_name)

# Read the first image
img_01 = img.imread(img_01_path)
img_02 = img.imread(img_02_path)

dims = img_01.shape

width = dims[1]
height = dims[0]

# Show the images
# plt.subplot(1, 3, 1)
# plt.imshow(img_01)
#
# plt.subplot(1, 3, 2)
# plt.imshow(img_02)
#
# plt.subplot(1, 3, 3)

region_list = RegionList([img_01, img_02]);

scc = region_list.SCC().Data;

# pdb.set_trace();

x, y = np.meshgrid(range(width), range(height))

fig = plt.figure();
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(x, y, scc / np.max(scc))



plt.show()        
    
