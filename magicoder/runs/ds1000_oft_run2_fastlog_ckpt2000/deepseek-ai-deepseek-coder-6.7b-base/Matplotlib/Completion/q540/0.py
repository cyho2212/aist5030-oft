
# Split the title into multiple lines
lines = myTitle.split(' ')

# Initialize a new list to store the lines
new_lines = []

# Initialize a variable to store the current line
current_line = ''

# Iterate through the words in the title
for word in lines:
    # If the current line plus the next word would exceed the maximum length, add the current line to the new list and start a new line
    if len(current_line) + len(word) > 60:
        new_lines.append(current_line)
        current_line = word
    # Otherwise, add the word to the current line
    else:
        current_line += ' ' + word

# Add the last line to the new list
new_lines.append(current_line)

# Join the new lines into a single string
new_title = '\n'.join(new_lines)

# Set the title of the plot
plt.title(new_title)

# Show the plot
plt.show()
