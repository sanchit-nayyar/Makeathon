import os, datetime
fname = str(datetime.datetime.now()).replace(' ', '\\ ') + '.avi'
os.chdir('/home/sanchit/Videos/ffmpeg-capture')
os.system('ffmpeg -f x11grab -y -r 30 -s 1280x720 -i :1.0 -vcodec huffyuv ' + fname)