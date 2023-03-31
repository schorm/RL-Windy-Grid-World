# RL-Windy-Grid-World(SARSA and_Q-learning) 

![image](https://user-images.githubusercontent.com/67517025/229214100-4e3190a2-4e8b-4374-87fb-c35f3874f2a6.png)

The mission is to have a agent travel from the start point to the goal point successfully. Now this is a just standard grid world, if adding a crosswind running upward through the middle of the grid, it turns to be the windy grid world. (King's move)

## SARSA without King's move
![image](https://user-images.githubusercontent.com/67517025/229214415-4226fea7-a133-48d6-853d-262d080296da.png)

total steps are 13218

the minmum step is  15

[(3, 0), (3, 1), (3, 2), (3, 3), (2, 4), (1, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (4, 8), (3, 7)]

## Q-learning without King's move 
![image](https://user-images.githubusercontent.com/67517025/229214605-0508ecec-8839-4348-984d-ebf0abbe1421.png)

total steps are 12944

the minmum step is  15

[(3, 0), (3, 1), (3, 2), (3, 3), (2, 4), (1, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (4, 8), (3, 7)]

## SARSA with King;s move
![image](https://user-images.githubusercontent.com/67517025/229214719-0d6db306-90dc-456b-995b-17d97dbf7594.png)

total steps are 23982

the minmum step is  10

[(3, 0), (4, 0), (6, 0), (6, 1), (6, 2), (6, 3), (5, 4), (5, 5), (4, 5), (4, 6), (3, 7)]

## Q-learning with King'smove 
![image](https://user-images.githubusercontent.com/67517025/229214817-4d69a801-fd47-40fe-a62a-cc419d26952f.png)

total steps are 26652

the minmum step is  8

[(3, 0), (5, 0), (5, 1), (5, 2), (6, 3), (6, 4), (6, 5), (5, 6), (3, 7)]
