
"""def checkCollision(obj1, obj2):
    if obj1.hitbox.colliderect(obj2):
        return(True)
    else:
        return(False)"""
    
def checkCollisionX(obj1, obj2):

    #obj1.onGround = False
    #obj2.onGround = False

    if not(obj1.hitbox.colliderect(obj2.hitbox)):



        if obj2.layer > 1:
            obj2.onGround = False        
        if obj1.layer > 1:
            obj1.onGround = False
        

    else:

        if obj1.hitbox.y < obj2.hitbox.y:
            #print("obj1 above obj2")
            if obj1.layer > obj2.layer:
                obj1.hitbox.y = obj2.hitbox.y - obj1.hitbox.height
                obj1.onGround = True
                #obj1.groundCounter +=1

            elif obj1.layer < obj2.layer:
                obj2.hitbox.y = obj1.hitbox.y + obj1.hitbox.height
                obj1.onGround = False
        
        elif obj1.hitbox.y > obj2.hitbox.y:
            #print("obj1 below obj2")
            if obj1.layer > obj2.layer:
                obj1.hitbox.y = obj2.hitbox.y + obj2.hitbox.height
                obj2.onGround = False

            elif obj1.layer < obj2.layer:
                obj2.hitbox.y = obj1.hitbox.y - obj2.hitbox.height
                obj2.onGround = True
                #obj2.groundCounter +=1

                

def checkCollisionY(obj1, obj2):
    if obj1.hitbox.colliderect(obj2.hitbox):

        if (obj1.hitbox.x+0.5*obj1.hitbox.width) < obj2.hitbox.x:
            #print("obj1 left from obj2")

        
       
            if obj1.layer > obj2.layer:
                if (obj1.hitbox.y+0.6*obj1.hitbox.height) > obj2.hitbox.y:  
                    obj1.hitbox.x = obj2.hitbox.x - obj1.hitbox.width

            elif obj1.layer < obj2.layer:
                if (obj2.hitbox.y+0.6*obj2.hitbox.height) > obj1.hitbox.y:  
                    obj2.hitbox.x = obj1.hitbox.x + obj2.hitbox.width
                

        elif (obj1.hitbox.x+0.5*obj1.hitbox.width) > (obj2.hitbox.x+obj2.hitbox.width):
            #print("obj1 right from obj2")

        

            if obj1.layer > obj2.layer:
                if (obj1.hitbox.y+0.6*obj1.hitbox.height) > obj2.hitbox.y:
                    obj1.hitbox.x = obj2.hitbox.x + obj2.hitbox.width
            elif obj1.layer < obj2.layer:
                if (obj2.hitbox.y+0.6*obj2.hitbox.height) > obj1.hitbox.y:
                    obj2.hitbox.x = obj1.hitbox.x - obj2.hitbox.width
        
        


"""def Jump(obj):
    if obj.jump == 1:
        obj.direction[1] = 20
        obj.jump == 0
    
    if obj.jump == 2:
        obj.direction[1] = 10
        obj.jump == 1

    if obj.jump == 3:
        obj.direction[1] = 0
        obj.jump == 2
        
    if obj.jump == 4:
        obj.direction[1] = -10
        obj.jump == 3

    if obj.jump == 5:
        obj.direction[1] = -20
        obj.jump == 4"""


def checkEnemyCollision(obj1, obj2, start):

    if obj1.hitbox.colliderect(obj2.hitbox):
        obj1.hitbox.x = start[0]
        obj1.hitbox.y = start[1]
        return(True)



    
    
