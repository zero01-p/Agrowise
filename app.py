import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'garlic need crop rotation' in command:
        talk('Garlic does not need crop rotation. This is because it is possible to grow garlic in the same field for several years in a row. Crop rotation is when the plants that are grown in a field are changed from time to time. Although it is not a necessity it is beneficial because it can reduce the damage which is done by soil bound pests and it can help balance the nutrient content of soil')
    elif 'What is soil health' in command:
        talk('Sometimes referred to as soil quality, soil health is the continued ability of soil to act as an ecosystem for plants, animals, and humans. The term “soil health” is used to remind farmers that the soil contains living organisms that help us produce food')
    elif 'What impact does farming have on soil health' in command:
        talk('Adding nutrients, Soil Loss, Overgrazing')
    elif 'What are types pesticides' in command:
        talk('Insecticides used to repel insects. Herbicides, used to repel weeds and other harmful plants. Rodenticides, used to repel rodents. Bactericides, used to repel various types of harmful bacteria. Fungicides, used to repel various types of fungi. Larvicides, used to repel various types of larvae.')
    elif 'What factors affect crop production' in command:
        talk('Nutrients, Water Availability, Climate, Pests and diseases')
    elif 'What is indoor farming' in command:
        talk('Indoor farming is the practice and process of growing crops and produce in vertically stacked layers. These layers use a controlled-environment agriculture, which optimizes plant growth by using soilless farming techniques')
    elif 'What crops can be grown indoors' in command:
        talk('The great thing about indoor farming is that seasonal crops can be grown during any time and in any climate. Crops like strawberries, peppers, herbs, leafy greens, microgreens, and more can be grown indoors')
    elif 'What is a greenhouse' in command:
        talk('A greenhouse is a building with glass walls and ceiling/roof that are used to grow plants. Greenhouses are able to stay warm inside using sunlight to warm both the plants and the air within. Sunlight is also used for photosynthesis, though supplemental artificial lighting can also be used')
    elif 'What are the benefits of a greenhouse' in command:
        talk('Benefits of a greenhouse include having fresh greens, vegetables, and fruit; a longer growing season; protection from pest and insects; and the ability to grow items that aren’t available using traditional means or during off seasons')
    elif 'What are the disadvantages of a greenhouse' in command:
        talk('Some disadvantages of a greenhouse include choosing a proper location that will be able to capture the sunlight during all seasons and temperature and ventilation management, so crops don’t die, trapping pests or diseases within')
    elif 'What is transplanting' in command:
        talk('Transplanting is taking a rooted crop and replanting it elsewhere. Transplanting is common practice for transferring baby plants from their optimal sprouting conditions, a nursery for example, to another location, like outdoors')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()