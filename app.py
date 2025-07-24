from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/user-dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

@app.route('/staff-dashboard')
def staff_dashboard():
    return render_template('staff_dashboard.html')

@app.route('/festival-planner')
def festival_planner():
    return render_template('festival_planner.html')

@app.route('/group-match')
def group_match():
    return render_template('group_match.html')

@app.route('/budget-generator')
def budget_generator():
    return render_template('budget_generator.html')

@app.route('/hidden-gems')
def hidden_gems():
    return render_template('hidden_gems.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/offline-kit')
def offline():
    return render_template('offline.html')

@app.route('/culture-tips')
def culture_tips():
    return render_template('culture_tips.html')

@app.route('/voice-guide')
def voice_guide():
    return render_template('voice_guide.html')

@app.route('/marketplace')
def marketplace():
    return render_template('marketplace.html')

@app.route('/eco-tracker')
def eco_tracker():
    return render_template('eco_tracker.html')

@app.route('/souvenir-scanner')
def souvenir_scanner():
    return render_template('souvenir_scanner.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

if __name__ == '__main__':
    app.run(debug=True)
