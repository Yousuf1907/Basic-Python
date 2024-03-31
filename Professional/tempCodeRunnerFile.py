player = pyglet.media.Player()
source = pyglet.media.load("D:\Yousuf's OneDrive\OneDrive\Pictures\Camera Roll\WIN_20221025_15_13_39_Pro.mp4")
player.queue(source)
player.play()

pyglet.app.run()