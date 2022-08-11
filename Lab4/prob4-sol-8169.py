sum = 0
count = 0
end_input = False
while not end_input:
    try:
        n = int(input("Enter an integer:"))
        if n > 0:           
           sum = sum + n
           count = count + 1
           avg = sum / count
        elif avg == 0:
            exit()
        else:
            break
    except ValueError:
        print("Please enter a valid integer")        
print(f"Average is {avg}")