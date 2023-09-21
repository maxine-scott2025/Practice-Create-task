colors = {"Red":[[0,255],[0,0],[0,0],"blue"], "Yellow": [[0,255],[165,255],[0,0]],'Orange': [[0,255],[0,165],[0,0]]}

R = int(input("Please input your RBG value for Red"))

B = int(input("Please input your RBG value for Blue"))

G = int(input("Please input your RBG value for Green"))

def check(colors,R,G,B):
  for i in colors:
    
    if R >=colors[i][0][0] and R <= colors[i][0][1] and G >= colors[i][1][0] and G <= colors[i][1][1] and B >= colors[i][2][0] and B <= colors[i][2][1]:

       print("The color you inputted was " + i + " and the complent to your color is " + colors[i][3])
check(colors,R,G,B)  