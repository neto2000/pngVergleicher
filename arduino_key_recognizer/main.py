import start_ahk_file as start_ahk
import threading as th
import serial

current_state = 0

class exe_ahk(th.Thread):
    global current_state

    def ini(self, stop):

        while True:

            if current_state == 0:
                print("nothing")

            else:
                start_ahk.start("ahk_scripts\\ahk_script" + str(current_state) + ".ahk")

            if stop():

                print("end")
                break



class Serial_Signal(th.Thread):

	def test(self, stop):
		global current_state

		while True:
			self.lol = 1
			

			
			current_state = self.lol

			if stop():
				print("end")
				break




	

	def get_state(self, stop):
		global current_state

		self.arduino = serial.Serial('COM3', 9600, timeout=0.5)

		while True:

			
			

			self.output = self.arduino.readline()

			print(self.output)

			self.out_raw_str = self.output.decode()

			

			self.out_normal_str = self.out_raw_str.strip()

			print(self.out_normal_str)

			try:

				self.button_state = int(self.out_normal_str)

			except:
				print("failed")

				self.button_state = 0


			current_state = self.button_state
			
			
			if stop():
				print("end")
				break

			

	
		self.arduino.close()


if __name__ == '__main__':

	



	app1 = exe_ahk()
	app2 = Serial_Signal()

	stop_threads = False

	t1 = th.Thread(target=app1.ini, args=(lambda : stop_threads,))
	t2 = th.Thread(target=app2.get_state, args=(lambda : stop_threads,))

	t1.start()
	t2.start()

	def end():
		global stop_threads

		stop_threads = True

		print("destroy")

		