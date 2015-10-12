from PIL import Image
from termcolor import colored

ascii_chars = [ '#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', ' ']

def image_to_ascii(image):
	image_as_ascii = []
	all_pixels = list(image.getdata())
	for pixel_value in all_pixels:
		index = pixel_value / 25 # 0 - 10
		image_as_ascii.append(ascii_chars[index])
	return image_as_ascii	

if __name__=="__main__":
	amount = input('Enter the amount you wish to donate (in dollars): ')

	# We will dynamically resize the ASCII that we are generating on the basis of the amount that is being donated
        new_width = 40 if amount <= 400 else 60 if amount <= 600 else 80 if amount <=800 else 100
        new_height = new_width/2
	new_image = Image.open("hand.jpg").resize((new_width, new_height)).convert("L") # resize and convert to grayscale
		
        img_as_ascii = image_to_ascii(new_image)
	img_as_ascii = ''.join(ch for ch in img_as_ascii)
	for c in range(0, len(img_as_ascii), new_width):
		print img_as_ascii[c:c+new_width]
        print colored("Lend an even bigger helping hand by donating more! Visit https://www.firsthandfoundation.org/donate/", "green")
