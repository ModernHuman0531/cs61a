def hanoi(disc_num , start_pill , goal_pill):
    if disc_num == 1:#One disc , you can directly move it
        move(disc_num , start_pill , goal_pill)
    else:
        spare_pill = 6 - start_pill - goal_pill#spare_pill will change as the goal_pill change
        hanoi(disc_num -1 , start_pill , spare_pill)
        move(disc_num , start_pill , goal_pill)
        hanoi(disc_num - 1 , spare_pill, goal_pill)
        
    
    
def move(disc_num , from_pill , to_pill):
    print("Move disk" , disc_num , "from pill" , from_pill , "to pill" , to_pill)