import math
perc = 1/3
coco_wt = 1450
macaw_wt = 900
macaw_limit = macaw_wt*perc
no_macaw_need = coco_wt/macaw_limit
print(macaw_limit)
print(no_macaw_need)
math.ceil(no_macaw_need)
print("After rounding off: ", math.ceil(no_macaw_need))

