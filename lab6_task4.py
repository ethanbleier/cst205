import math
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

c2 = (185, 77, 89)
c1 = (176, 63, 81)



#Calculate the Euclidean color distance and
def color_distance(c1, c2):
   r_diff = (c1[0] - c2[0])**2
   g_diff = (c1[1] - c2[1])**2
   b_diff = (c1[2] - c2[2])**2
   return (r_diff + g_diff + b_diff)**(1/2)

print(color_distance(c1, c2))


"""L*a*b* color distance of the two apples.
dL = 4.03
da = -3.05
db = 1.04 """

