import sys
import time
import keyboard
import pyautogui
import threading
import pywinctl as pwc
from PIL import Image
import cv2
import os.path
import PySimpleGUI as sg

PATH = "./pic/screenshot.png"
f = open('./battlelog/log.txt', 'a+')
menu = "WT-Applepie-Auto (minimal version)：\n" \
       "▶Main para：\nUI Scale: 100%\n" \
       "▶Graphics：\nResolution：1270x720  Mode：Window\n" \
       "▶Naval Battle Settings：\nDefault Target：All Target  Auto targetlock：On\n" \
       "▶Controls->Naval：\n" \
       "Target Tracking：=\nManual Aim Correction: ；\nHalt：X\n" \
       "Zoom Axis: Increase Value：\\\nZoom Axis: Relative Control：On\nZoom Axis：Sensitivity：100%，Step：50%，Multiplier：2"

sg.theme('Reddit')

updateLog = [
    [sg.Text("Disclaimer：\nThis is a work of a class project,\nregarding OpenCV and image regon.\nDo not use it to farm SL.\nUse at your own risk", key="-log-")]]

layout = [[sg.Text(menu)],
          [sg.Button("Run Script"), sg.VSeperator(), sg.Button("Stop and Exit")],
          [sg.Column(layout=updateLog, size=(300, 100))]]


def click(location):
    # click a certain location on the screen
    pyautogui.moveTo(location[0], location[1])
    time.sleep(0.2)
    pyautogui.mouseDown(button='left')
    time.sleep(0.2)
    pyautogui.mouseUp(button='left')


def log(message):
    # put the log in the GUI and the text log
    print(message)
    text = window["-log-"]
    text.update(message)
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f.write("[" + curr_time + "] " + message + "\n")


def hasImage(name, threshold, message):
    # returns true if the current screenshot has the desired image
    wholeWindow = cv2.imread(PATH)
    targetImg = cv2.imread("./model/" + name + ".png")
    "start matching"
    result = cv2.matchTemplate(wholeWindow, targetImg, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > threshold:
        return True
    else:
        if message is not None:
            log(message)
        return False


def getButtonLocation(name):
    # get the button's location
    wholeWindow = cv2.imread(PATH)
    targetImg = cv2.imread("./model/" + name + ".png")
    "start matching"
    height, width, channel = targetImg.shape
    result = cv2.matchTemplate(wholeWindow, targetImg, cv2.TM_SQDIFF_NORMED)
    ul = cv2.minMaxLoc(result)[2]
    lr = (ul[0] + width, ul[1] + height)
    center = (int((ul[0] + lr[0]) / 2), int((ul[1] + lr[1]) / 2))
    return center


def escapeBuying(window):
    # if a ship is researched, escape buying via the item shop
    time.sleep(1)
    getScreen(window, PATH)
    click(getButtonLocation("researchdone"))
    time.sleep(3)
    getScreen(window, PATH)
    if hasImage("newshipreseached", 0.85, None):
        getScreen(window, PATH)
        time.sleep(1)
        click(getButtonLocation("shop"))
        time.sleep(1)
        getScreen(window, PATH)
        time.sleep(1)
        click(getButtonLocation("itemshop"))
        time.sleep(1)
        getScreen(window, PATH)
        time.sleep(1)
        click(getButtonLocation("exitout"))
        time.sleep(1)
        getScreen(window, PATH)
        time.sleep(1)
        pressWithDelay('esc', 0.1, 0.5)
        pressWithDelay('esc', 0.1, 0.5)
        pressWithDelay('esc', 0.1, 0.5)


def getScreen(window, location):
    # screenshot the current screen
    left, top = window.topleft
    right, bottom = window.bottomright
    pyautogui.screenshot(location)
    img = Image.open(location)
    img = img.crop((left + 10, top, right - 10, bottom - 10))
    img.save(location)


def pressWithDelay(c, d, t):
    # press the button c, for d seconds, and wait t seconds
    keyboard.press(c)
    time.sleep(d)
    keyboard.release(c)
    time.sleep(t)


def maneuverPattern():
    # Have the ship go forward, turn to the left, stop, then open fire
    time.sleep(15)
    keyboard.press('a')
    time.sleep(18)
    keyboard.press('x')
    time.sleep(10)
    keyboard.release('a')
    keyboard.release('x')


def attackPattern():
    # open fire at the enemy
    pressWithDelay('=', 0.1, 0.1)
    pressWithDelay('\\', 0.5, 0.1)
    pressWithDelay('=', 0.1, 0.5)
    pyautogui.mouseDown(button='left')
    time.sleep(0.4)
    pyautogui.mouseUp(button='left')
    pressWithDelay(';', 0.1, 0.1)
    pressWithDelay('=', 0.1, 1)
    pressWithDelay('=', 0.1, 1)


def saveResults(window, times):
    # Save the results after a battle is done
    log("Result Screenshot saved in log, cap at " + str(times) + ", delete if needed")
    i = 0
    while i < times:
        temppath = './battlelog/result' + str(i) + '.png'
        if not os.path.isfile(temppath):
            getScreen(window, temppath)
            break
        else:
            i = i + 1
    time.sleep(0.5)


def timeoutEscape():
    # a dumb way to escape timeouts: spam esc many times.
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)
    pressWithDelay('esc', 0.1, 0.5)


