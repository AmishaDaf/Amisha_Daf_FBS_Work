l=int(input('Enter the Length of rectangle: '))
b=int(input('Enter the bredth of rectangle: '))
r=int(input('Enter the radius of circle: '))

rec_area=l*b
cir_area=(3.14* r * r)/2

Area=rec_area + cir_area

rec_p= 2*(l+b)
cir_p=3.14*r

Perimeter=rec_p + cir_p

print('Area is ',Area)
print('Perimeter is',Perimeter)



