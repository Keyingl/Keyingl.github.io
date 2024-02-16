import os
from MyQR import myqr
version, level, qr_name = myqr.run(
	'https://Keyingl.github.io/Vday',
	# 'https://Keyingl.github.io/Vday/',
    version=1,
    level='H',
    picture='Icon.jpeg',
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name='ip_hliu.png',
    save_dir=os.getcwd()
)
print('version',version)
print('level',level)
print('qr_name',qr_name)
# os.system('pause')