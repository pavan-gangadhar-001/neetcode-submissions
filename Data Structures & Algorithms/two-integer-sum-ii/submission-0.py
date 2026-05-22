class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) -1
        # numbers = sorted(numbers)
        while i <j :
            print(i,j)
            if numbers[i] + numbers[j] ==  target:
                return [i+1,j+1]
            elif numbers[i] + numbers[j] > target:
                print("inside if")
                j-=1
            else:
                print("inside second if")
                i+=1
          
        return []