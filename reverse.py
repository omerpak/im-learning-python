def reverse(value, output=[]):
    #range(start, stop, step)
    for i in range(len(value) - 1, -1, -1):
        output.append(value[i])
    
    return "".join(output)

text = input("say something man: ")
print("reversed text: {}".format(reverse(text)))
