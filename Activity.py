import colorama
from colorama import Fore, Style       
from textblob import TextBlob
colorama.init(autoreset=True)
print(f"{Fore.CYAN} Welcome to sentiment analysis!{Style.RESET_ALL}")

user_name =  input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()

print(f"\n {Fore.CYAN} Hello Agent {user_name}!")

print(f"\n Type a sentence and I will analyze your sentences with TextBlob: ")

user_input = input(f"{Fore.GREEN} Enter 'exit' quit >> {Style.RESET_ALL}").strip()

while True:
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell Agent {user_name}")
        break
    
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        break
    elif polarity > -0.25:
        sentiment_type = "Negative"
        color = Fore.GREEN
        break
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        break
        
print(f"{color}{sentiment_type} Sentiment Detected! " f"Polarity: ({polarity: .2f}) {Style.RESET_ALL}")