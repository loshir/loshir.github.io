from flask import Flask, render_template
from classes import TextMemory
import random
from TextMessages_collection import MEMORY_COLLECTION, get_random_memory, get_memory_by_name
from datetime import date, timedelta, datetime


app = Flask(__name__)

@app.route('/days')
def get_current_week_days():
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())  # Monday
    week_days = [start_of_week + timedelta(days=i) for i in range(7)]
    return [day.day for day in week_days]

@app.route('/home')
def home():
    now = datetime.now()
    month = now.month
    day = now.day
    
    if month == 11 and 24 <= day <= 30:
        return render_template('home.html')
    elif month == 12 and 1 <= day <= 7:
        return render_template('home_week2.html')
    else:
        return render_template('home.html')

@app.route('/home_week2')
def home_week2():
	return render_template("home_week2.html")

@app.route('/home_week3')
def home_week3():
	return render_template("home_week3.html")

@app.route('/home_week4')
def home_week4():
	return render_template("home_week4.html")

@app.route('/days_2411')
def days_2411():
	return render_template("days_2411.html")

@app.route('/days_2711')
def days_2711():
	return render_template("days_2711.html")

@app.route('/days_2811')
def days_2811():
	return render_template("days_2811.html")

@app.route('/days_2911')
def days_2911():
	return render_template("days_2911.html")

@app.route('/memories')
def memories():
    memory = TextMemory(8758, 8800)
    messages = memory.get_messages_for_replay()

    if messages:
        # Track which senders we've already shown
        shown_senders = set()
        processed_messages = []
        
        for msg in messages:
            show_sender = msg['sender'] not in shown_senders
            if show_sender:
                shown_senders.add(msg['sender'])
                
            processed_messages.append({
                'sender': msg['sender'],
                'content': msg['content'],
                'show_sender': show_sender
            })
        
        return render_template("memories.html", messages=processed_messages)
    
    return "No messages found"

@app.route('/random_memory')
def random_memory():
    # Choose random start and end within the allowed range
    start = random.randint(8758, 141914)
    end = random.randint(8758, 141914)
    if start > end:
        start, end = end, start

    memory_name = f"memory_{start}_{end}"

    # Get the messages for this random memory range
    memory = TextMemory(start, end)
    messages = memory.get_messages_for_replay()

    if messages:
        shown_senders = set()
        processed_messages = []

        for msg in messages:
            show_sender = msg['sender'] not in shown_senders
            if show_sender:
                shown_senders.add(msg['sender'])

            processed_messages.append({
                'sender': msg['sender'],
                'content': msg['content'],
                'show_sender': show_sender
            })

        return render_template("memories.html",
                               messages=processed_messages,
                               memory_name=memory_name.replace('_', ' ').title(),
                               description="")

    return "No messages found in this memory"


@app.route('/random')
def random_num():
	random_number = random.randint(0,10)
	return f"{random_number}"









if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)