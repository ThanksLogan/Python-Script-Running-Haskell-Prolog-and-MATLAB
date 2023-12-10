import subprocess

print("Running MATLAB CODE 1")
# Specify the full path to the MATLAB executable
# Adjust the path accordingly
matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'
matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlabcode1.m'); pause(3);"]
    , capture_output=True)

with open('input.txt', 'r') as file:
        line = file.readline()
        input_array = [int(value) for value in line.split()]

print("Running C code")
# running c code
subprocess.run(["gcc", "Cprog2.c", "-o", "Cprog2"])

# Convert input_array to strings
input_array_str = [str(value) for value in input_array]

# Execute subprocess
process = subprocess.run(["./Cprog2"] + input_array_str, capture_output=True, text=True)

output_variable = process.stdout.strip()

with open('c_output.txt', 'w') as f:
        f.write(output_variable)



print("Running Haskell Code")
subprocess.run(['ghc', 'haskellcode.hs'])
process = subprocess.run(['./haskellcode'] + [str(x) for x in input_array], text=True, capture_output=True)
result = process.stdout.strip()

output_variable2 = process.stdout.strip()

with open('h_output.txt', 'w') as f:
        f.write(output_variable2)


print("Running prolog code")
prolog_input = "[" + ",".join(map(str, input_array)) + "]."
result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'pcode.pl'], input=prolog_input,
                        capture_output=True, text=True)
output_variable3 = result.stdout.strip()

with open('p_output.txt', 'w') as f:
        f.write(output_variable3)



print("Running MATLAB CODE 2")
# Specify the full path to the MATLAB executable
# Adjust the path accordingly
matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'
matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlabcode2.m'); pause(5);"]
, capture_output=True)

with open('input.txt', 'r') as file:
        line = file.readline()
        input_array = [int(value) for value in line.split()]
