# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: MAIN
# Authors: Higor Alves
# Last updated: 12th December 2018
# ####################################################

from copy import deepcopy  # used to copy target without changing it



# ####################################################
# Functions to be called in Tetris function
# ####################################################

def generate_weighting(target):
        ''' Makes a weighted matrix, where a weighting is given to each target 1
            shape in accordance with how many neighbours they have'''
        new_target = deepcopy(target)
        
        # adds a border of 3 zeroes all the way around to prevent shapes extending past the target
        for i in range(len(new_target)):
            new_target[i] = [0] + [0] + [0] + new_target[i] + [0] + [0] + [0]
        new_target.insert([0][0], [0]*len(new_target[0])) # adds a line of 0s at the top of the target grid
        new_target.insert([0][0], [0]*len(new_target[0]))
        new_target.insert([0][0], [0]*len(new_target[0]))
        new_target.insert([len(new_target)][0], [0]*len(new_target[0])) # adds a line of 0s at the bottom of the target grid
        new_target.insert([len(new_target)][0], [0]*len(new_target[0]))
        new_target.insert([len(new_target)][0], [0]*len(new_target[0]))
        
        # generates the weightings for each target block
        for x in range(1, len(new_target)):
            for y in range(1, len(new_target[0])):
                weighting = 1
                #default set to 1 so encompassed blocks dont get a weighting of 0
                if new_target[x][y] == 0:
                    weighting -= 1
                elif new_target[x][y] == 1:
                    if new_target[x+1][y] == 0:
                        weighting +=1
                    if new_target[x-1][y] == 0:
                        weighting +=1
                    if new_target[x][y+1] == 0:
                        weighting +=1
                    if new_target[x][y-1] == 0:
                        weighting +=1
                    
                    new_target[x][y] = weighting
        return new_target
    
# ####################################################  
        
def format_answer(solution):
# Replace values in the wrong form with (0,0)
    for row in range(len(solution)):
        for col in range(len(solution[0])):
            if solution[row][col] == 0 :
                solution[row][col] = (0,0)
            if solution[row][col] == 1 :
                solution[row][col] = (0,0)
            if solution[row][col] == 2 :
                solution[row][col] = (0,0)
            if solution[row][col] == 3 :
                solution[row][col] = (0,0)
            if solution[row][col] == 4 :
                solution[row][col] = (0,0)
            if solution[row][col] == 5 :
                solution[row][col] = (0,0)
                
# ####################################################    

# ####################################################
# Tetris function to be called by performance_std.py
# ####################################################

