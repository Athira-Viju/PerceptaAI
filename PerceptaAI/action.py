import sptotx
import texttospeech # type: ignore
import datetime
import webbrowser
import weather

 
todo_list=[]
def action(data):
     user_data=data.lower()

     if "what is your name" in user_data:
      texttospeech.text_to_speech("My name is Percepta")
      return "My name is Percepta"
     elif "good night" in user_data:
         texttospeech.text_to_speech ("good night")
         return "good night"
     elif "good morning"   in user_data:
        texttospeech.text_to_speech("Good morning")
        return 'Good morning'
     elif "good evening" in user_data:
         texttospeech.text_to_speech("good evening")
         return "good evening"
     elif "how are you" in user_data:
       texttospeech.text_to_speech("I'm fine,what about you")
       return "I'm fine ,what about you"
     elif any(greeting in user_data for greeting in ["hello","hye","hi","hey"]) :
       texttospeech.text_to_speech("Hello there,how can i help u?")
       return 'Hello there,how can i help u'
     elif "who are you" in user_data:
       texttospeech.text_to_speech("I'm a reflection of you ,here to do whatever you need")

     elif "time now" in user_data:
      current_time=datetime.datetime.now()
      Time=(str)(current_time)+"Hour:",(str)(current_time.minute)+"Minte"
      texttospeech.text_to_speech(Time)
      return Time
     elif "Shut down" in user_data:
      texttospeech.text_to_speech("Okay shuting down")
      return 'Okay shuting down'
     elif "play music" in user_data:
      webbrowser.open("https://open.spotify.com/track/5b3XJ1pjrHO5JtY2PcTjnI?si=2bbf6bde98b64e2a")
      texttospeech.text_to_speech("Heres your song")
      return 'Heres your song'
     elif "open youtube" in user_data:
      webbrowser.open("https://youtube.com")
      texttospeech.text_to_speech("Opening Youtube")
      return 'Opening Youtube'
     elif "open google" in user_data:
      webbrowser.open("https://google.com")
      texttospeech.text_to_speech("Opening Google")
      return 'Opening Google'
     elif "weather" in user_data:
      ans= weather.weather()
      texttospeech.text_to_speech(ans)
      return ans
     elif"see you" in user_data:
       texttospeech.text_to_speech("Take care")
       return" take care"
     elif "thank you" in user_data:
       texttospeech.text_to_speech("No need to thank me ,it's my pleasure to assist you")
       return"No need to thank me,it's my pleasure to assist you "
     elif "add task" in user_data:
       task=user_data.replace("add task","").strip()  
       if task :
         todo_list.append(task)
         texttospeech.text_to_speech(f"Task added:{task}")
         return f"Task added:{task}"
       else:
         texttospeech.text_to_speech("Please specify a task to add.")
         return "Please specify a task to add."
     elif "show task" in user_data:
         if todo_list:
           tasks="\n".join(todo_list)
           texttospeech.text_to_speech(f"Your tasks are:\n{tasks}")
           return f"Your tasks are:\n{tasks}"
         else:
            texttospeech.text_to_speech("No tasks in your list.")
            return "No tasks in your list."
     elif "delete task" in user_data:
       task=user_data.replace("delete task","").strip()
       if task in todo_list:
         todo_list.remove(task)
         texttospeech.text_to_speech(f"Task removed: {task}")
         return f"Task removed: {task}"
       else:
            texttospeech.text_to_speech("Task not found.")
            return "Task not found."


     else:
       texttospeech.text_to_speech("I'm not able to understand")
       return "I'm not able to understand"