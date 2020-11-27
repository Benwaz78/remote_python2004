# area  = 3.142 * r^2
# area_triangle = 0.5 *base * height

area = lambda r:3.142 * r*r

print(area(5))

area_triangle = lambda base, height: 0.5 * base * height
print(area_triangle(10, 20))