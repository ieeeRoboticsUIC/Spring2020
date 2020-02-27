import serial
import pygame
 
class Controller:
    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        self.hatcount = self.joystick.get_numhats()
        self.axescount = self.joystick.get_numaxes()
        self.buttcount = self.joystick.get_numbuttons()
#end controller class

serxb = serial.Serial('/dev/ttyUSB0', 9600)
test = Controller()
serxb.close()
serxb.open()

print(test.hatcount)
print(test.axescount)
print(test.buttcount)


ly = test.joystick.get_axis(1)

ry = test.joystick.get_axis(5)

print('ly: {}'.format(ly))
print('ry: {}'.format(ry))

hatlist = [0,0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            if abs(ly - test.joystick.get_axis(1)) > 0.05:
                ly = test.joystick.get_axis(1)
                print('left Y is ', test.joystick.get_axis(1), end = '')
                if ly <= -0.25:
                    serxb.write("2".encode())
                    print(', Up')
                elif ly >= 0.25:
                    serxb.write("3".encode())
                    print(', Down')
                else:
                    print('')
            if abs(ry - test.joystick.get_axis(5)) > 0.05:
                ry = test.joystick.get_axis(5)      #if the change in the axis is great enough ry becomes the Y axis of the right joystick
                print('Right Y is ', test.joystick.get_axis(5), end = '')    #testing purposes
                if ry <= -0.25:
                    serxb.write("0".encode())
                    print(', Up')
                elif ry >= 0.25:
                    serxb.write("1".encode())
                    print(', Down')
                else:
                    print('')
               
        if event.type == pygame.JOYBUTTONDOWN:
            if test.joystick.get_button(0):
                print("Square has been activated")
            if test.joystick.get_button(1): #Activate the Sorter
                print("X has been activated")
                serxb.write("S".encode())
            if test.joystick.get_button(2): #Potion Release
                print("o has been activated")
                serxb.write("P".encode())
            if test.joystick.get_button(3):
                print("Triangle has been activated")
            if test.joystick.get_button(4):
                print("L1 has been activated")
            if test.joystick.get_button(5):
                print("R1 has been activated")
            if test.joystick.get_button(6): #Shooter Speed 2
                print("L2 has been activated")
                serxb.write("5".encode())
            if test.joystick.get_button(7): #Shooter Speed 1
                print("R2 has been activated")
                serxb.write("4".encode())
            if test.joystick.get_button(8):
                print("Share has been activated")
            if test.joystick.get_button(9):
                print("Options has been activated")

        if event.type == pygame.JOYHATMOTION:
            hatlist = test.joystick.get_hat(0)
            if(hatlist[0] == 1):
                serxb.write("R".encode())
                print("right")
            if(hatlist[0] == -1):
                serxb.write("L".encode())
                print("left")
            if(hatlist[0] == 0):
                serxb.write("X".encode())
                print("null x-axis")
            if(hatlist[1] == 1):
                serxb.write("U".encode())
                print("up")
            if(hatlist[1] == -1):
                serxb.write("D".encode())
                print("down")
            if(hatlist[1] == 0):
                serxb.write("Y".encode())
                print("null y-axis")
                
                
