ip_addr = input("Please enter your IP address")
print("You entered: ", ip_addr)


segment = 1
segment_length = 0
character = ""

#first the pointer starts at a number....the else loop is executed..segment_length is incremented
#when "." is found, segment is incremented and segment_length is reset to zero
# for the last segment continue statement is used to break out of the if loop and still be part of for loop
for character in range(0, len(ip_addr)):
    if ip_addr[character] == ".":
        print("Segment {} contains {} characters".format(segment,segment_length))
        segment += 1;
        segment_length = 0
    else:
        segment_length += 1
        continue


print("Segment {} contains {} characters".format(segment, segment_length))

#or you can use below two lines instead of the continue statement

# if character != ".":
#     print("Segment {} contains {} characters".format(segment, segment_length))


