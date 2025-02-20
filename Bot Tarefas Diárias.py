import schedule
import time
import requests
from datetime import datetime

# Função para obter a previsão do tempo
def get_weather(city="São Paulo"):
    API_KEY = "SUA_CHAVE_DA_API"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"☁️ Clima em {city}: {temp}°C, {description.capitalize()}")
    else:
        print("Erro ao obter dados do clima.")

# Função para buscar as principais notícias
def get_news():
    API_KEY = "SUA_CHAVE_DA_API"
    URL = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={API_KEY}"
    response = requests.get(URL)
    if response.status_code == 200:
        news = response.json()
        print("📰 Principais Notícias:")
        for article in news["articles"][:3]:  # Pegando as 3 principais notícias
            print(f"- {article['title']}")
    else:
        print("Erro ao obter notícias.")

# Função para lembretes
def reminder(message="Beba água! 💧"):
    print(f"🔔 Lembrete: {message}")

# Agendando as tarefas
schedule.every().day.at("08:00").do(get_weather)
schedule.every().day.at("09:00").do(get_news)
schedule.every(2).hours.do(reminder, message="Faça uma pausa e alongue-se! 🧘")

print("🤖 Bot iniciado! Automatizando suas tarefas do dia a dia...")
while True:
    schedule.run_pending()
    time.sleep(60)
