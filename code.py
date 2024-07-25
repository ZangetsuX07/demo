import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("/content/std-startup (1).xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
  input_text=input("Hospital BOT:")
  response =kernel.respond(input_text)
  print(">Bot:"+response)