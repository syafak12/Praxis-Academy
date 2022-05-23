from flask import Flask, render_template
app = Flask(__name__)


@app.route("/profil")
def template_test():
    return render_template('template.html', my_string="hahahahaha!", my_list=[0,1,2,3,4,5])


if __name__ == '__main__':
    app.run(debug=True)
