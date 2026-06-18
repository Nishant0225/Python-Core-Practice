# Problem 15:Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
# Note: It may be assumed that the rectangles are parallel to the coordinate axis.
# Rectangle 1
l1x, l1y = map(int, input("Enter L1 (x y): ").split())
r1x, r1y = map(int, input("Enter R1 (x y): ").split())

# Rectangle 2
l2x, l2y = map(int, input("Enter L2 (x y): ").split())
r2x, r2y = map(int, input("Enter R2 (x y): ").split())

# Check if rectangles do NOT overlap
if r1x < l2x or r2x < l1x or l1y < r2y or l2y < r1y:
    print("Not Overlapping")
else:
    print("Overlapping")