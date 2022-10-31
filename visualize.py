from tkinter import *
import numpy as np
import cv2


img = cv2.imread('VeryExpensive.png',0)


lst = []
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
         lst.append(np.binary_repr(img[i][j] ,width=8))


mostsignificant = (np.array([int(i[0]) for i in lst],dtype = np.uint8) * 128).reshape(img.shape[0],img.shape[1])
seven_bit_img = (np.array([int(i[1]) for i in lst],dtype = np.uint8) * 64).reshape(img.shape[0],img.shape[1])
six_bit_img = (np.array([int(i[2]) for i in lst],dtype = np.uint8) * 32).reshape(img.shape[0],img.shape[1])
five_bit_img = (np.array([int(i[3]) for i in lst],dtype = np.uint8) * 16).reshape(img.shape[0],img.shape[1])
four_bit_img = (np.array([int(i[4]) for i in lst],dtype = np.uint8) * 8).reshape(img.shape[0],img.shape[1])
three_bit_img = (np.array([int(i[5]) for i in lst],dtype = np.uint8) * 4).reshape(img.shape[0],img.shape[1])
two_bit_img = (np.array([int(i[6]) for i in lst],dtype = np.uint8) * 2).reshape(img.shape[0],img.shape[1])
leastsignificant = (np.array([int(i[7]) for i in lst],dtype = np.uint8) * 1).reshape(img.shape[0],img.shape[1])


top = Tk()

top.geometry("400x100")


def fun(image):
    cv2.imshow('Image', cv2.hconcat([image]))


b1 = Button(top, text="Most Significant bit",command=lambda:fun(seven_bit_img)).grid(row=0,column=1,padx=10,pady=10)

b3 = Button(top, text="7th bit",command=lambda:fun(seven_bit_img)).grid(row=0,column=2,padx=20,pady=10)

b4 = Button(top, text="6th bit",command=lambda:fun(six_bit_img)).grid(row=0,column=3,padx=20,pady=10)

b5 = Button(top, text="5th bit",command=lambda:fun(five_bit_img)).grid(row=0,column=4,padx=20,pady=10)

b2 = Button(top, text="Least Significant",command=lambda:fun(leastsignificant)).grid(row=2,column=1,padx=10,pady=10)

b6 = Button(top, text="2nd bit",command=lambda:fun(two_bit_img)).grid(row=2,column=2,padx=20,pady=10)

b7 = Button(top, text="3rd bit",command=lambda:fun(three_bit_img)).grid(row=2,column=3,padx=20,pady=10)

b8 = Button(top, text="4th bit",command=lambda:fun(four_bit_img)).grid(row=2,column=4,padx=20,pady=10)

top.mainloop()
