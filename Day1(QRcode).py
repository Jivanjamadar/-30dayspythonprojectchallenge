
import qrcode
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.animation as animation

data = "https://www.linkedin.com/in/jivan-jamdar/"
qr = qrcode.QRCode(
    version=1,
    box_size=15,
    border=6,
)
qr.add_data(data)
qr.make(fit=True)
qr_image = qr.make_image(fill_color="black", back_color="white")

qr_array = np.array(qr_image)

fig, ax = plot.subplots()
img = ax.imshow(qr_array, cmap='gray')

def animate(i):
    color = np.random.rand(4,)
    color_int = tuple(int(c * 255) for c in color.flatten())
    qr_img = qr.make_image(fill_color=color_int, back_color="white")
    qr_array = np.array(qr_img)
    img.set_array(qr_array)
    return [img]

ani = animation.FuncAnimation( fig,animate, frames=100, interval=200, blit=True) 
plot.show()
 