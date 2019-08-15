
import MMCorePy

devlabel = "Camera"
DEVICE = [devlabel, 'DemoCamera', 'DCam']

mmc = MMCorePy.CMMCore()
mmc.loadDevice(*DEVICE)
mmc.initializeDevice(devlabel)
mmc.setCameraDevice(devlabel)

mmc.snapImage()
img = mmc.getImage()

import matplotlib.pyplot as plt
plt.imshow(img, cmap='gray')
plt.show()