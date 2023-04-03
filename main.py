import numpy as np
import matplotlib.pyplot as plt

#world Height
WORLD_HEIGHT=7
#world Width
WORLD_WIDTH=10
#WIND COLUMN
WIND=[0,0,0,1,1,1,2,2,1,0]
#START AND GOAL POSITION
START=3*WORLD_WIDTH+0  #make each grid is a number
GOAL=3*WORLD_WIDTH+7
#ACTIONS
ACTIONS=["UP","DOWN","LEFT","RIGHT"]

def nextstate(kingbool,state,action): 
    if(kingbool):
        Wind_Prob=np.random.randint(1,4)
    else:
        Wind_Prob=1

    i=int(state/WORLD_WIDTH)
    j=state%WORLD_WIDTH
    if action=="UP":
        if(Wind_Prob==1):
            next_i=max(i-1-WIND[j],0)
        elif(Wind_Prob==2):
            next_i=max(i-1-WIND[j]-1,0)
        else:
            next_i=max(min(i-1-WIND[j]+1,WORLD_HEIGHT-1),0)
        return (next_i*WORLD_WIDTH+j)
    elif action=="DOWN":
        if(Wind_Prob==1):
            next_i=max(min(i+1-WIND[j],WORLD_HEIGHT-1),0)
        elif(Wind_Prob==2):
            next_i=max(i+1-WIND[j]-1,0)
        else:
            next_i=min(i+1-WIND[j]+1,WORLD_HEIGHT-1) 
        return (next_i*WORLD_WIDTH+j)
    elif action=="LEFT":
        if(Wind_Prob==1):
            next_i=max(i-WIND[j],0)
        elif(Wind_Prob==2):
            next_i=max(i-WIND[j]-1,0)
        else:
            next_i=max(min(i-WIND[j]+1,WORLD_HEIGHT-1),0)
        next_j=max(j-1,0)
        return (next_i*WORLD_WIDTH+ next_j)
    elif action=="RIGHT":
        if(Wind_Prob==1):
            next_i=max(i-WIND[j],0)
        elif(Wind_Prob==2):
            next_i=max(i-WIND[j]-1,0)
        else:
            next_i=max(min(i-WIND[j]+1,WORLD_HEIGHT-1),0)
        next_j=min(j+1,WORLD_WIDTH-1)
        return(next_i*WORLD_WIDTH+ next_j)

def Reward(state):
    if state==GOAL:
        return 1
    else:
        return -1

def greedy(state_table):
    greedyAction=''
    max_val= -1e10
    for action in ACTIONS:
        if(state_table[action]>max_val):
            greedyAction=action
            max_val=state_table[action]
    return greedyAction

def Greedy(state_table,epsilon):
    probability=[]
    greedyAction=greedy(state_table)
    for act in ACTIONS:
        if act==greedyAction:
            probability.append((epsilon /len(ACTIONS))+1-epsilon)
        else:
            probability.append(epsilon/len(ACTIONS))

    #return best action 
    choice= np.random.choice(ACTIONS,size=1,p=probability)
    return choice[0] 


    


def implement(kingbool,function,alpha,epsilon,gamma,Episode):
    #Initialize Q table
    if(function=="SARSA"):
        bool=True
    elif(function=="Qlearning"):
        bool=False

    Q_table={}
    for pos in range(WORLD_HEIGHT*WORLD_WIDTH):     
        Q_table[pos]={}
        for action in ACTIONS:
            action_table=Q_table[pos]
            if(bool or pos==GOAL):    #SARSA initialize
                action_table[action]=0
            else:        #Q-learning initialize
                action_table[action]=np.random.rand()

    ep=1
    step_list=[]
    step_total=0
    minmum=0
    while(ep<Episode):
        step=0
        state=START
        map=[(int(state/WORLD_WIDTH),state%WORLD_WIDTH)]
        if(bool): # SARSA algorithm
            action=Greedy(Q_table[state],epsilon)
        while state!=GOAL:
            if(not bool): # Q-larning algorithm
                action=Greedy(Q_table[state],epsilon)
            next_state=nextstate(kingbool,state,action)
            reward=Reward(next_state)
            if(bool):# SARSA use epsilon greedy
                next_action=Greedy(Q_table[next_state],epsilon)
            else:# Q-learning use action greedy
                next_action=greedy(Q_table[next_state])

            Q_table[state][action]+=alpha*(reward+ gamma*Q_table[next_state][next_action] - Q_table[state][action])
            state=next_state
            action=next_action
            step_total+=1
            step+=1
            map.append((int(state/WORLD_WIDTH),state%WORLD_WIDTH))
            step_list.append(ep)

        if(ep==1):
            minmum=step
        elif(minmum>step):
            minmum=step
            best_map=map
        ep+=1
    print("total steps are",step_total)
    print("the minmum step is ",minmum)
    print(best_map) 
    plt.plot(step_list)

    if(kingbool):
        string="with"
    else:
        string="without"
    plt.title("implement by %s  %s King's move ,(epsilon=%.2f,alpha=%.2f)"%(function,string,epsilon,alpha))
    plt.show()



if __name__=='__main__':
    print("Implement by SARSA without King's move")
    implement(kingbool=False,function="SARSA",alpha=0.5,epsilon=0.05,gamma=0.5,Episode=500)
    
    print("Implement by Q-Learning without King's move")
    implement(kingbool=False,function="Qlearning",alpha=0.5,epsilon=0.05,gamma=0.5,Episode=500)

    print("Implement by SARSA with King's move")
    implement(kingbool=True,function="SARSA",alpha=0.5,epsilon=0.05,gamma=0.5,Episode=500)

    print("Implement by Q-Learning with King's move")
    implement(kingbool=True,function="Qlearning",alpha=0.5,epsilon=0.05,gamma=0.5,Episode=500)
