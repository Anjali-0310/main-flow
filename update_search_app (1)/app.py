from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    search = request.args.get('search')
    filter_category = request.args.get('category')

    conn = get_db_connection()
    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if search:
        query += " AND (name LIKE ? OR buyer LIKE ?)"
        params += [f'%{search}%', f'%{search}%']
    
    if filter_category and filter_category != "All":
        query += " AND category = ?"
        params.append(filter_category)

    products = conn.execute(query, params).fetchall()
    conn.close()
    return render_template('index.html', products=products)

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        buyer = request.form['buyer']

        if not name or not category or not buyer:
            flash('All fields are required!')
        else:
            conn.execute('UPDATE products SET name = ?, category = ?, buyer = ? WHERE id = ?',
                         (name, category, buyer, id))
            conn.commit()
            conn.close()
            flash('Product updated successfully!')
            return redirect(url_for('index'))

    return render_template('edit.html', product=product)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM products WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Product deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
