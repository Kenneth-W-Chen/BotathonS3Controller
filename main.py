import pygame
pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True


inputPackage = []

#set all axes "initial" value to -10 so that input is sent if they start at 1 from the start of the program
#idk actually, just a safety net
axisValues = [-10.0,
              -10.0,
              -10.0,
              -10.0,
              -10.0,
              -10.0]
#was making this for button backlog stuff
#waitingToSendInput = []

for i in range(0, pygame.joystick.get_count()):
    # create a Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    # print a statement telling what the name of the controller is
    #print ("Detected joystick "),joysticks[-1].get_name(),"'"
while keepPlaying:
    clock.tick(50)
    for event in pygame.event.get():
        print(event)
        #if the event is for an axis input
        if event.type==1536:
            newAxisValue = event.__dict__['value']
            axisNum = event.__dict__['axis']
            if newAxisValue < .01:
                newAxisValue = 0
            #only send the value if it changed by more than 0.01 since the last update
            if abs(newAxisValue-axisValues[axisNum-1])>.01:
                toAdd = True
                for i in range(len(inputPackage)):
                    if inputPackage[i][0]=='a' and inputPackage[i][1]==axisNum:
                        axisValues[axisNum] = newAxisValue
                        inputPackage[i]= ('a', axisNum, newAxisValue)
                        toAdd = False
                        break
                if toAdd:
                    axisValues[axisNum] = newAxisValue
                    inputPackage.append(('a', axisNum, newAxisValue))
        # if the event is for a button
        elif event.type==1539 or event.type==1540:
            #Adds a tuple containing what button was pressed and if the button is pressed down (true if it is)
            inputPackage.append(('b',event.__dict__['button'],event.type==1539))
        #d-pad is rarely used, so we can make it the last else
        #there should be no other inputs besides this
        elif event.type==1538:
            inputPackage.append(('d',event.__dict__['value']))
    if inputPackage:
        print(inputPackage)
        #send inputPackage
        inputPackage.clear()
        #print(inputPackage)


#List of event types (as far as I'm aware, this numbering is constant)
#Axes input:    1536
#Button Down:   1539
#Button Up:     1540
#D-Pad:         1538
#there's also the gamepad being connected and mic/headphones (but no one cares about that)

#list of buttons/axes and their corresponding xbox input:
#NOTE: D-Pad comes with a value in an ordered pair representing x,y
#Axes 1,0:  Left joystick, x,y
#Axes 3,2:  Right joystick, x,y
#Axis 4:    Left Trigger, positive is pushed in
#Axis 5:    Right Trigger, same as Axis 4 (Left Trigger)
#Button 0:  A Button
#Button 1:  B Button
#Button 2:  X Button
#Button 3:  Y Button
#Button 4:  Left Bumper
#Button 5:  Right Bumper

#The three center buttons (excluding the xbox)
#Button 6:  Left center Button
#Button 7:  Right Center Button
#Button 11: Center Center Button

#Button 8:  Left Joystick Button
#Button 9:  Right Joystick Button
#Button 10: XBox Button
