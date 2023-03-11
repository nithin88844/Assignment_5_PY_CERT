# Q. You are given a valid XML document, and you have to print its score. The score is calculated 
#       by the sum of the score of each element. For any element, the score is equal to the number 
#       f attributes it has.

numLines = int(input())
count = 0
for _ in range(numLines):
    line = input()
    count += line.count('=')
print (count)