def WTScript(window):
    getScreen(window, PATH)
    windowName = window.title
    print(windowName)
    if not (windowName.__contains__("Test") or windowName.__contains__("In battle") or windowName.__contains__("Loading")):
        # We are at the hanger. Have to enter a game first
        if hasImage("naval", 0.91, "Not detecting naval battles"):
            if hasImage("enterbattle", 0.95, None):
                click(getButtonLocation("enterbattle"))
                time.sleep(5)
                getScreen(window, PATH)
                if hasImage("downloadprompt", 0.95, None):
                    # If the texture download happens to be there, close it
                    click(getButtonLocation("downloadprompt"))
                while window.title.__contains__("Waiting"):
                    time.sleep(1)
                log("Entered a match！")
    elif windowName.__contains__("Test"):
        # We are in testing mode. Under this mode it only fires to check if the attack pattern works
        attackPattern()
    elif windowName.__contains__("Loading"):
        # We are loading into one game
        time.sleep(4)
    elif windowName.__contains__("In battle"):
        # We are currently in a game
        # First sleep for a while
        time.sleep(25)
        getScreen(window, PATH)
        time.sleep(1)
        # Then, let it auto spawn to avoid being locked on
        while hasImage("spawn", 0.9, "Waiting……"):
            getScreen(window, PATH)
            time.sleep(2)
        log("Spawned")
        time.sleep(5)
        log("Turning")
        # After getting closer to the battlefield, start maneuvering
        maneuverPattern()
        log("Firing")
        i = 0
        # Lock on to the enemy and open fire
        while windowName.__contains__("In battle"):
            i = i + 1
            windowName = window.title
            attackPattern()
            getScreen(window, PATH)
            time.sleep(1)
            if i > 750:
                # Game is stuck, try to escape
                log("Game stuck")
                timeoutEscape()
                getScreen(window, PATH)
                time.sleep(1)
            if hasImage("creates", 0.92, None):
                # unlocked crates
                log("Crate, check inventory")
                getScreen(window, PATH)
                time.sleep(15)
                pressWithDelay('esc', 0.1, 0.5)
                break
            if hasImage("youdied", 0.95, None):
                # died before the game ended
                log("Died and returning to hanger")
                getScreen(window, PATH)
                time.sleep(1)
                while hasImage("youdied", 0.94, None):
                    click(getButtonLocation("youdied"))
                    getScreen(window, PATH)
                    time.sleep(1)
                time.sleep(15)
                break
            if hasImage("respawn", 0.95, None):
                # died but has enough points for a respawn
                log("Died but have enough points")
                getScreen(window, PATH)
                time.sleep(0.5)
                click(getButtonLocation("respawn"))
                time.sleep(2)
                maneuverPattern()
        # game is over
        log("Battle is over, waiting for updates")
        # wait for the points
        time.sleep(20)
        getScreen(window, PATH)
        time.sleep(0.5)
        researchDone = False
        i = 0
        while not hasImage("gotobase", 0.92, None):
            i = i + 1
            if i > 30:
                log("Game Stuck")
                timeoutEscape()
                break
            time.sleep(1)
            getScreen(window, PATH)
            time.sleep(1)
            if hasImage("researchdone", 0.91, None):
                # new ship got researched. To avoid spending all SL, we glitch the research out
                researchDone = True
                log("New ship researched")
                log("If you are buying then stop the script")
                saveResults(window, 150)
                escapeBuying(window)
                break
            if hasImage("exitout", 0.91, None):
                click(getButtonLocation("exitout"))
        if not researchDone:
            saveResults(window, 150)
            getScreen(window, PATH)
            time.sleep(1)
            log("Returning to hanger")
            click(getButtonLocation("gotobase"))
        time.sleep(5)
        getScreen(window, PATH)


def anchorWindow(window):
    # move war thunder to the top left of the screen
    window.moveTo(0, 0)
    time.sleep(0.5)


def detectWindow():
    # detect if the current window is war thunder. If not, don't input anything to avoid accidents
    while True:
        try:
            window = pwc.getActiveWindow()
            if window is None:
                continue
            windowName = window.title
            if windowName.__contains__("War Thunder"):
                "Currently in War Thunder"
                anchorWindow(window)
                WTScript(window)
                time.sleep(0.5)
            else:
                "Currently not in War Thunder"
                log("War Thunder Not Detected")
                time.sleep(3)

        except KeyboardInterrupt:
            break


def startScript():
    # start the whole script
    detectWindow()


if __name__ == '__main__':
    isRunning = False
    window = sg.Window(title="WT-APA", layout=layout)
    app = threading.Thread(target=startScript, daemon=True)
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Stop and Exit" or event == sg.WIN_CLOSED:
            f.close()
            sys.exit()
        if event == "Run Script" and not isRunning:
            isRunning = True
            log("Started script")
            app.start()
