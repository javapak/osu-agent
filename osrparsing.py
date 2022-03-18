from circleparse import replay # library for parsing osu! replays, which are formatted and stored in .osr files.


class processedReplay:
    def __init__(self, xytimetimedeltakeys):
     self.xytimetimedeltakeys = xytimetimedeltakeys
        
        

def modcheck(f):
    check = False # in this instance the presence of mods throws a false flag, backwards logic...
    rp = replay.parse_replay_file(f)
    if (rp.mod_combination == 0):
        check = True # set check to true if there are no mods present in the replay, can't support mods at this time as it changes position of hit objects.
    return check
        

def parseosr(f):
    rp = replay.parse_replay_file(f)
    data = rp.play_data
    offset = 0
    xytimetimedeltakeys = []
    
    
    
    
    # an event can also be referred to as a replay frame for more context. it holds the game states for a given frame (time in miliseconds to be more precise).
    for event in data:
        
        offset += event.time_since_previous_action
        xytimetimedeltakeys.append([event.x, event.y, offset, event.time_since_previous_action, event.keys_pressed])
        
    
    return processedReplay(xytimetimedeltakeys)
        




        
        


    
    
    
    
    
    