def Tetris(target, limit_tetris): # limit_tetris is the number of each shape available    
    
    # list of all shapes to be used
    shapes_list = deepcopy(limit_tetris)
    
    weighted_target = generate_weighting(target)
    
    width = len(weighted_target[0])
    height = len(weighted_target)
    
    # make a solution matrix of equal size to target
    solution = [[(0) for col in range(0, width)] for row in range(0, height)]
                
    accuracy_range = [4,3,2,1]
    
    piece_id = 0
    # starting with the most accurate, runs the following
    for accuracy in accuracy_range:
        for x in range(0, height):
            for y in range (0, width):
                scores = {0:0}
                #Tree of shapes
                if weighted_target[x][y] >= accuracy:
                    if weighted_target[x][y+1] != 0:
                        if weighted_target[x+1][y+1] != 0:
                            #SHAPE 1 
                            if weighted_target[x+1][y] != 0:
                                if shapes_list[1] > 0:
                                    score = int(weighted_target[x][y])+ int(weighted_target[x][y+1]) + int(weighted_target[x+1][y]) + int(weighted_target[x+1][y+1])
                                    scores.update({1:score})
                            
                            #SHAPE 6
                            if weighted_target[x+2][y+1] != 0:
                                if shapes_list[6] > 0:
                                    score = int(weighted_target[x][y])+ int(weighted_target[x][y+1]) + int(weighted_target[x+1][y+1]) + int(weighted_target[x+2][y+1])
                                    scores.update({6:score})
                                    
                            #SHAPE 18    
                            if weighted_target[x+1][y+2] != 0:
                                if shapes_list[18] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x][y+1]) + int(weighted_target[x+1][y+1]) + int(weighted_target[x+1][y+2])
                                    scores.update({18:score})
                                
                        if weighted_target[x][y+2] != 0:
                            #SHAPE 7
                            if weighted_target[x+1][y] != 0:
                                if shapes_list[7] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x][y+1]) + int(weighted_target[x][y+2]) + int(weighted_target[x+1][y])
                                    scores.update({7:score})
                            
                            #SHAPE 15
                            if weighted_target[x+1][y+1] != 0:
                                if shapes_list[15] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x][y+1]) + int(weighted_target[x][y+2]) + int(weighted_target[x+1][y+1])
                                    scores.update({15:score})
                            #SHAPE 9                                
                            if weighted_target[x+1][y+2] != 0:
                                if shapes_list[9] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x][y+1]) + int(weighted_target[x][y+2]) + int(weighted_target[x+1][y+2])
                                    scores.update({9:score})
                                    
                            #SHAPE 3    
                            if weighted_target[x][y+3] != 0:     
                                if shapes_list[3] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x][y+1]) + int(weighted_target[x][y+2]) + int(weighted_target[x][y+3])
                                    scores.update({3:score})
                                
                    if weighted_target[x+1][y] != 0:
                        if weighted_target[x+1][y+1] != 0:
                            #SHAPE 13
                            if weighted_target[x+1][y-1] != 0:
                                if shapes_list[13] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y+1]) + int(weighted_target[x+1][y-1])
                                    scores.update({13:score})
                                    
                            #SHAPE 12
                            if weighted_target[x+2][y] != 0:       
                                if shapes_list[12] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y+1]) + int(weighted_target[x+2][y])
                                    scores.update({12:score})
                                    
                            #SHAPE 17                                
                            if weighted_target[x+2][y+1] != 0:
                                if shapes_list[17] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y+1]) + int(weighted_target[x+2][y+1])
                                    scores.update({17:score})
                                    
                            #SHAPE 11    
                            if weighted_target[x+1][y+2] != 0:
                                if shapes_list[11] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y+1]) + int(weighted_target[x+1][y+2])
                                    scores.update({11:score})
                                
                        if weighted_target[x+2][y] != 0:
                            #SHAPE 2
                            if weighted_target[x+3][y] != 0:
                                if shapes_list[2] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+2][y]) + int(weighted_target[x+3][y])
                                    scores.update({2:score})
                                    
                            #SHAPE 8    
                            if weighted_target[x+2][y-1] != 0:
                                if shapes_list[8] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+2][y]) + int(weighted_target[x+2][y-1])
                                    scores.update({8:score})
                                    
                            #SHAPE 4    
                            if weighted_target[x+2][y+1] != 0:
                                if shapes_list[4] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+2][y]) + int(weighted_target[x+2][y+1])
                                    scores.update({4:score})
                                    
                            #SHAPE 10    
                            if weighted_target[x][y+1] != 0:
                                if shapes_list[10] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+2][y]) + int(weighted_target[x][y+1])
                                    scores.update({10:score})
                                
                        if weighted_target[x+1][y-1] != 0:
                            #SHAPE 5
                            if weighted_target[x+1][y-2] != 0:
                                if shapes_list[5] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y-1]) + int(weighted_target[x+1][y-2])
                                    scores.update({5:score})
                                    
                            #SHAPE 19    
                            if weighted_target[x+2][y-1] != 0:
                                if shapes_list[19] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y-1]) + int(weighted_target[x+2][y-1])
                                    scores.update({19:score})
                                    
                            #SHAPE 14    
                            if weighted_target[x+2][y] != 0:
                                if shapes_list[14] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y-1]) + int(weighted_target[x+2][y])
                                    scores.update({14:score})
                                    
                            #SHAPE 16    
                            if weighted_target[x][y+1] != 0:
                                if shapes_list[16] > 0:
                                    score = int(weighted_target[x][y])+int(weighted_target[x+1][y]) + int(weighted_target[x+1][y-1]) + int(weighted_target[x][y+1])
                                    scores.update({16:score})
                                    
                    shape_max = max(scores, key=scores.get)  
                    
                    if shape_max == 1:
                        #border is max here ie isolated piece
                        weighting = 2
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0:
                            weighting += 1
                        if weighted_target[x][y+2] == 0:
                            weighting += 1
                        if weighted_target[x+1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0:
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0:
                            weighting += 1
                        if weighted_target[x-1][y] == 0:
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0:
                            weighting += 1
                        if weighting > accuracy:
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+1][y+1] = 0
                            
                            solution[x][y] = (1,piece_id)
                            solution[x][y+1] = (1,piece_id)
                            solution[x+1][y] = (1,piece_id)
                            solution[x+1][y+1] = (1,piece_id)
                            
                            shapes_list[1] -= 1
                            
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0:
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x][y+2] != 0:
                                weighted_target[x][y+2] += 1
                            if weighted_target[x+1][y+2] != 0: 
                                weighted_target[x+1][y+2] += 1
                            if weighted_target[x+2][y] != 0:
                                weighted_target[x+2][y] += 1
                            if weighted_target[x+2][y+1] != 0:
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x-1][y] != 0:
                                weighted_target[x-1][y] += 1
                            if weighted_target[x-1][y+1] != 0:
                                weighted_target[x-1][y+1] += 1  
    
    
                # SHAPE 2       
                    if shape_max == 2:
                        weighting = 0
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+4][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0:
                            weighting += 1
                        if weighted_target[x+3][y+1] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+2][y] = 0
                            weighted_target[x+3][y] = 0
                            
                            solution[x][y] = (2,piece_id)
                            solution[x+1][y] = (2,piece_id)
                            solution[x+2][y] = (2,piece_id)
                            solution[x+3][y] = (2,piece_id)
                            
                            shapes_list[2] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+4][y] != 0: 
                                weighted_target[x+4][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x+2][y-1] != 0: 
                                weighted_target[x+2][y-1] += 1
                            if weighted_target[x+3][y-1] != 0: 
                                weighted_target[x+3][y-1] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x+2][y+1] != 0:
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x+3][y+1] != 0:
                                weighted_target[x+3][y+1] += 1
                                  
                                
                #SHAPE 3
                    if shape_max == 3:
                        weighting = 0
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+4] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+2] == 0:
                            weighting += 1
                        if weighted_target[x+1][y+3] == 0:
                            weighting += 1
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+3] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x][y+2] = 0
                            weighted_target[x][y+3] = 0 
                            
                            solution[x][y] = (3,piece_id)
                            solution[x][y+1] = (3,piece_id)
                            solution[x][y+2] = (3,piece_id)
                            solution[x][y+3] = (3,piece_id)                           

    
                            shapes_list[3] -= 1
                            
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x][y+4] != 0: 
                                weighted_target[x][y+4] += 1
                            if weighted_target[x+1][y] != 0: 
                                weighted_target[x+1][y] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x+1][y+2] != 0:
                                weighted_target[x+1][y+2] += 1
                            if weighted_target[x+1][y+3] != 0:
                                weighted_target[x+1][y+3] += 1
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x-1][y+1] != 0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x-1][y+2] != 0: 
                                weighted_target[x-1][y+2] += 1
                            if weighted_target[x-1][y+3] != 0:
                                weighted_target[x-1][y+3] += 1
                          
                            
                #SHAPE 4  
                
                    if shape_max == 4:
                        weighting = 2
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+2] == 0:
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y+1] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+2][y] = 0
                            weighted_target[x+2][y+1] = 0
                            
                            solution[x][y] = (4,piece_id)
                            solution[x+1][y] = (4,piece_id)
                            solution[x+2][y] = (4,piece_id)
                            solution[x+2][y+1] = (4,piece_id)

                            shapes_list[4] -= 1
                            
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+2][y+2] != 0:
                                weighted_target[x+2][y+2] += 1
                            if weighted_target[x+2][y-1] != 0: 
                                weighted_target[x+2][y-1] += 1
                            if weighted_target[x+3][y] != 0: 
                                weighted_target[x+3][y] += 1
                            if weighted_target[x+3][y+1] != 0:
                                weighted_target[x+3][y+1] += 1
                            
                        
                #SHAPE 5      
                    if shape_max == 5:
                        weighting = 2
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if  weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-3] == 0:
                            weighting += 1
                        if weighted_target[x+2][y-2] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x][y-2] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0 
                            weighted_target[x+1][y-2] = 0 
                            weighted_target[x+1][y-1] = 0  
                            weighted_target[x+1][y] = 0  
                                
                            solution[x][y] = (5,piece_id)
                            solution[x+1][y-2] = (5,piece_id)
                            solution[x+1][y-1] = (5,piece_id)
                            solution[x+1][y] = (5,piece_id)
                            
                            shapes_list[5] -= 1
                            
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if  weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y] != 0: 
                                weighted_target[x+2][y] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x+1][y-3] != 0:
                                weighted_target[x+1][y-3] += 1
                            if weighted_target[x+2][y-2] != 0: 
                                weighted_target[x+2][y-2] += 1
                            if weighted_target[x+2][y-1] != 0: 
                                weighted_target[x+2][y-1] += 1
                            if weighted_target[x][y-2] != 0:
                                weighted_target[x][y-2] += 1
               
                            
                #SHAPE 6
                    if shape_max == 6:
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+2] == 0:
                            weighting += 1
                        if weighted_target[x][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+2] == 0:
                            weighting += 1
                        if weighted_target[x+3][y+1] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:   
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x+1][y+1] = 0
                            weighted_target[x+2][y+1] = 0   
                            
                            solution[x][y] = (6,piece_id)
                            solution[x][y+1] = (6,piece_id)
                            solution[x+1][y+1] = (6,piece_id)
                            solution[x+2][y+1] = (6,piece_id)
                            
                            shapes_list[6] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y] != 0: 
                                weighted_target[x+2][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y] != 0: 
                                weighted_target[x+1][y] += 1
                            if weighted_target[x+1][y+2] != 0:
                                weighted_target[x+1][y+2] += 1
                            if weighted_target[x][y+2] != 0: 
                                weighted_target[x][y+2] += 1
                            if weighted_target[x-1][y+1] != 0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x+2][y+2] != 0:
                                weighted_target[x+2][y+2] += 1
                            if weighted_target[x+3][y+1] != 0:
                                weighted_target[x+3][y+1] += 1
                       
    
                #SHAPE 7   
                    if shape_max == 7:
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x][y+3] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+2] == 0: 
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1

                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x][y+2] = 0
                            weighted_target[x+1][y] = 0
                            
                            solution[x][y] = (7,piece_id)
                            solution[x][y+1] = (7,piece_id)
                            solution[x][y+2] = (7,piece_id)
                            solution[x+1][y] = (7,piece_id)
    
                            shapes_list[7] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y] != 0: 
                               weighted_target[x+2][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x-1][y+1] != 0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x-1][y+2] != 0: 
                                weighted_target[x-1][y+2] += 1
                            if weighted_target[x][y+3] != 0: 
                                weighted_target[x][y+3] += 1
                            if weighted_target[x+1][y+2] != 0: 
                                weighted_target[x+1][y+2] += 1
                 
                
                #SHAPE 8
                    if shape_max == 8: 
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0:
                            weighting += 1
                        if weighted_target[x+2][y-2] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y-1] == 0: 
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+2][y-1] = 0
                            weighted_target[x+2][y] = 0
                            
                            solution[x][y] = (8,piece_id)
                            solution[x+1][y] = (8,piece_id)
                            solution[x+2][y-1] = (8,piece_id)
                            solution[x+2][y] = (8,piece_id)
    
                            shapes_list[8] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+3][y] != 0: 
                                weighted_target[x+3][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+2][y+1] != 0:
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x+2][y-2] != 0: 
                                weighted_target[x+2][y-2] += 1
                            if weighted_target[x+3][y-1] != 0: 
                                weighted_target[x+3][y-1] += 1

                
                #SHAPE 9
                    if shape_max == 9:    
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y] == 0:
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x][y+3] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+3] == 0:
                            weighting += 1
                        if weighted_target[x+2][y+2] == 0:
                            weighting += 1
                            
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x][y+2] = 0
                            weighted_target[x+1][y+2] = 0
                            
                            solution[x][y] = (9,piece_id)
                            solution[x][y+1] = (9,piece_id)
                            solution[x][y+2] = (9,piece_id)
                            solution[x+1][y+2] = (9,piece_id)
    
                            shapes_list[9] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+1][y] != 0:
                                weighted_target[x+1][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x-1][y+1] != 0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x-1][y+2] != 0: 
                                weighted_target[x-1][y+2] += 1
                            if weighted_target[x][y+3] != 0: 
                                weighted_target[x][y+3] += 1
                            if weighted_target[x+1][y+3] != 0:
                                weighted_target[x+1][y+3] += 1
                            if weighted_target[x+2][y+2] != 0:
                                weighted_target[x+2][y+2] += 1
                          
            
                #SHAPE 10
                    if shape_max == 10:  
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+2][y] = 0
                            
                            solution[x][y] = (10,piece_id)
                            solution[x][y+1] = (10,piece_id)
                            solution[x+1][y] = (10,piece_id)
                            solution[x+2][y] = (10,piece_id)

                            shapes_list[10] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+3][y] != 0: 
                                weighted_target[x+3][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x-1][y+1] != 0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x][y+2] != 0: 
                                weighted_target[x][y+2] += 1
                            if weighted_target[x+2][y+1] != 0: 
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x+2][y-1] != 0:
                                weighted_target[x+2][y-1] += 1
                    
                
                #SHAPE 11
                    if shape_max == 11:   
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+3] == 0:
                            weighting += 1                       
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+1][y+1] = 0
                            weighted_target[x+1][y+2] = 0
                            
                            solution[x][y] = (11,piece_id)
                            solution[x+1][y] = (11,piece_id)
                            solution[x+1][y+1] = (11,piece_id)
                            solution[x+1][y+2] = (11,piece_id)
    
                            shapes_list[11] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y] != 0: 
                                weighted_target[x+2][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+2][y+1] != 0: 
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x+2][y+2] != 0: 
                                weighted_target[x+2][y+2] += 1
                            if weighted_target[x][y+2] != 0: 
                                weighted_target[x][y+2] += 1
                            if weighted_target[x+1][y+3] != 0:
                                weighted_target[x+1][y+3] += 1
                            
                            
                #SHAPE 12
                    if shape_max == 12: 
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y] == 0:   
                            weighting += 1         
                            
                        if weighting > accuracy:   
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+1][y+1] = 0
                            weighted_target[x+2][y] = 0
                            
                            solution[x][y] = (12,piece_id)
                            solution[x+1][y] = (12,piece_id)
                            solution[x+1][y+1] = (12,piece_id)
                            solution[x+2][y] = (12,piece_id)
    
                            shapes_list[12] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y-1] != 0: 
                                weighted_target[x+2][y-1] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x+1][y+2] != 0: 
                                weighted_target[x+1][y+2] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+2][y+1] != 0: 
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x+3][y] != 0:   
                                weighted_target[x+3][y] += 1
                                
      
                #SHAPE 13
                    if shape_max == 13: 
                        weighting = 2
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-2] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0:
                            weighting += 1                     
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y-1] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+1][y+1] = 0 
                            
                            solution[x][y] = (13,piece_id)
                            solution[x+1][y-1] = (13,piece_id)
                            solution[x+1][y] = (13,piece_id)
                            solution[x+1][y+1] = (13,piece_id)
    
                            shapes_list[13] -= 1
                            
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+1][y-2] != 0: 
                                weighted_target[x+1][y-2] += 1
                            if weighted_target[x+2][y+1] != 0: 
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x+2][y] != 0: 
                                weighted_target[x+2][y] += 1
                            if weighted_target[x+2][y-1] != 0: 
                                weighted_target[x+2][y-1] += 1
                            if weighted_target[x+2][y+1] != 0:
                                weighted_target[x+2][y+1] += 1
                                
                                      
                #SHAPE 14
                    if shape_max == 14:  
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-2] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0: 
                            weighting += 1                    
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y-1] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+2][y] = 0
                            
                            solution[x][y] = (14,piece_id)
                            solution[x+1][y-1] = (14,piece_id)
                            solution[x+1][y] = (14,piece_id)
                            solution[x+2][y] = (14,piece_id)
    
                            shapes_list[14] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+3][y] != 0: 
                                weighted_target[x+3][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-2] != 0: 
                                weighted_target[x+1][y-2] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+2][y+1] != 0: 
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x+2][y-1] != 0: 
                                weighted_target[x+2][y-1] += 1
                            
    
                #SHAPE 15
                    if shape_max == 15:   
                        weighting = 2
                        if weighted_target[x-1][y] == 0:
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x][y+3] == 0:
                            weighting += 1                 
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x][y+2] = 0
                            weighted_target[x+1][y+1] = 0
                            
                            solution[x][y] = (15,piece_id)
                            solution[x][y+1] = (15,piece_id)
                            solution[x][y+2] = (15,piece_id)
                            solution[x+1][y+1] = (15,piece_id)
    
                            shapes_list[15] -= 1
                            
                            if weighted_target[x-1][y] != 0:
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y+1] != 0: 
                                weighted_target[x+2][y+1] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y] != 0: 
                                weighted_target[x+1][y] += 1
                            if weighted_target[x+1][y+2] != 0: 
                                weighted_target[x+1][y+2] += 1
                            if weighted_target[x-1][y+1] != 0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x-1][y+2] != 0: 
                                weighted_target[x-1][y+2] += 1
                            if weighted_target[x][y+3] != 0:
                                weighted_target[x][y+3] += 1
                                
                            
                #SHAPE 16
                    if shape_max == 16:  
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0:
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-2] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-1] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x+1][y-1] = 0
                            weighted_target[x+1][y] = 0
                            
                            solution[x][y] = (16,piece_id)
                            solution[x][y+1] = (16,piece_id)
                            solution[x+1][y-1] = (16,piece_id)
                            solution[x+1][y] = (16,piece_id)
    
                            shapes_list[16] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y] != 0: 
                                weighted_target[x+2][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y+1] != 0:
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x-1][y+1] != 0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x][y+2] != 0: 
                                weighted_target[x][y+2] += 1
                            if weighted_target[x+1][y-2] != 0: 
                                weighted_target[x+1][y-2] += 1
                            if weighted_target[x+2][y-1] != 0:
                                weighted_target[x+2][y-1] += 1
                                
                            
                #SHAPE 17
                    if shape_max == 17:    
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y+1] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                                                        
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+1][y+1] = 0
                            weighted_target[x+2][y+1] = 0
                            
                            solution[x][y] = (17,piece_id)
                            solution[x+1][y] = (17,piece_id)
                            solution[x+1][y+1] = (17,piece_id)
                            solution[x+2][y+1] = (17,piece_id)
    
                            shapes_list[17] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y] != 0: 
                                weighted_target[x+2][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-1] != 0: 
                                weighted_target[x+1][y-1] += 1
                            if weighted_target[x+1][y+2] != 0: 
                                weighted_target[x+1][y+2] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+2][y+2] != 0: 
                                weighted_target[x+2][y+2] += 1
                            if weighted_target[x+3][y+1] != 0:
                                weighted_target[x+3][y+1] += 1
    
                
                #SHAPE 18
                    if shape_max == 18:  
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+3] == 0: 
                            weighting += 1
                        if weighted_target[x][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x-1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+2] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y+1] == 0:
                            weighting += 1
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x][y+1] = 0
                            weighted_target[x+1][y+1] = 0
                            weighted_target[x+1][y+2] = 0
                            
                            solution[x][y] = (18,piece_id)
                            solution[x][y+1] = (18,piece_id)
                            solution[x+1][y+1] = (18,piece_id)
                            solution[x+1][y+2] = (18,piece_id)

                            shapes_list[18] -= 1
                            
                            if weighted_target[x-1][y] !=0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+1][y] !=0: 
                                weighted_target[x+1][y] += 1
                            if weighted_target[x][y-1] !=0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y+3] !=0: 
                                weighted_target[x+1][y+3] += 1
                            if weighted_target[x][y+2] !=0: 
                                weighted_target[x][y+2] += 1
                            if weighted_target[x-1][y+1] !=0: 
                                weighted_target[x-1][y+1] += 1
                            if weighted_target[x+2][y+2] !=0: 
                                weighted_target[x+2][y+2] += 1
                            if weighted_target[x+2][y+1] !=0:
                                weighted_target[x+2][y+1] += 1
                                
                            
                #SHAPE 19          
                    if shape_max == 19: 
                        weighting = 2
                        if weighted_target[x-1][y] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y] == 0: 
                            weighting += 1
                        if weighted_target[x][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y-2] == 0: 
                            weighting += 1
                        if weighted_target[x+1][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x][y+1] == 0: 
                            weighting += 1
                        if weighted_target[x+3][y-1] == 0: 
                            weighting += 1
                        if weighted_target[x+2][y-2] == 0:
                            weighting += 1                         
                            
                        if weighting > accuracy:    
                            piece_id += 1
                            
                            weighted_target[x][y] = 0
                            weighted_target[x+1][y-1] = 0
                            weighted_target[x+1][y] = 0
                            weighted_target[x+2][y-1] = 0
                            
                            solution[x][y] = (19,piece_id)
                            solution[x+1][y-1] = (19,piece_id)
                            solution[x+1][y] = (19,piece_id)
                            solution[x+2][y-1] = (19,piece_id)                      
    
                            shapes_list[19] -= 1
                            
                            if weighted_target[x-1][y] != 0: 
                                weighted_target[x-1][y] += 1
                            if weighted_target[x+2][y] != 0: 
                                weighted_target[x+2][y] += 1
                            if weighted_target[x][y-1] != 0: 
                                weighted_target[x][y-1] += 1
                            if weighted_target[x+1][y-2] != 0: 
                                weighted_target[x+1][y-2] += 1
                            if weighted_target[x+1][y+1] != 0: 
                                weighted_target[x+1][y+1] += 1
                            if weighted_target[x][y+1] != 0: 
                                weighted_target[x][y+1] += 1
                            if weighted_target[x+3][y-1] != 0: 
                                weighted_target[x+3][y-1] += 1
                            if weighted_target[x+2][y-2] != 0:
                                weighted_target[x+2][y-2] += 1
                                
                                
# ####################################################
# Format solution to the way the answer wants it
# ####################################################
    final_solution = []
    for row in solution:
        #remove zeros from the start and end of each column
        final_solution.append(row[3:-3])
    #removes rows of zeros on top and bottom
    final_solution = final_solution[3:-3] 
    format_answer(final_solution)

    return final_solution