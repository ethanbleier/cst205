rgb = 250, 249, 70

if (rgb[0] > rgb[1]) and (rgb[0] > rgb[2]):
    print('The color is reddish.')
elif (rgb[1] > rgb[0]) and (rgb[1] > rgb[2]):
    print('The color is greenish.')
elif (rgb[2] > rgb[0]) and (rgb[2] > rgb[1]):
    print('The color is blueish.')
elif (rgb[1] == rgb[2]):
    print('The color is a shade of cyan.')
elif (rgb[0] == rgb[2]):
    print('The color is a shade of magenta.')
elif (rgb[0] == rgb[1]):
    print('The color is a shade of yellow.')