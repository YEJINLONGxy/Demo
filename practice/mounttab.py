#!/urs/bin/env python3

import os

def mount_details():
	"""
	打印挂载详细信息
	"""

	if os.path.exists("/proc/mounts"):
		#with open("/proc/mounts") as fd:
		#	fd = read(fd)  	#不能这样读取数据，否则 for 循环时会每个字母字符单个循环打印
		
		fd = open("/proc/mounts")
		for line in fd:
			line = line.strip()	# 去除左右边的空格
			words = line.split()	# 对字符串进行分割，默认空格分割
			print('{} on {} type {}'.format(words[0], words[1], words[2]))
			if len(words) > 5:
				print('()'.format(' '.join(words[3:-2])))
			else:
				print()
		fd.close()

if __name__ == "__main__":
	mount_details()

#+++++++++++++++++++++++++++++++++
# 
#>>> path
#'/proc/mounts'
#>>> fd = open(path)
#>>> fd			#返回的是一个对象
#<_io.TextIOWrapper name='/proc/mounts' mode='r' encoding='UTF-8'>
#>>> fd.close()

#案例中打开文件方式
#>>> path = "/proc/mounts"
#>>> with open(path) as fd:
#	fd = fd.read()
#>>> fd 
#'rootfs / rootfs rw 0 0\nsysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0\nproc /proc proc rw,nosuid,nodev,noexec,relatime 0 0\ndevtmpfs /dev devtmpfs rw,nosuid,size=1919512k,nr_inodes=479878,mode=755 0 0\nsecurityfs /sys/kernel/security securityfs rw,nosuid,nodev,noexec,relatime 0 0\ntmpfs /dev/shm tmpfs rw,nosuid,nodev 0 0\ndevpts /dev/pts devpts rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000 0 0\ntmpfs /run tmpfs rw,nosuid,nodev,mode=755 0 0\ntmpfs /sys/fs/cgroup tmpfs ro,nosuid,nodev,noexec,mode=755 0 0\n'

#>>>for line in fd:
#...	print(line) 
#r
#o
#o		#打印出的是单个字符，不符处理方式，所有不能用
######## or ###################
#使用 with 结合 for 一起用
#>>> with open(path) as fd:
#...     for line in fd:
#...             line = line.strip()
#...             print(line)
#...             words = line.split()
#...             print(words)

