import random
#import time
import pygame
pygame.init()
win=pygame.display.set_mode((560,560))
pygame.display.set_caption('Checkers')
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
bg = pygame.image.load('capture.png').convert()
pcgot= pygame.image.load('pcgoti.png')
usergot= pygame.image.load('usrgoti.png')
pcwins = pygame.image.load('computer wins.png')
userwins = pygame.image.load('user wins.png')
draw = pygame.image.load('draw.png')
pcghora = pygame.image.load('pcghora.png')
userghora = pygame.image.load('usrghora.png')


w=69


clock=pygame.time.Clock()
#x=450 
#y=450

f=255 #color
o=0 #color
b=255 #color
r=255 #color
e=0 #color
t=255 #color

j=80 #width of square


gameExit = False



def comp_move(grid):
    gotis =[]
    ghoraa=[]
    moves = []
    
    #moves = [currentx, currenty, updatedx, updatedy, score , kind of piece]

    
    for x in range(8):
        for y in range(8):
            if grid[x][y] == 1:
                gotis.append([x,y])
            if grid[x][y] == 6:
                ghoraa.append([x,y])
    print(gotis)
    for z in gotis:
        try:
            if grid[z[0]+1][z[1]+1] == 2:
                if grid[z[0]+2][z[1]+2] == 3:
                    moves.append([z[0],z[1], z[0]+2, z[1]+2, 1,1])
                    
        except:
            pass
    
        try:
            if grid[z[0]+1][z[1]-1] == 2:
                if grid[z[0]+2][z[1]-2] == 3:
                    moves.append([z[0],z[1], z[0]+2, z[1]-2, 1,1])
                    print('afueaheqwoefhioqwefio')
        except:
            print('bhaiya')
            

        try:
            if grid[z[0]+1][z[1]-1] == 3 and z[0]!=0 and z[1]!=0:
                moves.append([z[0],z[1], z[0]+1, z[1]-1, 0,1])
                print('pehla')
        except:
            print("passed")
            pass

        try:
            if grid[z[0]+1][z[1]+1] == 3:
                moves.append([z[0],z[1], z[0]+1, z[1]+1, 0,1])
                print('doosra')
        except:
            pass




        
    for z in ghoraa:
        try:
            if grid[z[0]+1][z[1]+1] == 2 or grid[z[0]+1][z[1]+1] == 4:
                if grid[z[0]+2][z[1]+2] == 3:
                    moves.append([z[0],z[1], z[0]+2, z[1]+2, 1,6])
                    
        except:
            pass

        try:
            if grid[z[0]-1][z[1]+1] == 2 or grid[z[0]-1][z[1]+1] ==4 :
                if grid[z[0]-2][z[1]+2] == 3:
                    moves.append([z[0],z[1], z[0]-2, z[1]+2, 1,6])
                    
        except:
            pass







        
        try:
            if grid[z[0]+1][z[1]-1] == 2 or grid[z[0]+1][z[1]-1] == 4:
                if grid[z[0]+2][z[1]-2] == 3:
                    moves.append([z[0],z[1], z[0]+2, z[1]-2, 1,6])
                    print('afueaheqwoefhioqwefio')
        except:
            print('bhaiya')
            
        try:
            if grid[z[0]-1][z[1]-1] == 2 or grid[z[0]-1][z[1]-1] == 4:
                if grid[z[0]-2][z[1]-2] == 3:
                    moves.append([z[0],z[1], z[0]-2, z[1]-2, 1,6])
                    print('afueaheqwoefhioqwefio')
        except:
            print('bhaiya')











        try:
            if grid[z[0]+1][z[1]-1] == 3 and z[0]!=0 and z[1]!=0:
                moves.append([z[0],z[1], z[0]+1, z[1]-1, 0, 6])
                print('pehla')
        except:
            print("passed")
            pass

        try:
            if grid[z[0]-1][z[1]-1] == 3 and z[0]!=0 and z[1]!=0:
                moves.append([z[0],z[1], z[0]-1, z[1]-1, 0,6 ])
                print('pehla')
        except:
            print("passed")
            pass

        try:
            if grid[z[0]+1][z[1]+1] == 3:
                moves.append([z[0],z[1], z[0]+1, z[1]+1, 0,6])
                print('doosra')
        except:
            pass


        try:
            if grid[z[0]-1][z[1]+1] == 3:
                moves.append([z[0],z[1], z[0]-1, z[1]+1, 0,6])
                print('doosra')
        except:
            pass





        
    
    moves.sort(key=lambda x:x[4])
    
    moves = moves[::-1]
    indexes= []
    new_moves=[]

    #agar koi negative index ajayega to usko eliminate karega
    
    for i in range(len(moves)):
        flag = False 
        for j in moves[i]:
            if j <0:
                flag= True
        if flag== False:
            indexes.append(i)
    for x in indexes:
        new_moves.append(moves[x])
        
    # Moves list can contain negative index but new_moves list cannot
    
    print(moves)
    print(new_moves)
    #if new_moves[0][4]==
    try:
        if new_moves[0][4]==0:
            print('adddd')
            random.shuffle(new_moves)
            print(new_moves)
            print('a')
            taken_move = new_moves[0]
            return taken_move
        
        if new_moves[0][4]==1:
            taken_move = new_moves[0]
            return taken_move
    except:
        if len(gotis) + len(ghoraa)>0 and len(new_moves)==0:
            print('drawwwwww')
            while True:
                win.blit(draw,(0,0))
                #pygame.display.update()
        if len(gotis) + len(ghoraa)==0 and len(new_moves)==0:
            print('user wonnnnnnnn')
            while True:
                win.blit(userwins,(0,0))
                #pygame.display.update()

