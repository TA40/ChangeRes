import win32api
import win32con
import pywintypes
import argparse

parser = argparse.ArgumentParser(description='Resolution Changer')
parser.add_argument("-x", help="Input Width")
parser.add_argument("-y", help="Input Height")
args = parser.parse_args()


if args.x is None ot args.y is None:
	print("x and/or y is empty. You can input it now or launch the .exe with -x and -y parameters.\n")
	print("Example: 1680x1050")
	xy=input("Input the full resolution (widthXheight) like in the example: ")

	try:
		xySplitted = xy.lower().split("x")
		x = int(xySplitted[0])
		y = int(xySplitted[1])
	except:
		raise
else:
	x = int(args.x)
	y = int(args.y)

devmode = pywintypes.DEVMODEType()

devmode.PelsWidth = x
devmode.PelsHeight = y

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)