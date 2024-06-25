import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
name = ["shivam", "mukesh", "ramesh", "hitesh"]
i = 0
for i in range(4):
    # print("Enter the word you want to speak it out by computer")
    s = f"shout out to {name[i]}"
    speaker.Speak(s)
