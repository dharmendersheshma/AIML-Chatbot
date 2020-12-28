import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    input_sentance = input("You >> ")
    output_sentnce = kernel.respond(input_sentance)
    print("Elderbot >> " + output_sentnce)
