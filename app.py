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

@app.route('/days_3011')
def days_3011():
	return render_template("days_3011.html")

@app.route('/days_0112')
def days_0112():
	return render_template("days_0112.html")

@app.route('/days_0212')
def days_0212():
    return render_template("days_0212.html")

@app.route('/days_0312')
def days_0312():          
    return render_template("days_0312.html")
@app.route('/days_0412')
def days_0412():          
    return render_template("days_0412.html")
@app.route('/days_0512')
def days_0512():
    return render_template("days_0512.html")

@app.route('/days_0612')
def days_0612():
    return render_template("days_0612.html")

@app.route('/days_0712')
def days_0712():
    return render_template("days_0712.html")

@app.route('/days_0812')
def days_0812():
    return render_template("days_0812.html")

@app.route('/days_0912')
def days_0912():      
    return render_template("days_0912.html")

@app.route('/days_1012')
def days_1012():                
    return render_template("days_1012.html")

@app.route('/days_1112')
def days_1112():                
    return render_template("days_1112.html")
@app.route('/days_1212')
def days_1212():                
    return render_template("days_1212.html")
@app.route('/days_1312')
def days_1312():                
    return render_template("days_1312.html")
@app.route('/days_1412')
def days_1412():                
    return render_template("days_1412.html")
@app.route('/days_1512')
def days_1512():                
    return render_template("days_1512.html")
@app.route('/days_1612')
def days_1612():                
    return render_template("days_1612.html")
@app.route('/days_1712')
def days_1712():                
    return render_template("days_1712.html")
@app.route('/days_1812')
def days_1812():                
    return render_template("days_1812.html")
@app.route('/days_1912')
def days_1912():                
    return render_template("days_1912.html")
@app.route('/days_2012')
def days_2012():                
    return render_template("days_2012.html")
@app.route('/days_2112')
def days_2112():                
    return render_template("days_2112.html")
@app.route('/days_2212')
def days_2212():                
    return render_template("days_2212.html")
@app.route('/days_2312')
def days_2312():                
    return render_template("days_2312.html")
@app.route('/days_2412')
def days_2412():                
    return render_template("days_2412.html")
@app.route('/days_2512')
def days_2512():                
    return render_template("days_2512.html")
@app.route('/days_2612')
def days_2612():                
    return render_template("days_2612.html")
@app.route('/days_2712')
def days_2712():                
    return render_template("days_2712.html")
@app.route('/days_2812')
def days_2812():                
    return render_template("days_2812.html")
@app.route('/days_2912')
def days_2912():                
    return render_template("days_2912.html")
@app.route('/days_3012')
def days_3012():                
    return render_template("days_3012.html")
@app.route('/days_3112')
def days_3112():                
    return render_template("days_3112.html")



@app.route('/special_gift')
def special_gift():
	return render_template("special_gift.html")

@app.route('/special_gift2')
def special_gift2():
	return render_template("special_gift2.html")

@app.route('/special_gift3')
def special_gift3():
	return render_template("special_gift3.html")

@app.route('/special_gift4')
def special_gift4():
    return render_template("special_gift4.html")

# @app.route('/memories')
# def memories():
#     memory = TextMemory(8758, 8800)
#     messages = memory.get_messages_for_replay()

#     if messages:
#         # Track which senders we've already shown
#         shown_senders = set()
#         processed_messages = []
        
#         for msg in messages:
#             show_sender = msg['sender'] not in shown_senders
#             if show_sender:
#                 shown_senders.add(msg['sender'])
                
#             processed_messages.append({
#                 'sender': msg['sender'],
#                 'content': msg['content'],
#                 'show_sender': show_sender
#             })
        
#         return render_template("memories.html", messages=processed_messages)
    
#     return "No messages found"

@app.route('/random_memory')
def random_memory():
    # Choose random start and end within the allowed range
    start = random.randint(8758, 141914)
    end = start + random.randint(20, 100)
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

        # Build human-friendly memory name and subtitle from message timestamps
        try:
            # Collect all datetimes from messages (expected format: YYYY-MM-DD HH:MM:SS)
            msg_datetimes = [datetime.strptime(m['date'], "%Y-%m-%d %H:%M:%S") for m in messages if 'date' in m]
            if msg_datetimes:
                first_dt = min(msg_datetimes)
                last_dt = max(msg_datetimes)
                # If all messages share the same date, use that date as the memory name
                if first_dt.date() == last_dt.date():
                    memory_name_display = first_dt.date().isoformat()
                    memory_subtitle = f"{first_dt.strftime('%H:%M:%S')} - {last_dt.strftime('%H:%M:%S')}"
                else:
                    memory_name_display = f"{first_dt.date().isoformat()} — {last_dt.date().isoformat()}"
                    memory_subtitle = f"{first_dt.strftime('%Y-%m-%d %H:%M:%S')} — {last_dt.strftime('%Y-%m-%d %H:%M:%S')}"
            else:
                # Fallback if no date fields present
                memory_name_display = memory_name.replace('_', ' ').title()
                memory_subtitle = ""
        except Exception:
            memory_name_display = memory_name.replace('_', ' ').title()
            memory_subtitle = ""

        return render_template("memories.html",
                               messages=processed_messages,
                               memory_name=memory_name_display,
                               memory_subtitle=memory_subtitle,
                               description="")

    return "No messages found in this memory"


@app.route('/random')
def random_num():
	random_number = random.randint(0,10)
	return f"{random_number}"









if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
