ffmpeg -r 30 -i %04d.png -vcodec libx264 -pix_fmt yuv420p -r 30 out.mp4