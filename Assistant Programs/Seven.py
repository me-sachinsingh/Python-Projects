import RPi.GPIO as gpio
import time
import json
import pyttsx
import sys, os

try:
    import api.ai as Jarvis

except ImportError:
    sys.path.append(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
        )
    import apiai as Jarvis

#=====================================================================#
'''
        Declaring GPIO pins as input/output
'''
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
gpio.setup(3, gpio.OUT)             #Light one 
gpio.setup(5, gpio.OUT)             #Light two
gpio.setup(7, gpio.OUT)             #Cooler
gpio.setup(11, gpio.OUT)            #Fan

#=====================================================================#


CLIENT_ACCESS_TOKEN = "b7293e4e08f144e5b2a304bcca5eaa70"

class ControlService:
    def lightControl(self, response = None, toDo = None):
        _speak(response)
        if toDo == 'On':
            gpio.output(3, gpio.HIGH)

        elif toDo == 'Off':
            gpio.output(3, gpio.LOW)


def __init__():
    global ai
    global engine
        
    ai = Jarvis.ApiAI(CLIENT_ACCESS_TOKEN)
    engine = pyttsx.init()
    engine.setProperty('rate', 180)

def _speak(toSpeak):
    engine.say(toSpeak)
    engine.runAndWait()

def send_query(speech):
    request = ai.text_request()
    request.query = speech
    
    response = request.getresponse()
    Json_response = json.loads(response.read())

    result = Json_response['result']
    action = result.get('action')
     #actionIncomplete = result.get('actionIncomplete', False)

    metadata = result['metadata']
    intentName  = metadata.get('intentName')

    #entities = result['parameters']

    parameters = result['parameters']
    parameterValue = parameters.get('controlroom')
        
    fulfillment = result['fulfillment']
    Jarvis_response = fulfillment.get('speech')

    print("Jarvis >> {0} \n\taction: {1}" .format(Jarvis_response, action))
    print("\tintentName: %s" %(intentName))
    print("\tparameterValue: %s" %parameterValue)


    if(action == "control.room"):
        controlService = ControlService()
        controlService.lightControl(Jarvis_response, parameterValue)
        
    elif(action == 'jarvis.welcome'):
        _speak(Jarvis_response)


if __name__ == '__main__':
    __init__();
    speech = ""
    while True:
        try:
            speech = raw_input("You >> ")
            send_query(speech)
        except KeyboardInterrupt:
            break
    
