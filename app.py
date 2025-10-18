from flask import Flask, request, redirect, url_for, session, escape;
import random;

app = Flask(__name__)
# NOTE: for production set a secure random secret key
app.secret_key = 'dev-secret-for-local'


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral (up to 3999) to integer."""
    s = s.upper()
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and vals.get(s[i], 0) < vals.get(s[i+1], 0):
            total += vals.get(s[i+1], 0) - vals.get(s[i], 0)
            i += 2
        else:
            total += vals.get(s[i], 0)
            i += 1
    return total


def int_to_roman(num: int) -> str:
    """Convert integer to Roman numeral (supports 1..3999)."""
    if num <= 0 or num >= 4000:
        return ""
    pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = []
    for val, sym in pairs:
        while num >= val:
            res.append(sym)
            num -= val
    return ''.join(res)


@app.route('/')
def home():
    return (
        "<h2>PyGames</h2>"
        "<p>Choose one of the mini tools below:</p>"
        "<ol>"
        "<li><a href='/time'>Time Converter</a></li>"
        "<li><a href='/rock'>Rock, Paper, Scissor</a></li>"
        "<li><a href='/length'>Length Converter</a></li>"
        "<li><a href='/quiz'>Quiz Game</a></li>"
        "<li><a href='/random'>Random Number Generator</a></li>"
        "<li><a href='/hangman'>Hangman (simple)</a></li>"
        "<li><a href='/todo'>To-do List</a></li>"
        "<li><a href='/spender'>Spender-Checker</a></li>"
        "<li><a href='/multiplier'>Multiplier</a></li>"
        "<li><a href='/roman'>Roman Numeral Converter</a></li>"
        "</ol>"
    )


@app.route('/time', methods=['GET', 'POST'])
def time_converter():
    if request.method == 'POST':
        try:
            seconds = float(request.form['seconds'])
        except Exception:
            return "Invalid input. Please enter a number. <a href='/time'>Go back</a>"
        minutes = seconds / 60
        hours = seconds / 3600
        days = seconds / 86400
        weeks = days / 7
        months = days / 30
        years = days / 365
        return (
            f"<h3>Results</h3>"
            f"Seconds: {seconds}<br>"
            f"Minutes: {minutes:.4f}<br>"
            f"Hours: {hours:.6f}<br>"
            f"Days: {days:.8f}<br>"
            f"Weeks: {weeks:.8f}<br>"
            f"Months (approx): {months:.8f}<br>"
            f"Years (approx): {years:.8f}<br>"
            "<br><a href='/time'>Back</a> | <a href='/'>Menu</a>"
        )
    return (
        "<h3>Time Converter</h3>"
        "<form method='post'>Seconds: <input name='seconds'/> <input type='submit' value='Convert'/></form>"
        "<p><a href='/'>Menu</a></p>"
    )


@app.route('/rock', methods=['GET', 'POST'])
def rock_paper_scissor():
    choices = ['rock', 'paper', 'scissor']
    if request.method == 'POST':
        user = request.form.get('choice', '').lower()
        if user not in choices:
            return "Invalid choice. <a href='/rock'>Try again</a>"
        comp = random.choice(choices)
        if user == comp:
            outcome = 'Stalemate.'
        elif (user == 'rock' and comp == 'scissor') or (user == 'paper' and comp == 'rock') or (user == 'scissor' and comp == 'paper'):
            outcome = 'You won!'
        else:
            outcome = 'You lost.'
        return f"Computer chose {comp}. {outcome} <br><a href='/rock'>Play again</a> | <a href='/'>Menu</a>"
    return (
        "<h3>Rock, Paper, Scissor</h3>"
        "<form method='post'>"
        "<select name='choice'><option>rock</option><option>paper</option><option>scissor</option></select>"
        " <input type='submit' value='Play'/></form>"
        "<p><a href='/'>Menu</a></p>"
    )


@app.route('/length', methods=['GET', 'POST'])
def length_converter():
    if request.method == 'POST':
        try:
            inches = float(request.form['inches'])
        except Exception:
            return "Invalid input. <a href='/length'>Go back</a>"
        feet = inches / 12
        yards = feet / 3
        miles = yards / 1760
        millimeters = inches * 25.4
        centimeters = inches * 2.54
        meters = inches / 39.37
        kilometers = inches / 39370
        return (
            f"<h3>Length Results</h3>"
            f"{inches} inches = {feet:.6f} feet = {yards:.6f} yards = {miles:.9f} miles<br>"
            f"{millimeters:.4f} mm, {centimeters:.4f} cm, {meters:.6f} m, {kilometers:.9f} km<br>"
            "<br><a href='/length'>Back</a> | <a href='/'>Menu</a>"
        )
    return (
        "<h3>Length Converter</h3>"
        "<form method='post'>Inches: <input name='inches'/> <input type='submit' value='Convert'/></form>"
        "<p><a href='/'>Menu</a></p>"
    )


@app.route('/quiz', methods=['GET', 'POST'])
def quiz_game():
    questions = [
        ("Earth's inner core is", [('a','solid'), ('b','liquid'), ('c','choice a and b'), ('d','lava')], 'a', 'Earth has two parts to its core. The inner core is solid.'),
        ("Most common letter in English?", [('a','A'), ('b','E'), ('c','I'), ('d','O')], 'b', 'E appears in about 11% of words.'),
        ("Sum of interior angles of a triangle?", [('a','90'), ('b','180'), ('c','270'), ('d','360')], 'b', 'Always 180 degrees.'),
        ("Who was the first US president?", [('a','Abraham Lincoln'), ('b','Thomas Jefferson'), ('c','George Washington'), ('d','John Adams')], 'c', 'George Washington served from 1789 to 1797.'),
    ]
    if request.method == 'POST':
        score = 0
        explanations = []
        for idx, (_, opts, correct, explanation) in enumerate(questions, start=1):
            ans = request.form.get(f'q{idx}', '')
            if ans == correct:
                score += 1
                explanations.append(f'Question {idx}: Correct - {explanation}')
            else:
                explanations.append(f'Question {idx}: Incorrect - {explanation}')
        # bonus
        bonus = request.form.get('bonus', '')
        if bonus == 'd':
            score += 2
            explanations.append('Bonus: Correct - Maine is closest to Africa.')
        else:
            explanations.append('Bonus: Incorrect - Maine is closest to Africa.')
        return (
            f"<h3>Results</h3>Score: {score} / 6<br><br>" + "<br>".join(explanations) + "<br><a href='/quiz'>Play again</a> | <a href='/'>Menu</a>"
        )
    # build form
    form = ["<h3>Quiz Game</h3><form method='post'>"]
    for i, (q, opts, correct, explanation) in enumerate(questions, start=1):
        form.append(f"<b>Question {i}</b>: {q}<br>")
        for val, text in opts:
            form.append(f"<label><input type='radio' name='q{i}' value='{val}' required/> {val}. {text}</label><br>")
        form.append("<br>")
    form.append("<b>Bonus (worth 2 points)</b>: Which US state is closest to Africa?<br>")
    form.append("<label><input type='radio' name='bonus' value='a' required/> a. Florida</label><br>")
    form.append("<label><input type='radio' name='bonus' value='b'/> b. South Carolina</label><br>")
    form.append("<label><input type='radio' name='bonus' value='c'/> c. Massachusetts</label><br>")
    form.append("<label><input type='radio' name='bonus' value='d'/> d. Maine</label><br>")
    form.append("<br><input type='submit' value='Submit'/> </form>")
    form.append("<p><a href='/'>Menu</a></p>")
    return ''.join(form)


@app.route('/random', methods=['GET', 'POST'])
def random_number():
    if request.method == 'POST':
        try:
            minimum = int(request.form['minimum'])
            maximum = int(request.form['maximum'])
            if maximum - minimum <= 1:
                return "Maximum should be at least two greater than minimum. <a href='/random'>Back</a>"
            num = random.randint(minimum + 1, maximum - 1)
        except Exception:
            return "Invalid input. <a href='/random'>Back</a>"
        return f"Random number between {minimum} and {maximum}: <b>{num}</b><br><a href='/random'>Again</a> | <a href='/'>Menu</a>"
    return "<h3>Random Number Generator</h3><form method='post'>Min: <input name='minimum'/> Max: <input name='maximum'/> <input type='submit' value='Generate'/></form><p><a href='/'>Menu</a></p>"


@app.route('/hangman', methods=['GET', 'POST'])
def hangman():
    # simplified: user supplies guesses (comma separated) and we reveal the word
    word = 'PYTHON'
    if request.method == 'POST':
        guesses_raw = request.form.get('guesses', '')
        guesses = {g.strip().upper() for g in guesses_raw.split(',') if g.strip()}
        revealed = ' '.join([ch if ch in guesses else '_' for ch in word])
        incorrect = [g for g in guesses if g not in word]
        msg = f"Word: {revealed}<br>Incorrect guesses: {', '.join(incorrect)} ({len(incorrect)})<br>"
        if all(ch in guesses for ch in word):
            msg += "Congratulations! You guessed the word correctly." + "<br>"
        else:
            msg += "Try again (submit more guesses separated by commas)." + "<br>"
        msg += "<a href='/hangman'>Back</a> | <a href='/'>Menu</a>"
        return msg
    return "<h3>Hangman (simple)</h3><form method='post'>Enter guesses (comma separated, letters):<br><input name='guesses' style='width:300px'/> <input type='submit' value='Check'/></form><p><a href='/'>Menu</a></p>"


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    # session-backed simple todo list
    todos = session.get('todos', [])
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            task = request.form.get('task', '').strip()
            priority = request.form.get('priority') == 'on'
            if task:
                if priority:
                    todos.insert(0, task)
                else:
                    todos.append(task)
                session['todos'] = todos
        elif action == 'remove':
            idx = int(request.form.get('index', -1))
            if 0 <= idx < len(todos):
                todos.pop(idx)
                session['todos'] = todos
        return redirect(url_for('todo'))
    # GET
    out = ['<h3>To-do List</h3>']
    out.append("<ul>")
    for i, t in enumerate(todos):
        out.append(f"<li>{escape(t)} <form style='display:inline' method='post'><input type='hidden' name='action' value='remove'/><input type='hidden' name='index' value='{i}'/><button type='submit'>Done</button></form></li>")
    out.append('</ul>')
    out.append("<form method='post'>Add task: <input name='task'/> Priority: <input type='checkbox' name='priority'/> <input type='hidden' name='action' value='add'/> <input type='submit' value='Add'/></form>")
    out.append("<p><a href='/'>Menu</a></p>")
    return ''.join(out)


@app.route('/spender', methods=['GET', 'POST'])
def spender():
    if request.method == 'POST':
        lines = request.form.get('items', '').strip().splitlines()
        items = []
        total = 0
        for line in lines:
            if not line.strip():
                continue
            try:
                name, price = line.split(',')
                price = int(price.strip())
                items.append((name.strip(), price))
                total += price
            except Exception:
                return "Invalid items format. Use one item per line: name,price . <a href='/spender'>Back</a>"
        try:
            money = int(request.form.get('money', '0'))
        except Exception:
            return "Invalid money amount. <a href='/spender'>Back</a>"
        if money >= total:
            change = money - total
            return f"Total: ${total}. You have enough money. Change: ${change}. <a href='/spender'>Back</a> | <a href='/'>Menu</a>"
        else:
            need = total - money
            return f"Total: ${total}. You need ${need} more. <a href='/spender'>Back</a> | <a href='/'>Menu</a>"
    example = "apple,10\nbanana,5\nshirt,20"
    return ("<h3>Spender-Checker</h3>"
            "<p>Enter one item per line as: name,price (price as integer)</p>"
            f"<form method='post'>Items:<br><textarea name='items' rows='6' cols='40'>{example}</textarea><br>How much money do you have? $<input name='money'/> <input type='submit' value='Check'/></form>"
            "<p><a href='/'>Menu</a></p>")


@app.route('/multiplier', methods=['GET', 'POST'])
def multiplier():
    if request.method == 'POST':
        try:
            table = int(request.form.get('table'))
        except Exception:
            return "Invalid table. <a href='/multiplier'>Back</a>"
        lines = []
        for i in range(0, 13):
            lines.append(f"{i} times {table} is {i*table}")
        return '<br>'.join(lines) + "<br><a href='/multiplier'>Back</a> | <a href='/'>Menu</a>"
    return ("<h3>Multiplier</h3><form method='post'>Table (2-12): <input name='table'/> <input type='submit' value='Show'/></form><p><a href='/'>Menu</a></p>")


@app.route('/roman', methods=['GET', 'POST'])
def roman():
    if request.method == 'POST':
        r1 = request.form.get('roman1','').strip()
        r2 = request.form.get('roman2','').strip()
        try:
            n1 = roman_to_int(r1) if r1 else 0
            n2 = roman_to_int(r2) if r2 else 0
        except Exception:
            return "Invalid roman numeral. <a href='/roman'>Back</a>"
        total = n1 + n2
        roman_total = int_to_roman(total)
        return (f"First: {r1.upper()} = {n1}<br>Second: {r2.upper()} = {n2}<br>Sum: {total} = {roman_total}<br>"
                "<a href='/roman'>Back</a> | <a href='/'>Menu</a>")
    return ("<h3>Roman Numeral Converter</h3>"
            "<form method='post'>Roman 1: <input name='roman1'/> Roman 2: <input name='roman2'/> <input type='submit' value='Add'/></form>"
            "<p><a href='/'>Menu</a></p>")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
    intro = "This is PyGames. You can play mini python games and quizes, as well as get useful conversions here. Choose one from the options below: <br> <br>1. Time Converter <br> 2. Rock, Paper, Scissor, Shoot! <br> 3. Length Converter <br> 4. Quiz Game <br> 5. Rondom Number Generator <br> 6. Hangman <br> 7. To-do List <br> 8. Spender Checker <br> 9. Multiplier <br> 10. Roman Numeral Converter <br> <br> Enter a number from 1-10: "
    choice = request
    


if __name__ == '__main__':
    app.run()
