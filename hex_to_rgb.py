# Source
# https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python

h = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(h[i:i+2], 16) for i in (0, 2, 4)))