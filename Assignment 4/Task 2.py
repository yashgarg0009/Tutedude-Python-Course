# Step 1: Write user input to file
content_to_write = input("Enter text to write to the file: ")

myfile = open("output.txt", "w")    
myfile.write(content_to_write)
myfile.close()
print("Data successfully written to output.txt.")

# Step 2: Append additional data
additional_data = input("Enter additional text to append: ")

myfile = open("output.txt", "a")    
myfile.write("\n" + additional_data)
myfile.close()
print("Data successfully appended.")

# Step 3: Read and display final content
print("\nFinal content of output.txt:")
myfile = open("output.txt", "r")    
print(myfile.read())
myfile.close()
