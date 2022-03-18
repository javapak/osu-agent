from slider import Beatmap as slider  # this library has the ability to parse both osr and osu files, but i liked the other one more for osr files..

class processedosu:
    def __init__(self, xytimetype):
        self.xytimetype = xytimetype
    

xytimetype = []
object2int = 0

def parseosu(f):
    beatmap = slider.from_path(f)
    
    hitobjects = beatmap.hit_objects()
    string = []

    for hitobject in hitobjects:
        string = str(hitobject)
        string = string.split(",",2)
        string = string[2].replace("ms>","") #time was formatted in standard minute convention, would rather have milliseconds directly. 
        integer = int(string)
        if (type(hitobject).__name__ == "Slider"):
            object2int = 2
        elif (type(hitobject).__name__ == "Circle"):
            object2int = 0
        elif (type(hitobject).__name__ == "Spinner"):
            object2int = 1
        
        xytimetype.append([hitobject.position[0], hitobject.position[1], integer, object2int])
    
    return processedosu(xytimetype)
        
    
    
    
    
    
    
  