#!/urs/bin/env python3

import os

def parse_mounts():
	"""
	分析 /proc/mounts 并返回元组的列表
	"""
	result = []
	if os.path.exists("/proc/mounts"):
		fd = open("/proc/mounts")
		for line in fd:
			line = line.strip()	# 去除左右边的空格
			words = line.split()	# 对字符串进行分割，默认空格分割
			if len(words) > 5:
				# 4个元组元素
				res = (words[0], words[1], words[2], '({})'.format(' '.join(words[3:-2])))
			else:
				res = (words[0], words, words[2])
			result.append(res)
		fd.close()
	return	result

def mount_details():
	"""
	打印挂在详情信息
	"""
	result = parse_mounts()
	for line in result:
		if len(line) == 4:
			print('{} on {} type {} {}'.format(*line))	# * 对元组拆封
		else:
			print('{} on {} type {}'.format(*line))

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

