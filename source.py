opening_html_tag = "<html>"

default_style_set = """
<style>

#header {
    background-color:blue;
    text-align:center;
    color: white   
}

#sidebar_left {
    background-color: lightblue;
    position: absolute;
    width: 15%;
    height: 100%;
    left: 0.5%;
    z-index: 1;
    top: 5%;    
}
#sidebar_right {
    background-color: lightblue;
    position: absolute;
    width: 15%;
    height: 100%;
    left: 84.5%;
    z-index: 1;
    top: 5%; 
}  

#footer {
    background-color:cyan;
    clear:both;
    text-align:center;
    padding:10px;    
}

</style>"""

header = """<head>
    <div id="header">
    <h1>Редактор форм</h1>
    </div>

</head>"""

open_workspace = """<body>
<div>
<div id="sidebar_left"></div>"""

close_workspace = """<div id="sidebar_right"></div>
</div>"""

footer = """<div id="footer"></div>
</body>"""

add_space_buttons = """
<div>
<form action="/add_input_page/" method="get">
<button style="position:absolute;
    width:120px;
    height:60px;
    left: 18%; 
    top: 5%; 
    z-index: 3;
    background-color: lightblue;">
    Добавить поле ввода
    </button>
</form>
<form action="/add_input_page/" method="get">
<button style="position:absolute;
    width:120px;
    height:60px;
    left: 36%; 
    top: 5%; 
    z-index: 3;
    background-color: lightblue;">
    Добавить текстовое поле
    </button>
</form>
<form action="/add_input_page/" method="get">
<button style="position:absolute;
    width:120px;
    height:60px;
    left: 54%; 
    top: 5%;
    z-index: 3;
    background-color: lightblue;">
    Добавить поле выбора ответа
    </button>
</form>
</div>
"""

closer_html_tag = "</html>"

add_input_page = """<!DOCTYPE html>
<html>
<body>

<h1>HTML Форма с кнопкой отправки</h1>

<form action="/action_page.php">
  Фамилия:<br>
  <input type="text" name="lastname" value="Щипунов">
  <br><br>
  <input type="submit" value="Отправить">
</form> 

<p>Если Вы нажмете на кнопку "Отправить", данные форма будут отправлены на страницу "action_page.php".</p>

</body>
</html>"""



