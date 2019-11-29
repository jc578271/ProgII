import random

# Input fahrenheit into input.txt
in_file = open('temps_input.txt', 'w')
temp = random.uniform(-200, 200)
for i in range(15):
    temp = random.uniform(-200, 200)
    in_file.write('{}\n'.format(temp))
in_file.close()


def main():
    in_file = open('temps_input.txt', 'r')
    out_file = open('temps_output.txt', 'w')
    
    # Reach each line on temp_input.txt
    for line_str in in_file:
        line_str = float(line_str)  #  convert type of line_str to float
        line_str = covertFahrenheitToCelcius(line_str)   # use converting function
        print(line_str,file=out_file) # Input celcius into temps_out.txt
        print('{}'.format(line_str))
    in_file.close()
    out_file.close()


def covertFahrenheitToCelcius(temp):
    return 5 / 9 * (temp - 32)


main()