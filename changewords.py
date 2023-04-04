#This code is used to change words in an array to a different words
arr = "Initially, one print was obtained from the primary code outside the parallel region. Following this, nine prints were obtained from a subprogram outside the parallel region, comprising one print from the subprogram outside the parallel region and eight prints from the subprogram's parallel region. Eight prints were then obtained from the main program's parallel region, followed by eight prints from the subprogram's non-parallel region and eight prints from the subprogram's parallel region. In total, there were thirty-four prints, and at this point, I realized that something was counter-intuitive due to the presence of a parallel region within another parallel region. As my computer's default number of threads was eight, the program should have used a total of sixty-four threads (eight threads multiplied by eight threads). However, after some investigation, I discovered that nested parallel loops are deactivated by default. Consequently, my program only obeyed the first parallelization and ignored the nested parallelization. To activate nested parallelization, one must set a Boolean environmental variable to true to activate nested loops"
arr = arr.replace("eight", "twelve")
arr = arr.replace("Eight", "Twelve")
arr = arr.replace("EIGHT", "TWELVE")
arr = arr.replace("sixty-four", "one hundred and twenty-eight")
arr = arr.replace("Sixty-four", "One hundred and twenty-eight")
arr = arr.replace("SIXTY-FOUR", "ONE HUNDRED AND TWENTY-EIGHT")
print(arr)

with open('text.txt', 'w') as f:
    f.write(arr)