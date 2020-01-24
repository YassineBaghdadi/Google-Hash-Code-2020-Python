


class Solution(object):
     def __init__(self):
        self.file = open('e_also_big.in','r')

        #m the max of pizza slides 
        #n pizza's count
        self.lines = self.file.read().split('\n')
        self.m, self.n = self.lines[0].split(' ')
        self.pizzas_indexs = []
        for i in range(len(str(self.lines[1]).split(' '))):
                self.pizzas_indexs.append(i)
        

        self.values = []
        for i in str(self.lines[1]).split(' '):
            self.values.append(int(i))

        self.sum_ = 0
        self.solution = []
        self.pizzas_indexs = list(reversed(self.pizzas_indexs))


        for i in self.pizzas_indexs:   
            if (self.sum_ + self.values[i]) <= int(self.m):
                self.sum_ += self.values[i]
                self.solution.append(i)

        self.soli = []
        for i in self.solution:
            self.soli.append(str(i))

        open('output.txt', 'w').write(str(len(self.soli)) + '\n')
        for i in list(reversed(self.soli)):
            open('output.txt', 'a').write(i + ' ')
         
          


solu = Solution()