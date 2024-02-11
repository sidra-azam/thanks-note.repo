def generate_thank_you_note(instructor_name, course_name, your_name):
    message = f"Dear {instructor_name},\n\n"
    message += f"I wanted to take a moment to express my heartfelt gratitude for your guidance and support throughout the online Python course .I am thrilled to have completed the {course_name} online course under your expert guidance. Your dedication to teaching and your ability to break down complex concepts made learning {
        course_name} an enjoyable journey.Your clear explanations, insightful examples, and patience helped me grasp complex concepts and improve my coding skills significantly. Your encouragement and feedback motivated me to keep pushing myself and strive for excellence in every assignment and project. Thank you for your patience, encouragement, and for sharing your knowledge with us. I am excited to apply what I've learned and continue my programming journey.Thank you once again for sharing your expertise with us. Your impact will be felt far beyond the duration of this course, and I am grateful to have had the opportunity to learn from you.\n\n"
    message += "Sincerely,\n"
    message += your_name
    return message


# Input details
instructor_name = "Muhammad Yahya"
course_name = "Python Basics"
your_name = "Iqra  ,Sidra"
# Generate and print the thank-you note
thank_you_note = generate_thank_you_note(
    instructor_name, course_name, your_name)
print(thank_you_note)
