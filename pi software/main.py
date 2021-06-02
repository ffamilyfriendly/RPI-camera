import cv2;
import threading;
from datetime import datetime;
import configparser;

config = configparser.ConfigParser();
config.read("conf.ini");
xstarts, xends, ystarts, yends = int(config["sample"]["xstart"]), int(config["sample"]["xend"]), int(config["sample"]["ystart"]), int(config["sample"]["yend"])
cap = cv2.VideoCapture(0);

# Avg r, g, b for pixels in area
class avg:
    r = []
    g = []
    b = []
    R = 0
    G = 0
    B = 0

def Avg(lst):
    return sum(lst) / len(lst)
    
def sample(frame):
        class avgFrame:
            r = []
            g = []
            b = []

        for x in range(xstarts,xends):
            for y in range(ystarts, yends):
                cf = frame[y,x]
                avgFrame.b.append(cf[0])
                avgFrame.g.append(cf[1])
                avgFrame.r.append(cf[2])
        return Avg(avgFrame.r), Avg(avgFrame.g), Avg(avgFrame.b)

def doFrame(frame):
    for x in range(xstarts,xends):
        frame[ystarts,x] = [0,0,255]
        frame[yends,x] = [0,0,255]
    for y in range(ystarts, yends):
        frame[y,xstarts] = [0,0,255]
        frame[y,xends] = [0,0,255]
    return frame

def run():
    thresh = int(config["sample"]["threshold"])
    def wThresh(fV,lV):
        return abs(fV - lV) < thresh

    threading.Timer(int(config["general"]["checkevery"]),run).start();
    ret, frame = cap.read()
    lR, lG, lB = sample(frame)

    if(wThresh(lR,avg.R) and wThresh(lG,avg.G) and wThresh(lB,avg.B)): exit()
    cv2.imwrite("./images/{}.png".format(datetime.now().strftime("%d-%m-%Y-%H;%M;%S")),doFrame(frame));

def runSample():
    print("Sampling x{}-{},y{}-{} for {} seconds".format(config["sample"]["xstart"],config["sample"]["xend"],config["sample"]["ystart"],config["sample"]["yend"],config["sample"]["seconds"]))
    
    class timesran:
        i = 0
        cont = True

    def getValues():
        if(timesran.i < int(config["sample"]["seconds"])): threading.Timer(1.0,getValues).start();
        else:
            if(not timesran.cont): exit(1)
            print("Done sampling!")
            avg.R = Avg(avg.r)
            avg.G = Avg(avg.g)
            avg.B = Avg(avg.b)
            print("Sampling concluded in average RGB of {},{},{}".format(round(avg.R),round(avg.G),round(avg.B)))
            run();
        ret, frame = cap.read()
        rows, cols, channels = frame.shape
        timesran.i += 1;
        if(cols < xends or rows < yends): 
            print("Pal, that is too big. Max x{} y{}".format(cols, rows))
            timesran.cont = False
            timesran.i = 6000
            exit()
            
        lR, lG, lB = sample(frame)

        avg.r.append(lR)
        avg.g.append(lG)
        avg.b.append(lB)

    getValues();

print("starting sampling in {} seconds".format(config["general"]["arm"]))
threading.Timer(int(config["general"]["arm"]),runSample).start()