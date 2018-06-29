import numpy as np
stride = 1 #CONSTANTS stride
zero_padding = 1 #CONSTANTS level of zero padding

input_volume = np.array([[
			[[3,1,3,8,2],
			[4,1,5,7,9],
			[2,1,4,5,0],
			[4,1,5,8,3],
			[3,1,4,7,2]],
			[[5,4,1,3,8],
			[4,9,1,4,7],
			[7,3,1,4,6],
			[8,4,1,5,2],
			[2,3,1,8,2]],
			[[2,2,3,7,3],
			[6,9,4,4,5],
			[1,1,1,1,1],
			[8,3,4,5,5],
			[7,2,3,1,4]]
			]])

vertical_mask = np.array([[
						[[-1,0,1],
						[-2,0,2],
						[-1,0,1]]
						]])

horizontal_mask = np.array([[
						[[1,2,1],
						[0,0,0],
						[-1,-2,-1]]
						]])

w1 = 5 #CONSTANTS w1 = width of input volume
h1 = 5 #CONSTANTS h1 = height of input volume
d1 = 3 #CONSTANTS d1 = depth of input volume
k = 2 #CONSTANTS k - number of filters
f = 3 #CONSTANTS f = Spatial Extent meaning filter size

output_volume_height = int((h1 - f + 2*zero_padding)/stride + 1) #Computing output volume's height with formula : H2 = (H1 - F + 2P)/S + 1
output_volume_width = int((w1 - f + 2*zero_padding)/stride + 1) #Computing output volume's width with formula : W2 = (W1 - F + 2P)/S + 1
output_volume_depth = k #Computing output volume's depth with formula : D2 = K
result = np.zeros((1,output_volume_depth,output_volume_height,output_volume_width)) #Initialize result matrix with all zeros for the size that we found

print("Output Volume's height: " + str(output_volume_height))
print("Output Volume's width: " + str(output_volume_width))
print("Output Volume's depth: " + str(output_volume_depth))

output_padding = np.pad(input_volume,((0,),(0,),(zero_padding,),(zero_padding,)),mode='constant',constant_values=0) #Padding zeros around the input volume with padding factor of 1
# The below for loop computes the values for horizontal mask placed over input volume with stride of 1
for i in range(output_volume_height):
	for j in range(output_volume_width):
		output_padding_match = output_padding[:, :, i*stride : i*stride + f, j*stride : j*stride + f] #output_padding_match of size which we want
		result[:, 0 , i, j] = np.sum(output_padding_match * horizontal_mask[0, :, :, :]) #Sum of all dot products of horizontal mask and output_padding_match
# The below for loop computes the values for vertical mask placed over input volume with stride of 1
for i in range(output_volume_height):
	for j in range(output_volume_width):
		output_padding_match = output_padding[:, :, i*stride : i*stride + f, j*stride : j*stride + f] #output_padding_match of size which we want
		result[:, 1 , i, j] = np.sum(output_padding_match * vertical_mask[0, :, :, :]) #Sum of all dot products of vertical mask and output_padding_match

print(result)