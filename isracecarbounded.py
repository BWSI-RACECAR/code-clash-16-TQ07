class Solution:
    def isracecarbounded(self, instructions):
            #type instructions: string
            #return type: boolean
            initial_pos=[0,0]
            cur_pos=[0,0]
            #direction= ['S':0,'W':1,'N':2,'E':3] Reference for cur_dir (current direction)
            cur_dir=2
            angle = 0
            print(instructions)
            return(instructions.count("R") != instructions.count("L"))
            # for b in range(3):
            #     for i in range(len(instructions)):
            #         if angle == 0:
            #             if instructions[i] == "G":
            #                 cur_pos = [cur_pos[0], cur_pos[1] + 1]
            #         if angle == 90:
            #             if instructions[i] == "G":
            #                 cur_pos = [cur_pos[0] + 1, cur_pos[1]]
            #         if angle == 180:
            #             if instructions[i] == "G":
            #                 cur_pos = [cur_pos[0], cur_pos[1]  - 1]
            #         if angle == 270:
            #             if instructions[i] == "G":
            #                 cur_pos = [cur_pos[0] - 1, cur_pos[1]]
            #         if angle == 360:
            #             if instructions[i] == "G":
            #                 cur_pos = [cur_pos[0], cur_pos[1] + 1]
            #         if angle == 360:
            #             angle = 0
            #         if instructions[i] == "L":
            #             angle = angle + 90
            #         if instructions[i] == "R":
            #             angle = angle - 90
                    
            # if cur_pos == initial_pos:
            #     return True
            # else:
            #     return False
        
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            pass
        
def main():
    input1=input()
    tc1 = Solution()
    ans = tc1.isracecarbounded(input1)
    print(ans)

if __name__ == "__main__":
    main()
