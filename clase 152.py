from tkinter import*
root=Tk()
root.title("Matrices multidimencionales")

root.geometry("5000x500")
label= Label(root)


array_1d = ["Coro","Leo","Peña"]
print( array_1d[0] )

array_2d = [["Coro","A"],["Leo","B"],["Peña","C"]]
print( array_2d[0][1] )

array_3d = [[["Coro","A","muy bien"],["Leo","B","bien"],["Peña","A+","exelente"]]]
print( array_3d[0][0][2] )

def report():
    label["text"] = array_3d[0][1][0] + "obtubo la calificacion de " + array_3d[0][1][1] +", te fue "+ array_3d[0][1][2]

btn = Button(root, text= "mostrar reporte", command = report)
btn.place(relx= 0.5, rely =0.5, anchor = CENTER)

label.place(relx = 0.5,rely =0.6,anchor=CENTER)

root.mainloop()