def win_or_lose(grid):
    flagpc= True
    flaguser= True
    for i in range(8):
        for j in range(8):
            if grid[i][j]==1 or grid[i][j]==6:
                flagpc=False
            if grid[i][j]==2 or grid[i][j]==4:    #2 goti of user
                flaguser=False
    if flagpc==True:
        print("user wins")
        while True:
            win.blit(userwins,(0,0))
    #        pygame.display.update()
        
        
    if flaguser==True:
        print("pc wins")
        while True:
            win.blit(pcwins,(0,0))
     #       pygame.display.update()
        
    

def show(grid):
    for i in range(8):
        for j in range(8):
            if grid[i][j]== 1: #1=pc piece
                a= i*69
                b= j*69
                win.blit(pcgot,(b,a))
                #pygame.display.update()
            elif grid[i][j]== 2:
                a= i*69
                b= j*69
                win.blit(usergot,(b,a))
                #pygame.display.update()
            elif grid[i][j]== 4:
                a= i*69
                b= j*69
                win.blit(userghora,(b,a))
                #pygame.display.update()
            elif grid[i][j]== 6:
                a= i*69
                b= j*69
                win.blit(pcghora,(b,a))
                #pygame.display.update()
    




grid= [ [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
x,y=0,0
win.fill((r,r,r))
##    pygame.display.update()
##for row in grid:
##    for col in row:
##        pygame.draw.rect(win,(e,r,t),[x,y,w,w])
##        x=x+w
##    y=y+w
##    x=0
##    pygame.display.update()



def firstplayers(grid): #pc pieces
    for j in range(1,8,2):
        grid[0][j]=1
    for j in range(0,7,2):
        grid[1][j]=1 
    return grid


def secondplayer(grid): #user piece
    for j in range(1,8,2):
        grid[6][j]=2
    for j in range(0,7,2):
        grid[7][j]=2
    return grid


def otheroptions(grid): #jahan chal skte hain
    a=[2,4]
    for i in a:
        for j in range(1,8,2):
            grid[i][j]=3
    
    b=[3,5]
    for i in b:
        for j in range(0,7,2):
            grid[i][j]=3
    return grid


def cannotmove(grid): #jahan nhy chalskte
    for i in range(8):
        for j in range(8):
            if grid[i][j]== 0:
                grid[i][j]=5
    return grid


grid=firstplayers(grid)
#print(grid)
grid=secondplayer(grid)
#print(grid)
grid=otheroptions(grid)
#print(grid)
grid=cannotmove(grid)
#print(grid)



def display():
    win.blit(bg,(0,0))
    show(grid)
    #pygame.display.update()


a=False 
count = []


while not gameExit:
    clock.tick(1)
    keys=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            gameExit ==True
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            count.append(1)
            pos_y , pos_x = pygame.mouse.get_pos()
            x1=pos_x//w
            y1=pos_y//w
            print(x1,y1)
            print(grid[x1][y1])
            a=False
            #print('bahar')
            while a==False:
                if grid[x1][y1]==5 or grid[x1][y1]==3 or grid[x1][y1]==1 or grid[x1][y1]==6:
                    #print('cudhiuhdvuhudv')
                    count=[]
                    a=True
                    break
                #print("inside while")
                if grid[x1][y1]==2:
                    
                    for event1 in pygame.event.get():
                        if event1.type == pygame.MOUSEBUTTONDOWN:
                            
                            pos2_y , pos2_x = pygame.mouse.get_pos()
                            x2=pos2_x//w
                            y2=pos2_y//w
                            print(x2,y2)
                            print(grid[x2][y2])
                            

                            if grid[x2][y2]==5:
                                count=[]
                                print('inside')
                                a=True
                                break
                                
                                
                            #show(grid)
                            #print('hello')
                            if (grid[x2][y2]==3 and x2==x1-2 and y2==y1+2 and grid[x1-1][y1+1]==1):
                                count.append(1)
                                grid[x1][y1]=3
                                grid[x1-1][y1+1]=3
                                grid[x2][y2]=2
                                #show(grid)
                                win_or_lose(grid)
                                a = True
                                if x2==0:
                                    grid[x2][y2]=4
                                    print(grid)
                                break
                            if (grid[x2][y2]==3 and x2== x1-2 and y2==y1-2 and grid[x1-1][y1-1]==1):
                                count.append(1)
                                grid[x1][y1]=3
                                grid[x1-1][y1-1]=3
                                grid[x2][y2]=2
                                #show(grid)
                                win_or_lose(grid)
                                a = True
                                if x2==0:
                                    grid[x2][y2]=4
                                    print(grid)
                                break
                            if grid[x2][y2]==3 and x2==x1-1 and y2==y1+1:
                                count.append(1)
                                grid[x2][y2]=2
                                grid[x1][y1]=3
                                #show(grid)
                                win_or_lose(grid)
                                print(grid[0])
                                print(grid[1])
                                print(grid[2])
                                print(grid[3])
                                print(grid[4])
                                print(grid[5])
                                print(grid[6])
                                print(grid[7])
                                a = True
                                if x2==0:
                                    grid[x2][y2]=4
                                    print(grid)
                                break
                            if grid[x2][y2]==3 and x2==x1-1 and y2==y1-1:
                                count.append(1)
                                grid[x2][y2]=2
                                grid[x1][y1]=3
                                
                                print(grid[0])
                                print(grid[1])
                                print(grid[2])
                                print(grid[3])
                                print(grid[4])
                                print(grid[5])
                                print(grid[6])
                                print(grid[7])
                                #show(grid)
                                win_or_lose(grid)
                                a = True
                                if x2==0:
                                    grid[x2][y2]=4
                                    print(grid)
                                break
                           
                elif grid[x1][y1] == 4:
                    #print('ghora')

                    for event1 in pygame.event.get():
                        if event1.type == pygame.MOUSEBUTTONDOWN:
                            
                            pos2_y , pos2_x = pygame.mouse.get_pos()
                            x2=pos2_x//w
                            y2=pos2_y//w
                            print(x2,y2)
                            print(grid[x2][y2])
                            

                            if grid[x2][y2]==5:
                                count=[]
                                #print('ehciuwhc')
                                
                                a=True
                                break
                                
                                
                            
                            #print('hello')
                            if (grid[x2][y2]==3 and x2==x1-2 and y2==y1+2 and (grid[x1-1][y1+1]==1 or grid[x1-1][y1+1]==6)):
                                count.append(1)
                                grid[x1][y1]=3
                                grid[x1-1][y1+1]=3
                                grid[x2][y2]=4
                                #show(grid)
                                win_or_lose(grid)
                                a = True
                                
                                break

                            if (grid[x2][y2]==3 and x2==x1+2 and y2==y1+2 and (grid[x1+1][y1+1]==1 or grid[x1+1][y1+1]==6)):
                                count.append(1)
                                grid[x1][y1]=3
                                grid[x1+1][y1+1]=3
                                grid[x2][y2]=4
                                #show(grid)
                                win_or_lose(grid)
                                a = True
                                
                                break










                            
                            if (grid[x2][y2]==3 and x2== x1-2 and y2==y1-2 and (grid[x1-1][y1-1]==1 or grid[x1-1][y1-1]==6)):
                                count.append(1)
                                grid[x1][y1]=3
                                grid[x1-1][y1-1]=3
                                grid[x2][y2]=4
                                #show(grid)
                                win_or_lose(grid)
                                a = True
                                
                                break

                            if (grid[x2][y2]==3 and x2== x1+2 and y2==y1-2 and (grid[x1+1][y1-1]==1 or grid[x1+1][y1-1]==6)):
                                count.append(1)
                                grid[x1][y1]=3
                                grid[x1+1][y1-1]=3
                                grid[x2][y2]=4
                                #show(grid)
                                win_or_lose(grid)
                                a = True
                                
                                break







                            
                            if grid[x2][y2]==3 and x2==x1-1 and y2==y1+1:
                                count.append(1)
                                grid[x2][y2]=4
                                grid[x1][y1]=3
                                #show(grid)
                                win_or_lose(grid)
                                print(grid[0])
                                print(grid[1])
                                print(grid[2])
                                print(grid[3])
                                print(grid[4])
                                print(grid[5])
                                print(grid[6])
                                print(grid[7])
                                a = True
                                
                                break

                            if grid[x2][y2]==3 and x2==x1+1 and y2==y1+1:
                                count.append(1)
                                grid[x2][y2]=4
                                grid[x1][y1]=3
                                #show(grid)
                                win_or_lose(grid)
                                
                                a = True
                                
                                break







                            
                            if grid[x2][y2]==3 and x2==x1-1 and y2==y1-1:
                                count.append(1)
                                grid[x2][y2]=4
                                grid[x1][y1]=3
                                
                                print(grid[0])
                                print(grid[1])
                                print(grid[2])
                                print(grid[3])
                                print(grid[4])
                                print(grid[5])
                                print(grid[6])
                                print(grid[7])
                                #show(grid)
                                win_or_lose(grid)
                                a = True

                                break

                            if grid[x2][y2]==3 and x2==x1+1 and y2==y1-1:
                                count.append(1)
                                grid[x2][y2]=4
                                grid[x1][y1]=3
                                
                                
                                #show(grid)
                                win_or_lose(grid)
                                a = True

                                break







                
                    
                if len(count)%2 == 0 and len(count)!=0:
                    #show(grid)
                    win_or_lose(grid)
                    comp = comp_move(grid)
                    grid[comp[0]][comp[1]] = 3
                    if comp[5]== 1:
                        
                        grid[comp[2]][comp[3]] = 1
                    elif comp[5]==6:
                        grid[comp[2]][comp[3]] = 6
                        
                    #show(grid)
                    if comp[4] == 1 and comp[5]==1:
                        if comp[0] < comp[2]:
                            pitiwi_x = comp[0] + 1
                        else:
                            pitiwi_x = comp[0] - 1
                        if comp[3] < comp[1]:
                            pitiwi_y = comp[1] - 1
                        else:
                            pitiwi_y = comp[1] + 1
                   
                        
                        grid[pitiwi_x][pitiwi_y] = 3
                    
                    if comp[4] == 1 and comp[5]==6:
                        if comp[0] < comp[2] and comp[1] < comp[3]:
                            pitiwi_x = comp[0] + 1
                            pitiwi_y = comp[1] + 1

                        if comp[0] < comp[2] and comp[1] > comp[3]:
                            pitiwi_x = comp[0] + 1
                            pitiwi_y = comp[1] - 1


                        if comp[0] > comp[2] and comp[1] < comp[3]:
                            pitiwi_x = comp[0] - 1
                            pitiwi_y = comp[1] + 1


                        if comp[0] > comp[2] and comp[1] > comp[3]:
                            pitiwi_x = comp[0] - 1
                            pitiwi_y = comp[1] - 1



                        
##                        if comp[3] < comp[1]:
##                            pitiwi_y = comp[1] - 1
##                        else:
##                            pitiwi_y = comp[1] + 1
                   
                        
                        grid[pitiwi_x][pitiwi_y] = 3
                    if comp[2] == 7:
                        grid[comp[2]][comp[3]] = 6
                        print(grid)
                    
                    #show(grid)
                    win_or_lose(grid)
                    print(grid[0])
                    print(grid[1])
                    print(grid[2])
                    print(grid[3])
                    print(grid[4])
                    print(grid[5])
                    print(grid[6])
                    print(grid[7])

                            
    #grid()
    #show(grid)
    display()
    pygame.display.update()
    #show(grid)
##    new_Square(0,0)

