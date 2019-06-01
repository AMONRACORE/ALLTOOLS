import os, sys

print ("\033[1;32mPLEASE INPUT USERNAME AND PASSWORD")

print ("\033[1;32mFOR FULL ACCESS..!!")

username = 'AMONRA'      

password = '666'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("USERNAME : ")

	if uname == username:

		pwd = raw_input("PASSWORD : ")



		if pwd == password:

			print "\033[1;32mLOADING,..!!", 

			sys.exit()



		else:

			print "\033[1;32mWRONG PASSWORD..!! [?]\033[00m"

			print "PLEASE LOGIN AGAIN..!!\n"

			restart()



	else:

		print "\033[1;32mSORRY..!! USERNAME FAILED..!! [?]\033[00m"

		print "PLEASE LOGIN AGAIN..!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
