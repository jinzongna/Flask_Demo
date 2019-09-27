from flask import Flask, render_template, request

app = Flask(__name__)

# 自动生成的hello world代码
@app.route('/')
def hello_world():
    return 'Hello World!'

# 通过URL传递参数
@app.route('/user/<name>')
def hello_user(name):
    return 'Hello {0}!'.format(name)

# 利用模版显示变量名
@app.route('/city/<city_name>')
def welcome(city_name):
    return render_template('city.html', name=city_name)

# 表单传递参数，模版输出页面
@app.route('/form', methods=['GET', 'POST'])
def form():
    name = None
    if request.method == 'POST' and 'name' in request.form:
        name = request.form['name']
    return render_template('form.html', name=name)

# 添加CSS和javascript
@app.route('/css_js')
def css_js():
    return render_template('css_js.html')

# 遍历列表
@app.route('/go_through_list')
def go_through_list():
    heroes = ["李白", "露娜", "韩信", "阿轲"]
    return render_template('go_through_list.html', heroes=heroes)

# 遍历字典
@app.route("/go_through_dict")
def go_through_dict():
    hero = {"名字": "李白", "属性": "刺客", "铭文": "百穿"}
    return render_template("go_through_dict.html", info=hero)

# 条件渲染
@app.route("/condition/<hero>")
def condition(hero):
    return render_template("condition.html", hero=hero)

# 过滤器的本质就是函数，用来修改变量的显示，格式化，运算等
@app.route('/filters')
def filters():
    return render_template('filters.html')

# 定义自己的过滤器 my_reverse 返转列表
@app.template_filter('my_reverse')
def do_list_reverse(li):
    li.reverse()
    return li


if __name__ == '__main__':
    app.run(port=5001, debug=True)
