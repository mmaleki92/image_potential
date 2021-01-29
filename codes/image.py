a=5
num = 2
pos_x = np.random.rand(num)*(a-1)
pos_y = np.random.rand(num)*(a-1)

grid = 256
points = np.linspace(0, a, grid)

pos_x,pos_y

X, Y = np.meshgrid(points, points)
image = np.zeros((grid, grid))

for p_x,p_y in zip(pos_x,pos_y):

    dx1 = X - p_x
    dy1 = Y - p_y

    dr1 = np.sqrt(dx1** 2 + dy1**2)

    image = image + np.exp(- (dr1**2 / (2 * (0.2 **2))))
plt.imshow(image,cmap=plt.cm.get_cmap('Blues', 6))
#plt.show()
#plt.imshow(image,cmap='RdBu')

plt.colorbar()
plt.savefig('lj_image.png',dpi = 500)
