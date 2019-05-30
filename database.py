import imports

models = {
        'maps' : [],        #{
                            #'filename' : "",
                            #}
        'objects' : [],
        'actors' : []       #{
                            #'filename_body' : "path",
                            #'animations' : {'name' : "path"},
                            #'filename_head' : "path",
                            #'headname' : ""
                            #'filename_texture_torso' : "path",
                            #'filename_texture_arm' : "path",
                            #'filename_texture_leg' : "path",
                            #'position' : [],
                            #}
        }

#Convenience
maps = models['maps']
objects = models['objects']
actors = models['actors']    
    
def moveActor(act, pos): # X=None, Y=None, Z=None):
#    if X: act.setX(X)
#    if Y: act.setY(Y)
#    if Z: act.setZ(Z)
    if pos[0]: act.setX(pos[0])
    if pos[1]: act.setY(pos[1])
    if pos[2]: act.setZ(pos[2])


def createActor(act):
    #Reading info before act is overwritten
    head = loader.loadModel(act['filename_head']).find("**/"+i['headname'])
    TorsoTexture = loader.loadTexture(act['filename_texture_torso'])
    ArmTexture = loader.loadTexture(act['filename_texture_arm'])
    LegTexture = loader.loadTexture(act['filename_texture_leg'])
    pos = act['position']
      
    #Construct the model
    act = Actor(act['filename_body'],act['animations']) #Main actor instance
    
    head.reparentTo(act.find("**/joint_head")) #Recapitation
    
    act.find("**/torso").setTexture(TorsoTexture, 1) #Body texturing
    
    act.find("**/arms").setTexture(ArmTexture, 1) #Arm texturing
    
    act.find("**/legs").setTexture(LegTexture, 1) #Leg texturing
    
    act.reparentTo(render)
    
    #Positioning
    moveActor(act, pos)


def initialise(typ, Id):
    i = models[typ][Id]
    
    if typ == 'actors': createActor(i)        
    elif typ == 'maps': 
        i = loader.loadModel(i['filename'])
        i.reparentTo(render)