class Sol:
    def climbing_stairs(self,numOfStairs):
        if numOfStairs ==1 or numOfStairs ==0:
            return 1
        return self.climbing_stairs(numOfStairs - 1) + self.climbing_stairs(numOfStairs - 2)
if __name__ == '__main__':
    numOfStairs=5
    p1=Sol()
    print(p1.climbing_stairs(numOfStairs))
