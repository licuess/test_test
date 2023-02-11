import atexit
import time
from itertools import product


def range_func():
	list1 = range(1, 3)
	list2 = range(4, 6)
	list3 = range(7, 9)

	for item1, item2, item3 in product(list1, list2, list3):
		print(item1 + item2 + item3)


@atexit.register
def clean():
	"""注册程序结束后运行函数clean"""
	print("清理任务")


@atexit.register
def world():
	print(time.time())
	print("world")


def main():
	clean()
	world()
	print("hello world!")
	range_func()


if __name__ == "__main__":
	main()
